
sid_key = IIR.keys()

print 'Compute popularity'
pop_sid = {}
for i in IIR.keys():
    pop_sid[i] = len(IIR[i])

import numpy as np

while 1:
    ex= []
    qword = raw_input('Input search string or sid:')

    if qword.isdigit():
        count = 1
        i = int(qword)
        item = np.array(IIR[i].items())
        idx = np.argsort(item[:,1])[::-1]

        for s_id in idx:
            count+=1
            if count%10 == 0:
                ex = raw_input('Please enter a key to continue:')
                count+=1
            try:
                if 'exit' in ex:
                    break
            except:
                pass

            i = item[s_id,0]
            co = item[s_id,1]
            try:
                art = song_meta[i]['artist']
            except:
                print '%d == %d'%(i,co)
                continue
            tit = song_meta[i]['title']
            gen = song_meta[i]['genre']
            rel = song_meta[i]['release date']
            print '%d == %d %s - %s|%s|%s'%(i,co,tit,art,rel,gen),




    else:
        have_sid_pop = []
        for i in sid_key:
            try:
                art = song_meta[i]['artist']
            except:
                continue
            tit = song_meta[i]['title']
            gen = song_meta[i]['genre']
            rel = song_meta[i]['release date']
            if qword in art or qword in tit:
                have_sid_pop.append([i,pop_sid[i]])

        item = np.array(have_sid_pop)
        idx = np.argsort(item[:,1])[::-1]

        for s_id in idx:
            i = item[s_id,0]
            co = item[s_id,1]
            try:
                art = song_meta[i]['artist']
            except:
                print '%d == %d'%(i,co)
                continue
            tit = song_meta[i]['title']
            gen = song_meta[i]['genre']
            rel = song_meta[i]['release date']
            print '%d == %d %s - %s|%s|%s'%(i,co,tit,art,rel,gen),


