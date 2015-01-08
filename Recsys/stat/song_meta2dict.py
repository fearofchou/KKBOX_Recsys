
def song_meta2dict():
    song_meta_fn = '/home/fearofchou/KKBOX_Recsys/data/song_meta'

    song_meta = {}

    with open(song_meta_fn) as f:
        song_info = f.readlines()

    for i in song_info:
        i = i.split('\t')
        try:
            r_sid =  int(i[0])
        except:
            continue
        song_meta[r_sid] = {}
        song_meta[r_sid]['title'] =  i[1]
        song_meta[r_sid]['artist'] =  i[3]
        song_meta[r_sid]['genre'] =  i[5]
        song_meta[r_sid]['release date'] =  i[4]
    return song_meta

