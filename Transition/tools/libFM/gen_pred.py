import pickle
fn = '/home/fearofchou/KKBOX_transition/gen_data/sid_mask'
with open(fn) as f:
    sid_mask = pickle.load(f)

sk = sorted(sid_mask.keys())

fp = '/home/fearofchou/KKBOX_transition/gen_data/libFM/exe/'
uid  = [10883526,27818274,1700795,1562494,15370242,19528752,21802114]

tar_f = open(fp+'tar.test','w')
uid_f = open(fp+'uid.test','w')
sid_f = open(fp+'sid.test','w')

for i in uid:
    i = sid_mask[i]
    for j in range(len(sid_mask)):
        uid_f.write('%d\n'%(i))
        sid_f.write('%d\n'%(j+1))
        tar_f.write('1\n')

uid_f.close()
sid_f.close()
tar_f.close()


