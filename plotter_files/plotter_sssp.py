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
lruipc_exc = [0.279755,0.268999,0.239376,0.183965]
lfuipc_exc = [0.279087,0.267856,0.238519,0.184327]
fifoipc_exc = [0.279749,0.269058,0.239303,0.184257]
randomipc_exc = [0.257187,0.25225,0.234533,0.183946 ]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access frequency for different sizes of LLC
lruDAF_exc = [17.96,16.41,14.84,13.79]
lfuDAF_exc = [18,16.48,14.87,13.77]
fifoDAF_exc = [17.96,16.41,14.84,13.77]
randomDAF_exc = [19.69,17.49,15.04,13.79]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,1)
bar1 = plt.bar(ind, lfuipc_exc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_exc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_exc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_exc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.18, 0.29)
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
plt.ylim(10, 20)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Exclusive cache hierarchy", fontsize=10)

# inclusive data
#data--ipc  for each replacement policy we need data for different sizes
lruipc_inc = [0.284242,0.29648,0.281197,0.203212]
lfuipc_inc = [0.292354,0.317753,0.294732,0.205256]
fifoipc_inc = [0.284242,0.29648,0.281197,0.203212]
randomipc_inc = [0.267596, 0.266592,0.24015, 0.189825]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access frequency for different sizes of LLC
lruDAF_inc = [6.7,3.7,2.3,1.9]
lfuDAF_inc = [6.09,3.1,2.1,1.8]
fifoDAF_inc = [6.7,3.7,2.3,1.9]
randomDAF_inc = [8.4,5.4,5.09,2.34]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,2)
bar1 = plt.bar(ind, lfuipc_inc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_inc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_inc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_inc, width, color = 'c')
# bar4 = plt.bar(ind+width*3, lruipc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.18, 0.32)
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
plt.ylim(0, 10)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Inclusive cache hierarchy", fontsize=10)

# non-inclusive data
#data--ipc  for each replacement policy we need data for different sizes
lruipc_ninc = [ 0.294612,0.307853,0.2917177,0.209084]
lfuipc_ninc = [0.303351,0.330853,0.306223,0.211228]
fifoipc_ninc = [0.294612,0.307853,0.291717,0.209084]
randomipc_ninc = [0.289817, 0.278915,0.254101, 0.199201]
# randomipc = [plotdata[0][3][0], plotdata[1][3][0], plotdata[3][3][0], plotdata[2][3][0]]

#data--LLC dram access percentage for different sizes of LLC
lruDAF_ninc = [6.33,3.52,2.19,2.07]
lfuDAF_ninc = [5.70,3,2 , 1.76]
fifoDAF_ninc = [6.33,3.52,2.19,2.07]
randomDAF_ninc = [8.52,5.53, 3.27 , 2.07]
# random = [plotdata[0][3][1], plotdata[1][3][1], plotdata[3][3][1], plotdata[2][3][1]]

plt.subplot(2,3,3)
bar1 = plt.bar(ind, lfuipc_ninc, width, color = 'r')
bar2 = plt.bar(ind+width, fifoipc_ninc, width, color='g')
bar3 = plt.bar(ind+width*2, lruipc_ninc, width, color = 'b')
bar4 = plt.bar(ind+width*3, randomipc_ninc, width, color = 'c')
plt.xlabel("Size of LLC (MB)")
plt.ylabel("IPC")
plt.ylim(0.19, 0.35)
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
plt.ylim(0, 10)
plt.xticks(ind+width,['8', '16', '32', '64'])
plt.legend( (bar1, bar2, bar3, bar4), ('LFU', 'FIFO', 'LRU', 'random') )
plt.title("DRAM Access comparison for Non-Inclusive cache hierarchy", fontsize=10)

plt.suptitle("Plot for trace sssp",fontsize=20, fontweight='bold')
plt.show()