fp = '/home/fearofchou/KKBOX_Recsys/data/song_meta'

f = open(fp)
song_meta = f.readlines()

qword = raw_input("Search query (word in song meta):")

import re
while 1:
    con = 1
    for i in song_meta:
        if qword in i:
            print i
            con+=1
        if con%10==0:
            a = raw_input("Press Enter to continue")
            con+=1



