f=open('/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/test_bin_MODEL_sgd.1_of_1')
a=f.readlines()

re = {}
for i in a:
    i=i.split('\t')
    uid = int(i[0])
    sid = int(i[1])
    tar = float(i[2][:-1])

    try:
        re[uid][sid]=tar
    except:
        re[uid] = {}
        re[uid][sid]=tar

for i in sorted(re.keys()):
    for j in sorted(re[i]):
        print '%.2f '%re[i][j],
    print '\n'


