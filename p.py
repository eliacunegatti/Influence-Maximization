from cmath import log10
from pickle import TRUE
import pandas as pd
import networkx as nx
from sklearn.cluster import MeanShift
from src.load import read_graph
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import collections
warnings.filterwarnings("ignore")
from math import log, log10
import math
name = 'ffb-pages-public-figure'

filenames = ["scale_graphs/fb-pages-public-figure_8.txt","scale_graphs/fb-pages-public-figure_4.txt","scale_graphs/fb-pages-public-figure_2.txt","graphs/fb-pages-public-figure.txt"]
#filenames = ["scale_graphs/facebook_combined_prova8.txt","scale_graphs/facebook_combined_8.txt","graphs/facebook_combined.txt"]
kk = []


for item in filenames:
    G = read_graph(item)
    print(nx.info(G))
    den = (2*G.number_of_edges()) / (G.number_of_nodes()*(G.number_of_nodes()-1))
    print("Density --> {0}".format(den))
    my_degree_function = G.degree
    mean = []
    mean_degree = []
    for item in G:
        mean.append(my_degree_function[item])
    kk.append(mean)

for item in kk:
    print(np.mean(item))


x = ['Original', '2', '4', '8']
x = x[::-1]
print(x)

real = np.mean(kk[0])
color = ["green", 'blue','orange','red']
# plt.figure(figsize=(6, 6)) 
# i = 0
# for item in filenames:
#     G = read_graph(item)   
#     degree_freq = nx.degree_histogram(G)
#     degrees = range(len(degree_freq))
#     plt.loglog(degrees, degree_freq,'go-', color=color[i], label = str(x[i]))
#     i +=1
# plt.xlabel('Degree')
# plt.ylabel('Frequency')
# plt.legend()
# plt.savefig('degree_log.png')

# #plt.show()
# plt.cla()
# plt.close()


i=0
filenames = filenames[::-1]
x = x[::-1]
color = color[::-1]
i = 0
fig, axs = plt.subplots(4, sharex=True,figsize=(8, 8)) 
#fig.suptitle('Degree Distribution')

i = 0
for item in filenames:
    G = read_graph(item)
    degree_sequence = sorted([(d) for n, d in G.degree()], reverse=True)  # degree sequence
    degree_sequence_1 = sorted([log10(d) for n, d in G.degree()], reverse=True)  # degree sequence

    # print "Degree sequence", degree_sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    #axs[len(filenames)-1-i].set_yscale('log')
    #axs[len(filenames)-1-i].set_xscale('log')

    #axs[len(filenames)-1-i].hist(list(dict(nx.degree(G)).values()))
    #i +=1
    #plt.xscale('log')
    #n, bins, patches = axs[len(filenames)-1-i].hist(degree_sequence, 20, facecolor=color[i], alpha=0.75, log=True)
    axs[len(filenames)-1-i].hist(degree_sequence, bins=int(max(degree_sequence)), facecolor=color[i], alpha=0.75, edgecolor='black', linewidth=0.5,log=True)
    #axs[len(filenames)-1-i].loglog(deg, cnt, basex=10, basey=10, 
    #       markeredgecolor='red')
    # if i == 0:
    #     t = []
    #     k = 0
    #     tt = []
    #     print(max(degree_sequence))
    #     while k < max(degree_sequence):
    #         t.append(k)
    #         tt.append(int(10 ** k))
    #         print(k, 10 ** k)
    #         k += 0.5
        
    #     plt.xticks(t,tt)
    # add a 'best fit' line
    #axs[len(filenames)-1-i].plot(bins, color=color[i])
    i += 1

#plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
#plt.savefig('aaaa')
plt.show()
#plt.show()
# i = 0
# for item in filenames:
#     G = read_graph(item)
#     degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
#     #degree_sequence = [log(x) for x in degree_sequence]
    
#     degreeCount = collections.Counter(degree_sequence)
#     deg, cnt = zip(*degreeCount.items())
#     #num_bins = len(degree_sequence)
#     #deg = [float(log10(x)) for x in deg]  

#     d = pd.DataFrame()
#     d["count"] = cnt
#     d["degree"] = deg

#     deg = [log10(x) for x in deg]


#     if i == 0:
#         max_t = (max(deg))
    
#     #sns.histplot(data=d, x='degree', kde=True, bins=10,
#     #sns.barplot(data=d, x='degree', y='count',ax = axs[len(filenames)-1-i],color=color[i])
    
#     #plt.show()
#     #n,bins, patches = axs[len(filenames)-1-i].hist(degree_sequence, 100, density=True)
#     #y = ((1 / (np.sqrt(2 * np.pi) * np.std(degree_sequence))) *np.exp(-0.5 * (1 / np.std(degree_sequence) * (bins - np.mean(degree_sequence))**2)))
#     #axs[len(filenames)-1-i].set_xscale('log')
#     #axs[len(filenames)-1-i].bar(deg, cnt)#, drawstyle='steps-mid')
#     sns.histplot(x=deg, bins=int(1 + 3.322 * log(len(deg))),kde=True, ax = axs[len(filenames)-1-i],log_scale=False,color=color[i])
#     t = [0,0.5,1,1.5,2,2.5,3]
#     tt = []
#     for item in t:
#         tt.append(int(10 ** item))
# # add a 'best fit' line
#     #axs[len(filenames)-1-i].plot(bins, y, '--')
#     plt.xticks(t,tt)
#     axs[len(filenames)-1-i].set_xlim(0, max_t)
#     i +=1
# #plt.legend()
# plt.show()

# plt.xlabel('log(degree)')
# plt.ylabel('count')
# plt.tight_layout()
# plt.savefig(name + '_hist')

# from collections import Counter

plt.figure(figsize=(6, 6)) 
i = 0
for item in filenames:
    G = read_graph(item)
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    
    
    degreeCount = collections.Counter(degree_sequence)
    #print(degreeCount)
    x1, y = zip(*degreeCount.items())                                                                                                                      

    plt.xscale('log')  
    plt.yscale('log')                                                                                                        
                                                                                                      
    plt.scatter(x1, y, marker='.',  s=100,color=color[i], label = str(x[i]))    
    #axs[len(filenames)-1-i].bar(x1, y,color=color[i], label = str(x[i]))     

    # if i == 0:
    #     t = []
    #     k = 0
    #     tt = []
    #     print(max(degree_sequence))
    #     while k < max(degree_sequence):
    #         t.append(log10(k))
    #         tt.append(k)
    #         print(k)
        
    #     plt.xticks(t,tt)    
    #plt.xlim(1, max(x1))  
    #locs, labels = plt.xticks()
    #plt.get_major_formatter().labelOnlyBase = False
    #print(labels)

    #plt.xticks()
    i = i+1
plt.xlabel('Degree')
plt.ylabel('Frequency')  
plt.legend()
#plt.savefig(name + '_scatter')
plt.show()
plt.close()
plt.cla()

exit(0)

plt.figure(figsize=(6, 6)) 
i = 0
for item in filenames:
    # Subset to the airline
    G = read_graph(item)
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True) 
    print(max(degree_sequence))

    degree_sequence = [float(log10(x)) for x in degree_sequence]
    print(max(degree_sequence))
    # Draw the density plot
    sns.distplot(degree_sequence, hist = False, kde = True,
                 kde_kws = {'shade': False,'linewidth': 3},color=color[i], label = str(x[i]))
    i += 1       
    
# Plot formatting
plt.legend()
#plt.title('Density Plot with np.mean(degree_sequenceltiple Airlines')
plt.xlabel('LOG(degree)')
plt.ylabel('Density')
plt.savefig(name + '_density.png')
#plt.xlim(0,max(degree_sequence))
#plt.show()