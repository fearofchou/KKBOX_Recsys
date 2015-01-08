import numpy as np
import subprocess
import os,sys
import shutil
#input Resys format
#user_id::item_id::rating
#1 10 5

ex = '/home/fearofchou/Tools/Recsys/libMF/libmf '
def libMF_convert(data):
    co = 'convert '
    da = '%s '%(data)
    out_da = '%s '%(data+'.binary')
    print ex + co + da + out_da
    subprocess.call( ex + co + da +out_da,shell = True)

def libMF_train(data,tp):
    co = 'train '
    bin_da = '%s '%(data+'.binary')
    out_da = '%s'%(data+'.model')
    print ex + co + tp + bin_da + out_da
    subprocess.call( ex + co + tp + bin_da +out_da,shell = True)

def libMF_predict(tr_da,te_da,g,pq):
    trm = tr_da.split('/')[-1]
    co = 'predict '
    tes_da = '%s '%(te_da+'.binary')
    mod_da = '%s '%(tr_da+'.model')
    pre_da = '%s'%(te_da+'train_%s_g_%f_pq_%f'%(trm,g,pq))
    subprocess.call( ex + co + tes_da + mod_da  + pre_da,shell = True)


tr_fn = '/home/fearofchou/KKBOX_Recsys/gen_data/libMF/ZS_2014'
te_fn = '/home/fearofchou/KKBOX_Recsys/gen_data/libMF/pred/interl.pred'


#train model
di = '-k 40 '
te = '-t 40 '
ub = '-ub 1 '
ib = '-ib 1 '
#rs = '--rand-shuffle '
#system
ob = '--obj '
ns = '--no-use-avg '
tm = '--tr-rmse '
th = '-s 16 ' #number of thread
va = '-v %s '%(te_fn+'.binary')
g = [2e-3,3e-3,4e-3,5e-2]
pq = [0e-0]

libMF_convert(tr_fn)
libMF_convert(te_fn)
for i in g:
    for j in pq:

        gr = '-g %f '%(i)
        pr = '-p %f '%(j)
        qr = '-q %f '%(j)

        tpar = tm+ob+di+qr+pr+gr+ub+ib+ns
        libMF_train(tr_fn,tpar)
        libMF_predict(tr_fn,te_fn,i,j)


