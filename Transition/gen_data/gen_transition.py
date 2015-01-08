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
pop_sid = []

from scipy import stats
for i,uid in enumerate(UIR.keys()):
    print '%d--%d'%(i,len(UIR.keys()))
    item = np.array(UIR[uid].items())
    idx = np.argsort(item[:,1])[::-1]
    print '%d==%d'%(uid,len(idx))
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
                pop_sid.append(sid_s)
            except:
                IIR[sid_s][sid_e] = 1

sid_mask = {}
for idx,val in enumerate(sorted(IIR.keys())):
    sid_mask[val] = idx+1

import pickle
with open('/home/fearofchou/KKBOX_transition/gen_data/sid_mask','w') as f:
    pickle.dump(sid_mask,f)

print 'Write'
fp = '/home/fearofchou/KKBOX_transition/gen_data/'
f = open(fp+'II_rank_2014','w')

for sid_s in IIR.keys():
    for sid_e in IIR[sid_s].keys():

        tar = np.log2( 1 + IIR[sid_s][sid_e])
        msid_e = sid_mask[sid_e]
        msid_s = sid_mask[sid_s]
        f.write('%d %d %f\n'%(msid_s,msid_e,tar))

f.close()


