import pickle
import subprocess
import os,sys
import shutil
import numpy as np
ex = '/home/fearofchou/Tools/Recsys/libMF/libmf '
def libMF_convert(data):
    co = 'convert '
    da = '%s '%(data)
    out_da = '%s '%(data+'.binary')
    print ex + co + da + out_da
    subprocess.call( ex + co + da +out_da,shell = True)

def libMF_predict(tr_da,te_da):
    trm = tr_da.split('/')[-1]
    co = 'predict '
    tes_da = '%s '%(te_da+'.binary')
    mod_da = '%s '%(tr_da+'.model')
    pre_da = '%s'%(te_da+'train_%s'%(trm))
    subprocess.call( ex + co + tes_da + mod_da  + pre_da,shell = True)

with open('/home/fearofchou/KKBOX_transition/gen_data/sid_mask') as f:
    sid_mask = pickle.load(f)

sid = sorted(sid_mask.keys())

out_fn = '/home/fearofchou/KKBOX_transition/gen_data/all_pred/all_pred'
out_f = open(out_fn,'w')
for i in sid:
    fn ='/home/fearofchou/KKBOX_transition/gen_data/all_pred/sid_all.pred'
    f = open(fn,'w')
    t_sid = sid_mask[i]
    print t_sid
    for j in sid:

        p_sid = sid_mask[j]
        f.write('%d %d 0\n'%(t_sid,p_sid))

    f.close()
    tr_fn = '/home/fearofchou/KKBOX_transition/gen_data/II_rank_2014'
    te_fn = fn

    libMF_convert(te_fn)
    libMF_predict(tr_fn,te_fn)

    fn = '/home/fearofchou/KKBOX_transition/gen_data/all_pred/sid_all.predtrain_II_rank_2014'
    f = open(fn)
    pred = np.array(f.readlines()).astype(float)
    idx = np.argsort(pred)[::-1]

    out_f.write('%d'%(i))
    for i in idx[:10000]:
        out_f.write('\t%d'%(sid[i]))

    out_f.write('\n')
out_f.close()

