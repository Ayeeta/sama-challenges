import numpy as np 
import matplotlib.pyplot as plt

point_arr = np.array([[20,0,0], [20,0,10], [0,0,0], [0,0,10], [20,10,0], [20,10,10], [0,10,0], [0,10,10]])

arranged_coordinates_arr = np.array([[0,0,0], [20,0,0], [20,10,0], [0,10,0], [0,0,10],[20,0,10], [20,10,10],[0,10,10]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(arranged_coordinates_arr[:, 0], arranged_coordinates_arr[:, 1], arranged_coordinates_arr[:, 2], c='r', marker='o')

for i in range(4):
    ax.plot3D([arranged_coordinates_arr[i, 0], arranged_coordinates_arr[i+4, 0]],
              [arranged_coordinates_arr[i, 1], arranged_coordinates_arr[i+4, 1]],
              [arranged_coordinates_arr[i, 2], arranged_coordinates_arr[i+4, 2]], color='b')
    
    ax.plot3D([arranged_coordinates_arr[i, 0], arranged_coordinates_arr[(i+1) % 4, 0]],
              [arranged_coordinates_arr[i, 1], arranged_coordinates_arr[(i+1) % 4, 1]],
              [arranged_coordinates_arr[i, 2], arranged_coordinates_arr[(i+1) % 4, 2]], color='b')
    
    ax.plot3D([arranged_coordinates_arr[i + 4, 0], arranged_coordinates_arr[4 + (i+1) % 4, 0]],
              [arranged_coordinates_arr[i + 4, 1], arranged_coordinates_arr[4 + (i+1) % 4, 1]],
              [arranged_coordinates_arr[i + 4, 2], arranged_coordinates_arr[4 + (i+1) % 4, 2]], color='b')
    
plt.show()