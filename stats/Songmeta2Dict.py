fn = '/home/fearofchou/KKBOX_Recsys/data/song_meta'
f = open(fn)
song_info = f.readlines()

song_meta = {}
for idx,i in enumerate(song_info):
    sm = i.split('\t')
    try:
        sid = int(sm[0])
    except:
        break
    song_meta[sid] = {}
    song_meta[sid]['1_track'] = sm[1]
    song_meta[sid]['2_album'] = sm[2]
    song_meta[sid]['3_artist'] = sm[3]
    song_meta[sid]['4_release date'] = sm[4]
    song_meta[sid]['5_genre'] = sm[5][:-1]


import pickle
ofn = '/home/fearofchou/KKBOX/data/song_meta.dict'
with open(ofn,'w') as f:
    pickle.dump(song_meta,f)

