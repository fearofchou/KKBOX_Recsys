import glob

glob.glob()

pred_fn = '/home/fearofchou/TEST_MF/data/'


f = open(pred_fn+'')
pred = f.readlines()

Top_N = {}

for i in pred:
    i=i.split()
    uid = int(i[0])
    sid = int(i[1])
    pre = float(i[2])

    try:
        Top_N[uid][sid] = pre
    except:
        Top_N[uid] = {}
        Top_N[uid][sid] = pre

