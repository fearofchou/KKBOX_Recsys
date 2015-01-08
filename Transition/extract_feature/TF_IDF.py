import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from per_user_lis_log import *
from song_meta2dict import *

song_meta = song_meta2dict()
import numpy as np
UIR = {} #user item rating matrix
inter_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/internal_member/2014'
KKBOX_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/play_count_log_2014'

UIR,_,_,_ = user_log2dict(UIR,inter_user_log_fn)
UIR,_,_,_ = user_log2dict(UIR,KKBOX_user_log_fn)

IIR = {}
rang = 0.1

sid_TF = {}
sid_IDF = {}

from scipy import stats
for i,uid in enumerate(UIR.keys()):
    if (i+1)%1000==0:
        print '%d--%d'%(i,len(UIR.keys()))
        #break
    item = np.array(UIR[uid].items())
    idx = np.argsort(item[:,1])[::-1]

    tar = item[:,1][idx]
    if len(np.unique(tar))<10:
        continue
    N= np.ceil(len(idx)*rang)
    if N>100:
        N=100
    ssid = item[:,0][idx[:N]]

    for sid_s in ssid:
        if sid_s not in IIR:
            IIR[sid_s] = {}
        for sid_e in ssid:
            if sid_s == sid_e:
                continue

            try:
                IIR[sid_s][sid_e] += 1
            except:
                IIR[sid_s][sid_e] = 1

#TF
for i in IIR.keys():
    item = np.array(IIR[i].items())
    sid_TF[i] = item[:,1].sum()

    for j in item[:,0]:
        try:
            sid_IDF[j] += 1
        except:
            sid_IDF[j] = 1


sid_mask = {}
for idx,val in enumerate(sorted(IIR.keys())):
    sid_mask[val] = idx+1

import pickle
with open('/home/fearofchou/KKBOX_transition/gen_data/sid_mask','w') as f:
    pickle.dump(sid_mask,f)

item = np.array(sid_IDF.items())
#rank
idx = np.argsort(item[:,1])[::-1]
rank = np.arange(len(idx))+1

zipfs = item[idx,1]*rank
ssid = item[idx,0]

sid_zipfs = {}
for i,j in enumerate(ssid):
    sid_zipfs[j] = zipfs[i]
maxIDF = item[:,1].max()
'''
M = float(maxIDF/2)
S = 10
X = np.arange(maxIDF)+1
GN = np.exp( -(X-M)**2/2*S**2 ) / (np.sqrt(S)*np.sqrt(2*np.pi))
'''
print 'Write'
fu = 'TF-Zipfs'
fp = '/home/fearofchou/KKBOX_transition/gen_data/'
f = open(fp+'II_rank_%s_2014'%(fu),'w')

TL = len(sid_TF.keys())
for sid_s in IIR.keys():
    for sid_e in IIR[sid_s].keys():
        tar = float(IIR[sid_s][sid_e])
        TF = tar/sid_TF[sid_s]

        if fu == 'log':
            tar = np.log2( 1 + IIR[sid_s][sid_e])
        if fu == 'TF':
            tar = TF
        if fu == 'TF-IDF':
            IDF = np.log(maxIDF/sid_IDF[sid_e])
            tar = TF*IDF
        if fu == 'TF-GN':
            IDF = GN[sid_IDF[sid_e]-1]*10
            tar = TF*IDF
        if fu == 'TF-Zipfs':
            IDF = np.log( sid_zipfs[sid_e]  )
            tar = TF*IDF

        msid_e = sid_mask[sid_e]
        msid_s = sid_mask[sid_s]
        f.write('%d %d %f\n'%(msid_s,msid_e,tar))

f.close()

