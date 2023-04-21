# -*- coding: utf-8 -*-
"""A -  Star Algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_B3TSFXX8XX81AlCLfJsJYwc5mBmOtfA

## **Importing** **Libraries**
"""

# Commented out IPython magic to ensure Python compatibility.
import networkx as nx
import matplotlib.pyplot as plt
# %matplotlib inline

"""## **Defining** **Destences**"""

def dist(a,b):
  (x1,y1) = a
  (x2,y2) = b
  return ((x1-x2)**2 + (y1-y2)**2)**0.5

"""## **Defining** **Grid** **Graph**"""

G = nx.grid_graph([3,3])
nx.set_edge_attributes(G, {e:e[1][0]*2 for e in G.edges()}, "cost")

"""## **Visualizing The Grid Graph**"""

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, "cost")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

"""## **Applying A - star**"""

path = nx.astar_path(G, (0,0), (2,2), heuristic=dist, weight="cost")

"""## **Finding Length**"""

length = nx.astar_path_length(G, (0,0), (2,2), heuristic=dist, weight="cost")

"""## **Outcome**"""

print("Path: ", path)

print('Path Length: ', length)