# cs230_Project
### Shikhar Parmar   210050145 
### Shriyank Tatawat 210050147
### Vaibhav Vishal   210050159

Original Champsim folder contains workable files for Non-Inclusive hierarchy.
It also contains the 4 replacement policies fifo, lfu, lru & random in replacement subfolder.


#### plot folder 
Contains graphs showing comparison between different traces.
For each trace we've plotted 6 graphs, collectively showing differences using the paramneters IPC and DRAM Access(%) between Inclusive, Non Inclusive and Exclusive hierarchy combined with different replacement policies like fifo, lfu, lru & random. Along the X-axis, plotted against the different cache sizes mainly (MB) 8, 16, 32 & 64.

#### Running Instruction
##### Non Inclusive

./build_champsim.sh bimodal no no no no "replacement Policy" 1  <br>
./run_champsim.sh bimodal-no-no-no-no-"replacement Policy"-1core 30 30 <Trace Name>.trace.gz <br>

for eg: Running for the trace bfs for the lru replacement policy.<br>
./build_champsim.sh bimodal no no no no lru 1 <br>
./run_champsim.sh bimodal-no-no-no-no-lru-1core 30 30 bfs-14.trace.gz <br>


