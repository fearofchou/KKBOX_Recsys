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

inter_user = open('/home/fearofchou/KKBOX_Recsys/data/internal_member/users.meta')
uid = inter_user.readlines()

inter_uid = []
for i in uid:
    i=i.split()
    muid = uid_mask[int(i[0])]
    inter_uid.append(muid)


print 'Write'
f = open('/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/interl.pred','w')


for uid in inter_uid:
    for sid in xrange(len(sid_mask.keys())):

        f.write('%d %d 0\n'%(uid,sid+1))

f.close()
