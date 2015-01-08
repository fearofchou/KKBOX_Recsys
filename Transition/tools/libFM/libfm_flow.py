import numpy as np
import subprocess
import os,sys,glob
import shutil


fea = ['uid','sid']
FM = '/home/fearofchou/Tools/Recsys/libFM/bin/libFM '
def BS_train(par):
    subprocess.call(par,shell = True)

fp = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/'
os.chdir(fp)
tar_tr = 'tar.train'
tar_te = 'tar.test'

ta = ' -task r'
fi = ' -train ' + tar_tr + ' -test ' + tar_te
di = ' -dim 1,1,10'
it = ' -iter 50'
ma = ' -method als'
rg = ' -regular 1,1,10'
ou = ' -out out_org.pred'
re = ' -relation '

sa = ' -save '
la = ' -load '

for i in fea:
    re = re+i
    sa = sa+i
    la = la+i
    if i != fea[-1]:
        re=re+','
        sa=sa+'_'
        la=la+'_'
    if i == fea[-1]:
        sa=sa+'.model'
        la=la+'.model'


par = FM+ta+fi+ma+rg+di+re+it+ou
print par
BS_train(par)
