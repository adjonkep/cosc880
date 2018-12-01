import numpy as np


coord_file = open('C:/Users/atouomo/Downloads/test_coord.txt', 'r')
raw_coord = coord_file.read()
raw_coord = raw_coord.replace(".", "")
coord = raw_coord.split("},{")
# Remove "{" from first and lat element of list
coord[0]= coord[0].replace("{", "")
coord[len(coord)-1] = coord[len(coord)-1].replace("}", "")

distance = []
dist = 0
distance.append(dist)

#Spa 1.796 m/pixel

spa_m_pix_ratio = 1.796

for index, item in enumerate(coord):
    if index < len(coord)-1:
        pt1 = coord[index].split(",")
        pt2 = coord[index + 1].split(",")
        euclid_distance = np.sqrt(((float(pt2[0])-float(pt1[0]))**2) + (float(pt2[1])-float(pt1[1]))**2)
        dist = dist + euclid_distance
        distance.append(dist * spa_m_pix_ratio)

print(distance)