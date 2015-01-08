import sys
sys.path.append('/home/fearofchou/KKBOX_Recsys/code/stat/')
from per_user_lis_log import *
from song_meta2dict import *

song_meta = song_meta2dict()
import numpy as np
UIR = {} #user item rating matrix
inter_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/internal_member/2014'
KKBOX_user_log_fn = '/home/fearofchou/KKBOX_Recsys/data/play_count_log_2014'

UIR,_,_,_ = user_log2dict(UIR,inter_user_log_fn)
UIR,count,uid_mask,sid_mask = user_log2dict(UIR,KKBOX_user_log_fn)
'''
pop_pl_sid = {}
pop_li_sid = {}
for i in UIR.keys():
    for j in UIR[i]:
        try:
            pop_li_sid[j] += 1
        except:
            pop_li_sid[j] = 1
        try:
            pop_pl_sid[j] += UIR[i][j]
        except:
            pop_pl_sid[j] = UIR[i][j]
'''

print 'Write'
fp = '/home/fearofchou/KKBOX_Recsys/gen_data/'
#f = open('/LOG_2014','w')
f = open(fp+'ZS_2014','w')

from scipy import stats
for uid in UIR.keys():
    item = np.array(UIR[uid].items())
    idx = np.argsort(item[:,1])[::-1]

    tar = item[:,1][idx]
    tar = stats.zscore(tar)
    if np.isnan(tar[0]):
        continue
    ssid = item[:,0][idx]



    for i,sid in enumerate(ssid):
        muid = uid_mask[uid]
        msid = sid_mask[sid]

        f.write('%d %d %f\n'%(muid,msid,tar[i]))
    '''
    for sid in bot_song:
        muid = uid_mask[uid]
        msid = sid_mask[sid]

        tar = UIR[uid][sid]
        tar = 0
        f.write('%d %d %f\n'%(muid,msid,tar))
    '''
f.close()

