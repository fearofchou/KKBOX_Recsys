#read model
rel = ['uid','sid']
fea = ''
for i in rel:
    fea = fea+i
    if i!=rel[-1]:
        fea = fea + '_'

fn = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/%s.model.v'%(fea)
with open(fn) as f:
    v = f.readlines()
fn = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/%s.model.w'%(fea)
with open(fn) as f:
    w = f.readlines()
fn = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/%s.model.w0'%(fea)
with open(fn) as f:
    w0 = f.readlines()

w0 = float(w0[0][:-1])

fn = '/home/fearofchou/KKBOX_transition/gen_data/sid_mask'
import pickle
with open(fn) as f:
    sid_mask = pickle.load(f)

import numpy as np
all_v = {}
rel = ['uid','sid']
for i in rel:
    all_v[i] = {}

for iidx,i in enumerate(v):
    i = i.split('\t')
    VL = len(i)/len(rel)

    for idx,j in enumerate(i):
        rel_idx = idx/VL
        if iidx == 0:
            all_v[rel[rel_idx]][idx%VL] = [float(j)]
        else:
            all_v[rel[rel_idx]][idx%VL].append(float(j))

all_w = {}
for i in rel:
    all_w[i] = {}
for idx,i in enumerate(w):
    rel_idx = idx/VL
    all_w[rel[rel_idx]][idx%VL] = float(i)

fn = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/uid.test'
f=open(fn)
uid_te = f.readlines()
f.close()
fn = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/sid.test'
f=open(fn)
sid_te = f.readlines()
f.close()
for idx,val in enumerate(sid_te):
    uid = int(uid_te[idx][:-1])
    sid = int(sid_te[idx][:-1])
    pred = w0 + all_w['uid'][uid] + all_w['sid'][sid] + np.dot(all_v['uid'][uid],all_v['sid'][sid])
    print pred

