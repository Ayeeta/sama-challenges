import numpy as np 
import matplotlib.pyplot as plt

edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  
    [4, 5], [5, 6], [6, 7], [7, 4],  
    [0, 4], [1, 5], [2, 6], [3, 7]   
]

#To scale dimensions
length = 10
width = 20
height = 30

point_arr = np.array([[20,0,0], [20,0,10], [0,0,0], [0,0,10], [20,10,0], [20,10,10], [0,10,0], [0,10,10]])

arranged_coordinates_arr = np.array([[0,0,0], [20,0,0], [20,10,0], [0,10,0], [0,0,10],[20,0,10], [20,10,10],[0,10,10]])

scaled_arranged_coordinates_arr = arranged_coordinates_arr * [length, width, height]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#Unscaled Cuboid
ax.scatter3D(arranged_coordinates_arr[:, 0], arranged_coordinates_arr[:, 1], arranged_coordinates_arr[:, 2], c='r', marker='o')

for edge in edges:
   ax.plot3D(*zip(*arranged_coordinates_arr[edge]), color='b')
    

#Scaled Cuboid
ax.scatter3D(scaled_arranged_coordinates_arr[:, 0], scaled_arranged_coordinates_arr[:, 1], scaled_arranged_coordinates_arr[:, 2], c='g', marker='o')

for edge in edges:
    ax.plot3D(*zip(*scaled_arranged_coordinates_arr[edge]), color='orange')
    
plt.show()