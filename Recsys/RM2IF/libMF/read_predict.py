import pickle
with open('/home/fearofchou/KKBOX_Recsys/gen_data/stat/sid_mask') as f:
    sid_mask = pickle.load(f)
with open('/home/fearofchou/KKBOX_Recsys/gen_data/stat/uid_mask') as f:
    uid_mask = pickle.load(f)

import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from song_meta2dict import *
print 'Read song meta'
song_meta = song_meta2dict()

print 'Transform sid mask to ruid'
ruid_mask = {}
for i in uid_mask.keys():
    ruid_mask[uid_mask[i]] = i
rsid_mask = {}
for i in sid_mask.keys():
    rsid_mask[sid_mask[i]] =i

import glob
pred_fn =glob.glob( '/home/fearofchou/KKBOX_Recsys/gen_data/libMF/pred/*_g_*')
usid_fn = '/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/interl.pred'


print 'Read pred data'
f = open(usid_fn)
usid_fn = f.readlines()

import glob
for fn in pred_fn:
    par = fn.split('train_')[-1]
    f = open(fn)
    pred = f.readlines()

    print 'Read pred data to dict'
    Top_N = {}
    for idx,i in enumerate(usid_fn):
        i=i.split()
        uid = int(i[0])
        sid = int(i[1])
        pre = float(pred[idx][:-1])

        try:
            Top_N[uid][sid] = pre
        except:
            Top_N[uid] = {}
            Top_N[uid][sid] = pre

    Top_N_test = Top_N
    print 'Sort top song'
    import numpy as np
    Top_N_idx = {}
    N =20
    for i in Top_N.keys():
        print i
        item = np.array(Top_N[i].items())
        idx = np.argsort(item[:,1])[::-1]

        Top_N_idx[i] = item[:,0][idx[:N]]

    Top_N = Top_N_idx
    fp = '/home/fearofchou/KKBOX_Recsys/gen_data/libMF/Top_N_song/'
    for i in Top_N.keys():
        ii = ruid_mask[i]
        print i
        f = open(fp + '%d_%s'%(ii,par),'w')
        for j in Top_N[i]:
            val = rsid_mask[j]
            try:
                ge = song_meta[val]['genre']
                rd = song_meta[val]['release date']
                at = song_meta[val]['artist']
                ti = song_meta[val]['title']

                f.write('%d %s %s %s %s'%(val,ti,at,rd,ge))
            except:
                f.write('%d\n'%(val))

        f.close()

