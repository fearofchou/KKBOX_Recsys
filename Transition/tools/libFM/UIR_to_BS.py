import numpy as np
import pickle,sys
import Convert_Transpose
fp = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/'

#input user-item  rating matrix
def Gen_UI_BS(fn):

    user_dict = {}
    song_dict = {}

    print 'load UIR file'
    f = open(fn)
    ra = f.readlines()

    fu = open(fp+'uid.train','w')
    fs = open(fp+'sid.train','w')
    ft = open(fp+'tar.train','w')

    print 'Write BS train and test'
    for i in ra:
        UIR=i.split()
        uid = UIR[0]
        sid = UIR[1]
        tar = UIR[2]
        user_dict[uid] = 1
        song_dict[sid] = 1

        fu.write(uid+'\n')
        fs.write(sid+'\n')
        ft.write(tar+'\n')

    fu.close()
    fs.close()
    ft.close()

    fu = open(fp+'uid.test','w')
    fs = open(fp+'sid.test','w')
    ft = open(fp+'tar.test','w')
    fu.write('1\n')
    fs.write('1\n')
    ft.write('1\n')
    fu.close()
    fs.close()
    ft.close()

    rel_uid_file = fp + 'uid'
    rel_sid_file = fp + 'sid'

    print 'Write BS feature'
    f = open(rel_uid_file,'w')
    for i in user_dict.keys():
        f.write('0 ' + str(i)  + ':1\n' )
    f.close()

    f = open(rel_sid_file,'w')
    for i in song_dict.keys():
        f.write('0 ' + str(i)  + ':1\n' )
    f.close()

fn = '/home/fearofchou/KKBOX_transition/gen_data/II_rank_2014'
Gen_UI_BS(fn)
Convert_Transpose.CT(fp+'uid')
Convert_Transpose.CT(fp+'sid')
