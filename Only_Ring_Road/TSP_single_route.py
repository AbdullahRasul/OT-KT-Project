import numpy as np
import os
import time
import matplotlib.pyplot as plt
import networkx as nx
import Coordinates_to_Nx as cnx
from networkx.algorithms.approximation import traveling_salesman_problem
import matplotlib.animation as animation



#----------------------------------- TSP 1 ----------------------------------------------

tsp = nx.approximation.traveling_salesman_problem
# Solve the TSP to get an optimal route
optimal_route = tsp(cnx.graph1, weight='weight')


print("Optimal Route TSP 1:", optimal_route)
print(type(optimal_route))
print(list(cnx.graph1.nodes()))
print(list(cnx.graph1.edges()))


total_distance = 0
for i in range(len(optimal_route) - 1):
    w = cnx.graph1[optimal_route[i]][optimal_route[i + 1]]
    total_distance +=(w['weight'])

# Print statistics
print("Total Distance from TSP 1:", total_distance)


# ------------------------------------------- TSP 2 --------------------
# Solve the TSP to get an optimal route

#----------------------------- Visualization ------------------------
# Create a list to store the colors of each edge
edge_colors = ['gray'] * len(cnx.graph1.edges())

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Function to update the graph visualization for each frame of the animation
def update(frame):
    ax.clear()
    # Get the edges to be traversed up to the current frame
    traversed_edges = optimal_route[:frame+1]
    # Update the colors of the traversed edges
    for i in range(len(traversed_edges) - 1):
        edge = (traversed_edges[i], traversed_edges[i+1])
        reverse_edge = (traversed_edges[i+1], traversed_edges[i])
        if edge in list(cnx.graph1.edges()) and edge_colors[list(cnx.graph1.edges()).index(edge)] == 'gray':
            edge_colors[list(cnx.graph1.edges()).index(edge)] = 'blue'
        elif reverse_edge in list(cnx.graph1.edges()) and edge_colors[list(cnx.graph1.edges()).index(reverse_edge)] == 'gray':
            edge_colors[list(cnx.graph1.edges()).index(reverse_edge)] = 'blue'
        else:
            if edge in list(cnx.graph1.edges()):
                edge_colors[list(cnx.graph1.edges()).index(edge)] = 'red'
            elif reverse_edge in list(cnx.graph1.edges()):
                edge_colors[list(cnx.graph1.edges()).index(reverse_edge)] = 'red'
    # Draw the networkx graph with the updated edge colors
    nx.draw_networkx(cnx.graph1, cnx.pos1, edge_color=edge_colors)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(optimal_route), interval=1000, repeat=False)

# Show the animation
plt.show()