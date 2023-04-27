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
lruipc_exc = [0.165732,0.146795,0.124941,0.107989]
lfuipc_exc = [0.165729,0.146786,0.125114,0.109146]
fifoipc_exc = [0.165732,0.146795,0.12494,0.108065]
randomipc_exc = [0.168052,0.150193,0.129062,0.109026]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access frequency for different sizes of LLC
lruDAF_exc = [10.39,10.37,9.97,8.4]
lfuDAF_exc = [10.39,10.38,9.95,8.31]
fifoDAF_exc = [10.39,10.37,9.97,8.4]
randomDAF_exc = [10.27,10.19,9.68,8.32]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,1)
bar1 = plt.bar(ind, lfuipc_exc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_exc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_exc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_exc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.1, 0.17)
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
plt.ylim(8, 11)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Exclusive cache hierarchy", fontsize=10)

# inclusive data
#data--ipc  for each replacement policy we need data for different sizes
lruipc_inc = [0.187939 ,0.16477,0.13067,0.103892]
lfuipc_inc = [0.189319,0.165432,0.131008,0.104888]
fifoipc_inc = [0.187939,0.16477,0.13067,0.103892]
randomipc_inc = [0.183148,0.166462,0.1398990,0.113551]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access frequency for different sizes of LLC
lruDAF_inc = [5.2,5.14,5.11,3.8]
lfuDAF_inc = [5.15,5.11,5.1,3.72]
fifoDAF_inc = [5.2,5.14,5.11,3.82]
randomDAF_inc = [5.32,8.67,7.66,5.34]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,2)
bar1 = plt.bar(ind, lfuipc_inc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_inc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_inc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_inc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.10, 0.19)
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
lruipc_ninc = [0.197463 ,0.171509,0.134779,0.106459]
lfuipc_ninc = [0.198685,0.172139,0.135101,0.10749]
fifoipc_ninc = [0.197463,0.171509,0.134779,0.106459]
randomipc_ninc = [0.194257,0.172604,0.14774,0.117826]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access percentage for different sizes of LLC
lruDAF_ninc = [5.06,5.02,5.00,3.74]
lfuDAF_ninc = [5.02,5.00,4.96,3.64]
fifoDAF_ninc = [5.06,5.02,5.00,3.74]
randomDAF_ninc = [5.55,5.06,4.12,2.92]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,3)
bar1 = plt.bar(ind, lfuipc_ninc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_ninc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_ninc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_ninc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.10, 0.20)
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
plt.ylim(2.5, 6)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Non-Inclusive cache hierarchy", fontsize=10)

plt.suptitle("Plot for trace bfs",fontsize=20, fontweight='bold')
plt.show()