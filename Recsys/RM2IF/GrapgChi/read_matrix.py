
U_fn = open('/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/LOG_2014_MODEL_sgd.U.1_of_1')
U_mm = U_fn.readlines()
um_size = len(U_mm)

vector_size = len(U_mm[0].split(' '))-2

import numpy as np

UM = np.zeros([um_size,vector_size])

for i in U_mm:
    i=i.split(' ')
    idx = int(i[0][:-1])-1
    for j in range(vector_size):
        midx = j+1
        UM[idx,j] = float(i[midx])

V_fn = open('/home/fearofchou/KKBOX_Recsys/gen_data/grapgchi/LOG_2014_MODEL_sgd.V.1_of_1')
V_mm = V_fn.readlines()
vm_size = len(V_mm)

VM = np.zeros([vm_size,vector_size])

for i in V_mm:
    i=i.split(' ')
    idx = int(i[0][:-1])-1
    for j in range(vector_size):
        vidx = j+1
        VM[idx,j] = float(i[vidx])

