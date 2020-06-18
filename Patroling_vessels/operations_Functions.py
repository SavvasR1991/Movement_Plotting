import os
import math
import numpy as np

class operations_Functions():

    def brownian_motion_simulation(xyz,cur,m,n,d,t):
        dt = t / float(n - 1)
        for j in range(1, n):
            s = np.sqrt(2.0 * m * d * dt) * np.random.randn(1)
            dx = np.random.randn(m)
            norm_dx = np.sqrt(np.sum(dx ** 2))
            for i in range(0, m):
                dx[i] = s * dx[i] / norm_dx
                cur[0] += dx[0]; cur[1] += dx[1]
            cur[2] = 0
            p = np.array(cur[:])
            xyz.append(cur[:])
