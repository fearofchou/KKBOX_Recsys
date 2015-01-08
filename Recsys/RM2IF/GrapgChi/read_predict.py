ruid_mask = {}
for i in uid_mask.keys():
    ruid_mask[uid_mask[i]] = i
rsid_mask = {}
for i in sid_mask.keys():
    rsid_mask[sid_mask[i]] =i

pred_fn = '/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/exe/_MODEL_sgd.1_of_1'

f = open(pred_fn)
pred = f.readlines()

Top_N = {}

for i in pred:
    i=i.split()
    uid = int(i[0])
    sid = int(i[1])
    pre = float(i[2])

    try:
        Top_N[uid][sid] = pre
    except:
        Top_N[uid] = {}
        Top_N[uid][sid] = pre

import numpy as np
Top_N_idx = {}
N =20
for i in Top_N.keys():
    item = np.array(Top_N[i].items())
    idx = np.argsort(item[:,1])[::-1]

    Top_N_idx[i] = item[:,0][idx[:N]]

Top_N = Top_N_idx
fp = '/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/Top_N_song/'
for i in Top_N.keys():
    ii = ruid_mask[i]
    print i
    f = open(fp + '%d'%(ii),'w')
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

