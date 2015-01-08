import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from per_user_lis_log import *
from song_meta2dict import *

song_meta = song_meta2dict()
import numpy as np
UIR = {}
inter_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/internal_member/2014'

UIR,_,_,_ = user_log2dict(UIR,inter_user_log_fn)

import pickle
with open('/home/fearofchou/KKBOX_transition/gen_data/sid_mask') as f:
    sid_mask = pickle.load(f)

csid = [1700795,1562494,1562494,15370242,19528752,10883526,21802114]
Top_IIR_pred = {}
'''
Top_N = 10
for i in UIR.keys():
    item = np.array(UIR[i].items())
    idx = np.argsort(item[:,1])[::-1]
    tsid = item[:,0][idx[:Top_N]]

    for j in tsid:
        Top_IIR_pred[j]={}
        for k in sorted(sid_mask.keys()):
            Top_IIR_pred[j][k] =1
'''
for j in csid:
    Top_IIR_pred[j]={}
    for k in sorted(sid_mask.keys()):
        Top_IIR_pred[j][k] =1

for val in Top_IIR_pred.keys():
    try:
        ti = song_meta[val]['title']
    except:
        continue
    ge = song_meta[val]['genre']
    rd = song_meta[val]['release date']
    at = song_meta[val]['artist']

    print '%d %s %s %s %s'%(val,ti,at,rd,ge[:-1])

print 'Write'
f = open('/home/fearofchou/KKBOX_transition/gen_data/top_pred','w')


for sid_s in Top_IIR_pred.keys():
    for sid_e in Top_IIR_pred[sid_s].keys():

        msid_s = sid_mask[sid_s]
        msid_e = sid_mask[sid_e]
        f.write('%d %d 0\n'%(msid_s,msid_e))

f.close()
