fn = '/home/fearofchou/KKBOX_transition/gen_data/sid_mask'
import pickle
with open(fn) as f:
    sid_mask = pickle.load(f)
sm = np.array(sorted(sid_mask.keys()))

import multiprocessing as mp
import numpy as np

def pred_all(i):
    if i%1000==0:
        print i
    fn = '/home/fearofchou/KKBOX_transition/gen_data/all_pred/top_%d'%(i+1)
    top_song = []
    uid = i+1
    for j in range(VL-1):
        sid = j+1
        pred = w0 + all_w['uid'][uid] + all_w['sid'][sid] + np.dot(all_v['uid'][uid],all_v['sid'][sid])
        top_song.append(pred)
    idx = np.argsort(top_song)[::-1]

    return [uid,sm[idx[:10000]]]
    '''
    with open(fn,'w') as f:
        f.write('%d'%(sm[uid-1]))
        for k in idx:
            f.write(' %d'%(sm[k-1]))
        f.write('\n')
    '''

p = mp.Pool(processes=32)
'''
for i in range(100-1):
    fn = '/home/fearofchou/KKBOX_transition/gen_data/all_pred/top_%d'%(i+1)
    #p.apply_async(pred_all,(fn,i,))
p.close()
p.join()
'''
re=p.map(pred_all,range(VL-1))

