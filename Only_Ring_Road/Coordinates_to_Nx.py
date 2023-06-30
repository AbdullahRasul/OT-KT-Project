import numpy as np
import os
import time
import matplotlib.pyplot as plt
import networkx as nx
import point_extractor as pe

def create_graph(x_coordinates, y_coordinates):
    graph = nx.Graph()

    # Add nodes to the graph
    for i, (x, y) in enumerate(zip(x_coordinates, y_coordinates)):
        graph.add_node(i, x=x, y=y)

    # Add edges to the graph
    for i in range(len(x_coordinates) - 1):
        distance = calculate_distance(x_coordinates[i], y_coordinates[i], x_coordinates[i+1], y_coordinates[i+1])
        graph.add_edge(i, i+1, weight=distance)

    return graph

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Example x and y coordinates
x_coordinates1 = pe.lane_x_list[0]
y_coordinates1 = pe.lane_y_list[0]

x_coordinates2 = pe.lane_x_list[1]
y_coordinates2 = pe.lane_y_list[1]

x_coordinates3 = pe.lane_x_list[2]
y_coordinates3 = pe.lane_y_list[2]

x_coordinates4 = pe.lane_x_list[3]
y_coordinates4 = pe.lane_y_list[3]

x_coordinates5 = pe.lane_x_list[4]
y_coordinates5 = pe.lane_y_list[4]

x_coordinates6 = pe.lane_x_list[5]
y_coordinates6 = pe.lane_y_list[5]

x_coordinates7 = pe.lane_x_list[6]
y_coordinates7 = pe.lane_y_list[6]

x_coordinates8 = pe.lane_x_list[7]
y_coordinates8 = pe.lane_y_list[7]

# Create the graph
graph1 = create_graph(x_coordinates1, y_coordinates1)
graph2 = create_graph(x_coordinates2, y_coordinates2)
graph3 = create_graph(x_coordinates3, y_coordinates3)
graph4 = create_graph(x_coordinates4, y_coordinates4)
graph5 = create_graph(x_coordinates5, y_coordinates5)
graph6 = create_graph(x_coordinates6, y_coordinates6)
graph7 = create_graph(x_coordinates7, y_coordinates7)
graph8 = create_graph(x_coordinates8, y_coordinates8)

# Draw the graph
pos1 = {node: (graph1.nodes[node]['x'], graph1.nodes[node]['y']) for node in graph1.nodes()}
pos2 = {node: (graph2.nodes[node]['x'], graph2.nodes[node]['y']) for node in graph2.nodes()}
pos3 = {node: (graph3.nodes[node]['x'], graph3.nodes[node]['y']) for node in graph3.nodes()}
pos4 = {node: (graph4.nodes[node]['x'], graph4.nodes[node]['y']) for node in graph4.nodes()}
pos5 = {node: (graph5.nodes[node]['x'], graph5.nodes[node]['y']) for node in graph5.nodes()}
pos6 = {node: (graph6.nodes[node]['x'], graph6.nodes[node]['y']) for node in graph6.nodes()}
pos7 = {node: (graph7.nodes[node]['x'], graph7.nodes[node]['y']) for node in graph7.nodes()}
pos8 = {node: (graph8.nodes[node]['x'], graph8.nodes[node]['y']) for node in graph8.nodes()}


'''
nx.draw(graph1, pos=pos1, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph2, pos=pos2, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph3, pos=pos3, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph4, pos=pos4, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph5, pos=pos5, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph6, pos=pos6, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph7, pos=pos7, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graph8, pos=pos8, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
'''


# Show the plot
#plt.show()
#plt.figure()

#nodes files coordinates
xn_coordinates1 = pe.node_x_list[0]
yn_coordinates1 = pe.node_y_list[0]

xn_coordinates2 = pe.node_x_list[1]
yn_coordinates2 = pe.node_y_list[1]

xn_coordinates3 = pe.node_x_list[2]
yn_coordinates3 = pe.node_y_list[2]

xn_coordinates4 = pe.node_x_list[3]
yn_coordinates4 = pe.node_y_list[3]

xn_coordinates5 = pe.node_x_list[4]
yn_coordinates5 = pe.node_y_list[4]


graphn1 = create_graph(xn_coordinates1, yn_coordinates1)
graphn2 = create_graph(xn_coordinates2, yn_coordinates2)
graphn3 = create_graph(xn_coordinates3, yn_coordinates3)
graphn4 = create_graph(xn_coordinates4, yn_coordinates4)
graphn5 = create_graph(xn_coordinates5, yn_coordinates5)


posn1 = {node: (graphn1.nodes[node]['x'], graphn1.nodes[node]['y']) for node in graphn1.nodes()}
posn2 = {node: (graphn2.nodes[node]['x'], graphn2.nodes[node]['y']) for node in graphn2.nodes()}
posn3 = {node: (graphn3.nodes[node]['x'], graphn3.nodes[node]['y']) for node in graphn3.nodes()}
posn4 = {node: (graphn4.nodes[node]['x'], graphn4.nodes[node]['y']) for node in graphn4.nodes()}
posn5 = {node: (graphn5.nodes[node]['x'], graphn5.nodes[node]['y']) for node in graphn5.nodes()}
'''
nx.draw(graphn1, pos=posn1, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graphn2, pos=posn2, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graphn3, pos=posn3, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graphn4, pos=posn4, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)
nx.draw(graphn5, pos=posn5, with_labels=True, node_color='lightblue', node_size=50, edge_color='gray',font_size=6)


plt.show()


'''