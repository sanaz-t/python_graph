import networkx as nx
import matplotlib.pyplot as plt

# Define the parameters for the Watts and Strogatz graph
n = int(input('\n  Final number of nodes : n='))  # Number of nodes
k = int(input('\n Means degree  : k='))   # Number of nearest neighbors to connect initially
p = float(input('\n Probability of rewiring : p='))  # Probability of rewiring each edge

# Create the Watts and Strogatz graph
G = nx.watts_strogatz_graph(n, k, p)

# Visualize the graph (optional)
plt.title('watts_strogatz_graph')
nx.draw(G, with_labels=True, node_color="#4BD87A",edge_color='violet', node_size=2, font_size=2)
plt.show()

# calculating parameters:

K=[]
for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
   K.append(nx.average_shortest_path_length(C))
G_average_path_length =K[0]
print('G_average_path_length=', G_average_path_length)

G_CC = nx.average_clustering(G)
print('G_CC=', G_CC)

degree_list=degrees = [val for (node, val) in G.degree()]
G_average_degree=sum(degree_list)/n
print('G_average_degree=', G_average_degree)
print("final graph:", G)
