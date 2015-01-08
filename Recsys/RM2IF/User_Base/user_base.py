
chou = 63810209
uid_sid = np.array(UIR[chou].items())
idx = np.argsort(uid_sid[:,1])[::-1]
uid_sid = uid_sid[:,0][idx[:1]]
uid_group = []
for idx,uid in enumerate(UIR.keys()):
    if uid == chou:
        continue
    for sid in UIR[uid]:
        if sid in uid_sid:
            uid_group.append(uid)
            break


user_base = {}

for i in uid_group:
    uid_sid = np.array(UIR[i].items())
    idx = np.argsort(uid_sid[:,1])[::-1]
    uid_sid = uid_sid[:,0][idx[:100]]
    for j in uid_sid:
        try:
            user_base[j] += 1
        except:
            user_base[j] = 1

re = np.array(user_base.items())
idx = np.argsort(re[:,1])[::-1]
re = re[:,0][idx]

for i in re[:100]:

    print song_meta[i]['title'] +' - ' + song_meta[i]['artist']
