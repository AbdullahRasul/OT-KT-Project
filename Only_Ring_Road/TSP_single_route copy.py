import numpy as np
import os
import time
import matplotlib.pyplot as plt
import networkx as nx
import Coordinates_to_Nx as cnx
from networkx.algorithms.approximation import traveling_salesman_problem
import matplotlib.animation as animation



#----------------------------------- TSP 1 ----------------------------------------------
# Perform DFS traversal starting from node 1
print("DFS Traversal:")
dfs_traversal = nx.dfs_preorder_nodes(cnx.graph1, source=0)
for node in dfs_traversal:
    print(node,end = ' ')  # You can perform any desired operation on the node here

# Perform BFS traversal starting from node 1
print("BFS Traversal:")
bfs_traversal = nx.bfs_tree(cnx.graph1, source=0).nodes()
for node in bfs_traversal:
    print(node)  # You can perform any desired operation on the node here