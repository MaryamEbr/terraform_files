from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time

latency_list = []

file = open('results_after/nohup_destination_4.txt')
for line in file:
    if (line[:7] == "latency"):
        line = line[16:-3]
        line = line.replace('\'', '').replace('(', '').split('),')
        latency_list.append([a.replace(' ', '').split(',') for a in line])
        
        

end_to_end_list = []
source_to_tier1_list = []
tier1_comp_list = []
tier1_to_tier2_list = []
tier2_comp_list = []
tier2_to_tier3_list = []
tier3_comp_list = []
tier3_to_tier4_list = []
tier4_comp_list = []
tier4_to_destination_list = []

for i,item in enumerate(latency_list[0]):
    print(i , " -> ", item)

for row in latency_list:
    end_to_end_list.append((float(row[-1][2]) - float(row[0][2]))*1000)
    source_to_tier1_list.append((float(row[1][2]) - float(row[0][2]))*1000)
    tier1_comp_list.append((float(row[2][2]) - float(row[1][2]))*1000)
    tier1_to_tier2_list.append((float(row[3][2]) - float(row[2][2]))*1000)
    tier2_comp_list.append((float(row[4][2]) - float(row[3][2]))*1000)
    tier2_to_tier3_list.append((float(row[5][2]) - float(row[4][2]))*1000)
    tier3_comp_list.append((float(row[6][2]) - float(row[5][2]))*1000)
    tier3_to_tier4_list.append((float(row[7][2]) - float(row[6][2]))*1000)
    tier4_comp_list.append((float(row[8][2]) - float(row[7][2]))*1000)
    tier4_to_destination_list.append((float(row[9][2]) - float(row[8][2]))*1000)

begin = 100
end = len(end_to_end_list)

plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('end-to-end latency (ms)')
plt.plot(end_to_end_list[begin:end], label="end_to_end", color='red')
plt.legend()
plt.savefig('pics/end-to-end.pdf', format='pdf')

plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('source_to_tier1 latency (ms)')
plt.plot(source_to_tier1_list[begin:end], label="source_to_tier1", color='orange')
plt.legend()
plt.savefig('pics/source_to_tier1.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier1_comp latency (ms)')
plt.plot(tier1_comp_list[begin:end], label="tier1_comp", color='blue')
plt.legend()
plt.savefig('pics/tier1_comp.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier1_to_tier2 latency (ms)')
plt.plot(tier1_to_tier2_list[begin:end], label="tier1_to_tier2", color='green')
plt.legend()
plt.savefig('pics/tier1_to_tier2.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier2_comp latency (ms)')
plt.plot(tier2_comp_list[begin:end], label="tier2_comp", color='grey')
plt.legend()
plt.savefig('pics/tier2_comp.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier2_to_tier3 latency (ms)')
plt.plot(tier2_to_tier3_list[begin:end], label="tier2_to_tier3", color='black')
plt.legend()
plt.savefig('pics/tier2_to_tier3.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier3_comp latency (ms)')
plt.plot(tier3_comp_list[begin:end], label="tier3_comp", color='pink')
plt.legend()
plt.savefig('pics/tier3_comp.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier3_to_tier4 latency (ms)')
plt.plot(tier3_to_tier4_list[begin:end], label="tier3_to_tier4", color='brown')
plt.legend()
plt.savefig('pics/tier3_to_tier4.pdf', format='pdf')


plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier4_comp latency (ms)')
plt.plot(tier4_comp_list[begin:end], label="tier4_comp", color='crimson')
plt.legend()
plt.savefig('pics/tier4_comp.pdf', format='pdf')

plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('tier4_to_destination latency (ms)')
plt.plot(tier4_to_destination_list[begin:end], label="tier4_to_destination", color='yellow')
plt.legend()
plt.savefig('pics/tier4_to_destination.pdf', format='pdf')












plt.figure()
plt.grid()
plt.xlim([begin, end])
plt.xlabel('time')
plt.ylabel('latency (ms)')
plt.plot(end_to_end_list[begin:end], label="end_to_end", color='red', linewidth=2)
plt.plot(source_to_tier1_list[begin:end], label="source_to_tier1", color='orange')
plt.plot(tier1_comp_list[begin:end], label="tier1_comp", color='blue')
plt.plot(tier1_to_tier2_list[begin:end], label="tier1_to_tier2", color='green')
plt.plot(tier2_comp_list[begin:end], label="tier2_comp", color='grey')
plt.plot(tier2_to_tier3_list[begin:end], label="tier2_to_tier3", color='black')
plt.plot(tier3_comp_list[begin:end], label="tier3_comp", color='pink')
plt.plot(tier3_to_tier4_list[begin:end], label="tier3_to_tier4", color='brown')
plt.plot(tier4_comp_list[begin:end], label="tier4_comp", color='crimson')
plt.plot(tier4_to_destination_list[begin:end], label="tier4_to_destination", color='yellow')
plt.legend(loc='best', bbox_to_anchor=(1.01, 1))
plt.subplots_adjust(right=0.8)
# plt.tight_layout()
plt.savefig('pics/all.pdf', format='pdf',  bbox_inches="tight")
plt.show()

