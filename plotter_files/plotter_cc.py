import numpy as np
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#plotting, we generate two different plots for ipc and LLC miss rate
N = 4
ind = np.arange(N) 
width = 0.2

# exclusive data
#data--ipc  for each replacement policy we need data for different sizes
lruipc_exc = [0.213043,0.216662,0.196307,0.147686]
lfuipc_exc = [0.212148,0.213837,0.194985,0.148017]
fifoipc_exc = [0.213061,0.216607,0.196493,0.148021]
randomipc_exc = [0.182814,0.200055,0.193361,0.147986]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access frequency for different sizes of LLC
lruDAF_exc = [18.9,16.9,15.4,14.6]
lfuDAF_exc = [19,17,15.5,14.6]
fifoDAF_exc = [18.9,17,15.4,14.6]
randomDAF_exc = [21.67,18,15.5,14.6]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,1)
bar1 = plt.bar(ind, lfuipc_exc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_exc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_exc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_exc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.14, 0.22)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("IPC comparison for Exclusive cache hierarchy", fontsize=10)

plt.subplot(2,3,4)
bar1 = plt.bar(ind, lfuDAF_exc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoDAF_exc, width, color='g')
bar3 = plt.bar(ind+width*2, lruDAF_exc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomDAF_exc, width, color = 'c')
# bar8 = plt.bar(ind+width*3, lruLLCmissrate, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("DRAM Access(%)")
plt.ylim(10, 25)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Exclusive cache hierarchy", fontsize=10)

# inclusive data
#data--ipc  for each replacement policy we need data for different sizes
lruipc_inc = [0.21481,0.245565,0.229507,0.156771]
lfuipc_inc = [0.223956,0.266004,0.234161,0.156823]
fifoipc_inc = [0.21481,0.245565,0.229507,0.156771]
randomipc_inc = [0.201515,0.210046,0.198967,0.153066 ]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access frequency for different sizes of LLC
lruDAF_inc = [6.2,2.5,1.39,1.3]
lfuDAF_inc = [5.47,2,1.32,1.3]
fifoDAF_inc = [6.3,2.5,1.4,1.3]
randomDAF_inc = [11.94,6.4,3.8,2.24]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,2)
bar1 = plt.bar(ind, lfuipc_inc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_inc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_inc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_inc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.15, 0.27)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("IPC comparison for Inclusive cache hierarchy", fontsize=10)

plt.subplot(2,3,5)
bar1 = plt.bar(ind, lfuDAF_inc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoDAF_inc, width, color='g')
bar3 = plt.bar(ind+width*2, lruDAF_inc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomDAF_inc, width, color = 'c')
# bar8 = plt.bar(ind+width*3, lruLLCmissrate, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("DRAM Access(%)")
plt.ylim(0, 15)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Inclusive cache hierarchy", fontsize=10)

# non-inclusive data
#data--ipc  for each replacement policy we need data for different sizes
lruipc_ninc = [0.222292,0.255146,0.238013 ,   0.160795]
lfuipc_ninc = [0.232012,0.277305,0.243034   ,0.16085]
fifoipc_ninc = [0.222292,0.255146,0.238013  ,   0.160795]
randomipc_ninc = [0.207973,0.21802,0.203531 , 0.15541 ]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access percentage for different sizes of LLC
lruDAF_ninc = [5.76,2.33,1.28  , 1.20  ]
lfuDAF_ninc = [5.04,1.84,2.16  , 1.19  ]
fifoDAF_ninc = [5.76,2.33,1.28 ,1.20   ]
randomDAF_ninc = [7.15,4.00, 2.16 , 1.37]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,3)
bar1 = plt.bar(ind, lfuipc_ninc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_ninc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_ninc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_ninc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.15, 0.30)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("IPC comparison for Non-Inclusive cache hierarchy", fontsize=10)

plt.subplot(2,3,6)
bar1 = plt.bar(ind, lfuDAF_ninc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoDAF_ninc, width, color='g')
bar3 = plt.bar(ind+width*2, lruDAF_ninc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomDAF_ninc, width, color = 'c')
# bar8 = plt.bar(ind+width*3, lruLLCmissrate, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("DRAM Access(%)")
plt.ylim(0,8)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Non-Inclusive cache hierarchy", fontsize=10)

plt.suptitle("Plot for trace cc",fontsize=20, fontweight='bold')
plt.show()