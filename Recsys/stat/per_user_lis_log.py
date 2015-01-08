
def user_log2dict(inte_mem_ulog,log_fn):

    with open(log_fn) as f:
        log = f.readlines()

    for i in log:
        i =  i.split('\t')
        uid = int(i[0])
        sid = int(i[1])
        tar = int(i[2])
        try:
            inte_mem_ulog[uid][sid] = tar
        except:
            inte_mem_ulog[uid] = {}
            inte_mem_ulog[uid][sid] = tar

    uid_dict ={}
    sid_dict ={}
    log_count = 0
    for i in inte_mem_ulog.keys():
        uid_dict[i]=1
        for j in inte_mem_ulog[i]:
            sid_dict[j]=1
            log_count += 1

    uid_count = len(uid_dict.keys())
    sid_count = len(sid_dict.keys())
    count = {}
    count['log'] = log_count
    count['uid'] = uid_count
    count['sid'] = sid_count

    uid_mask = {}
    sid_mask = {}
    for idx,val in enumerate(sorted(uid_dict.keys())):
        uid_mask[val] = idx+1
    for idx,val in enumerate(sorted(sid_dict.keys())):
        sid_mask[val] = idx+1

    return inte_mem_ulog,count,uid_mask,sid_mask


