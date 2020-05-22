import math 
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for filename in files:
    if ".py" not in filename:
        file1 = open(str(filename), 'r') 
        Lines = file1.readlines() 
        X_ = []
        for line in Lines: 
            if line !="\n":
                output = line.strip().split(",")
                print(output)
                X_.append([float(output[0]),float(output[1]),float(output[2])])
                    
        X = np.array(X_)
        ax.scatter(X[:, 0], X[:, 1],0, s = 10, color = 'b')  

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
