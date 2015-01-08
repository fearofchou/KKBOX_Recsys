import numpy as np
import subprocess
import os,sys
import shutil

ex = '/home/fearofchou/Tools/Recsys/graphlab/release/toolkits/collaborative_filtering/'

def ALS(ex,tr,mi,vf):
    me = 'als '
    sl = '--lambda=1e-4 '
    qu = '--quiet=1'
    pr = '--predictions=%s%s_%s '%(tr[:-1],me)
    cmd = ex+me+tr+pr+sl+mi+vf
    print cmd
    subprocess.call( cmd,shell = True)

def SGD(ex,tr,mi,vf):
    me = 'sgd '
    sg = '--gamma=1e-4 '
    sl = '--lambda=0.0001 '
    par = mi[:-1]+sg[:-1]+sl[:-1]+vf
    pr = '--predictions=%s%s_%s '%(tr[:-1],me,par)
    cmd = ex+me+tr+pr+sl+sg+mi+vf
    print cmd
    subprocess.call( cmd,shell = True)

def SVDpp(ex,tr,mi,vf):
    me = 'svdpp '
    sg = '--gamma=1e-10'
    sl = '--lambda=1e-8 '
    pr = '--predictions=%s_MODEL_%s '%(tr[:-1],me)
    cmd = ex+me+tr+pr+sg+sl+mi+vf
    print cmd
    subprocess.call( cmd,shell = True)

vector_size = 10
ite =20

tr_fn = '/home/fearofchou/TEST_MF/data/'
tr = '%s '%(tr_fn)
mi = '--max_iter=%d '%(ite)
vf = '--D=%d'%(vector_size)

SGD(ex,tr,mi,vf)
#ALS(ex,tr,mi,vf)
#SVDpp(ex,tr,mi,vf)


