import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from per_user_lis_log import *
from song_meta2dict import *

inter_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/internal_member/2014'
user_log = {}
song_meta = song_meta2dict()
user_log,_,uid_mask,sid_mask = user_log2dict(user_log,inter_user_log_fn)

uk = user_log.keys()

view_N =100
import numpy as np
while 1:
    er = []
    print uk
    in_uid = raw_input('user idx:')
    in_uid = uk[int(in_uid)]
    #try:
    out = np.array(user_log[int(in_uid)].items())
    idx = np.argsort(out[:,1])
    idx = idx[::-1]

    sort_sid = out[:,0][idx]
    sort_tar = out[:,1][idx]

    for idx,val in enumerate(sort_sid):
        if idx>view_N:
            break
        try:
            ti = song_meta[val]['title']
        except:
            er.append(val)
            continue
        ge = song_meta[val]['genre']
        rd = song_meta[val]['release date']
        at = song_meta[val]['artist']

        out_std = '%d %d %s %s %s %s'%(val,sort_tar[idx],ti,at,rd,ge[:-1])
    #except:
        print out_std
    print  er
