import math

from operations_Functions import *

class Data:
    def unkwown_movement():
        xyz = []
        operations_Functions.brownian_motion_simulation(xyz, [0,5,5], 3, 500,1, 1)
        return xyz

