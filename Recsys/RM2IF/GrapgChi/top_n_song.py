'''
import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from per_user_lis_log import *
from song_meta2dict import *

song_meta = song_meta2dict()
import numpy as np
train_user_item_rating = {}
inter_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/internal_member/2014'
KKBOX_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/play_count_log_2014'

train_user_item_rating,count,uid_mask,sid_mask = user_log2dict(train_user_item_rating,inter_user_log_fn)
train_user_item_rating,count,uid_mask,sid_mask = user_log2dict(train_user_item_rating,KKBOX_user_log_fn)
'''
import numpy as np
rsid_mask ={}
for i in sid_mask.keys():
    rsid_mask[sid_mask[i]] =i


inter_user = open('/home/fearofchou/KKBOX_Recsys/data/internal_member/users.meta')
uid = inter_user.readlines()

inter_uid = []
for i in uid:
    i=i.split()
    inter_uid.append(int(i[0]))

Top_N = {}
Top_N_val = {}
for idx,iuid in enumerate(inter_uid):
    muid = uid_mask[iuid]-1
    IUM = UM[muid]
    Top_N[iuid] = []
    for i in xrange(len(VM)):
       Top_N[iuid].append( np.dot(IUM, VM[i]) )

    Top_N_val[iuid] = Top_N[iuid]
    Top_N[iuid] = np.argsort(Top_N[iuid])[::-1]

er = []
N = 20
fp = '/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/Top_N_song/'
for i in Top_N.keys():
    print i
    f = open(fp + '%d'%(i),'w')
    for j in Top_N[i][:N]:
        val = rsid_mask[j+1]
        tar = Top_N_val[i][j]
        try:
            ge = song_meta[val]['genre']
            rd = song_meta[val]['release date']
            at = song_meta[val]['artist']
            ti = song_meta[val]['title']

            f.write('%d %s %s %s %s'%(tar,ti,at,rd,ge))
        except:
            er.append(val)
            f.write('%d\n'%(val))

    f.close()
