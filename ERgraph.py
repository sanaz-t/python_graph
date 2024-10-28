import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from itertools import product

n = int(input('\n  Final number of nodes : n='))  # 16216  # len(A1)
print("n=", n)
p0=float(input('please insert p0:') )  #.03


df = lambda p: -(np.log(n)-0.5)/(((np.log(p*(n-1)))**2)*p*(n-1))
theta = 0.02
precision = 0.0001
max_iters = 1000
iters_count = 0
previous_step_size = 1
while previous_step_size > precision and iters_count < max_iters:
    prev_p0 = p0
    p0 = p0 - theta * df(prev_p0)
    previous_step_size = abs(p0 - prev_p0)
    iters_count = iters_count + 1

print("minimum occurs at", p0)
p=p0

# def erdos_renyi_graph(n,p):
#     G=nx.Graph()
#     G.add_nodes_from(range(n))
#     for i in range(n):
#         for j in range(i+1,n):
#             if np.random.random() <= p:
#                 G.add_edge(i,j)
#     return G

G=nx.erdos_renyi_graph(n,p)
print("erdos renyi:", G)
plt.title('erdos renyi graph')
nx.draw(G, alpha=0.1, edge_color="#016963", node_color="#c91352", node_size=2, with_labels=True)
plt.show()

K=[]
for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
   K.append(nx.average_shortest_path_length(C))
G_average_path_length =K[0]
print('G_average_path_length=', G_average_path_length)

cc_matrix = nx.clustering(G)
cc_matrix=list(cc_matrix.values())
# print('cc_matrix=',cc_matrix)
G_CC = nx.average_clustering(G)
print('G_CC=', G_CC)

degree_list=degrees = [val for (node, val) in G.degree()]
G_average_degree=sum(degree_list)/n
print('G_average_degree=', G_average_degree)
print("final graph:", G)

