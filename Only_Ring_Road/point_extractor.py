import numpy as np
import os
import time
import matplotlib.pyplot as plt

path = os.path.abspath(__file__).split('point_extractor.py')[0]

lane_file_list = []
node_file_list = []
for i in os.listdir(path):
    if "lane_" in i:
        lane_file_list.append(path + i)
        print(path + i)
    elif "node_" in i:
        node_file_list.append(path + i)
        print(path + i)

lane_x_list = []
lane_y_list = []
for i in lane_file_list:
    
    fp = open(i, 'r')
    x = []
    y = []
    while True:
        line = fp.readline()
        if not line:
            break
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))

    lane_x_list.append(x)
    lane_y_list.append(y)

node_x_list = []
node_y_list = []
for i in node_file_list:
    
    fp = open(i, 'r')
    x = []
    y = []
    while True:
        line = fp.readline()
        if not line:
            break
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))

    node_x_list.append(x)
    node_y_list.append(y)

'''

plt.figure()
for i in range(len(lane_x_list)):
    plt.plot(lane_x_list[i], lane_y_list[i], 'r*-')
    #plt.text(lane_x_list[i][10], lane_y_list[i][10], lane_file_list[i].split('\\')[-1].split('.')[0], fontsize = 40)
for i in range(len(node_x_list)):
    plt.plot(node_x_list[i], node_y_list[i], 'b*-')
#    plt.text(node_x_list[i][10], node_y_list[i][10], node_file_list[i].split('\\')[-1].split('.')[0], fontsize = 40)
    
# plt.plot(-156.9, -59.1, 'vm', markersize = 30, label = 'Base Station')
# plt.legend(fontsize = 40)
plt.grid()
plt.axis('equal')
plt.show()
'''