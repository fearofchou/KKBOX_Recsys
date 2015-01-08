fn = '/home/fearofchou/KKBOX_transition/gen_data/II_rank_TF_2014'
f = open(fn)
uir = f.readlines()

fn = '/home/fearofchou/KKBOX_transition/gen_data/sid_mask'
import pickle
with open(fn) as f:
    sid_mask = pickle.load(f)

import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from song_meta2dict import *

song_meta = song_meta2dict()

IIR = {}
for i in uir:
    log = i.split(' ')
    ssid = int(log[0])
    esid = int(log[1])
    tar = float(log[2])
    try:
        IIR[ssid][esid] = tar
    except:
        IIR[ssid] = {}
        IIR[ssid][esid] = tar

fn = '/home/fearofchou/KKBOX_transition/gen_data/sid.meta'
f = open(fn,'w')
for i in sid_mask.keys():
    try:
        ar = song_meta[i]['artist']
    except:
        continue
    ti = song_meta[i]['title']
    ge = song_meta[i]['genre']

    f.write('%d %s %s %s'%(i,ti,ar,ge))

f.close()

ex = []
sk = sorted(sid_mask.keys())
import numpy as np
while 1:
    sid = raw_input('song id:')
    try:
        msid = sid_mask[int(sid)]
    except:
        continue
    item = np.array(IIR[msid].items())
    idx = np.argsort(item[:,1])[::-1]

    ssid = item[idx,0]
    tar = item[idx,1]

    print 'Start sid=%s Num inter=%d=========================='%(sid,len(ssid))
    for idx,val in enumerate(ssid):
        if idx%10==0:
            ex = raw_input('Contiune-->')
        if ex == 'ex':
            break
        val = int(val)
        val = sk[val-1]
        ar = song_meta[val]['artist']
        ti = song_meta[val]['title']
        ge = song_meta[val]['genre']

        print '%d %f %s %s %s'%(val,tar[idx],ti,ar,ge[:-1])

