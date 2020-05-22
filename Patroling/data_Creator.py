import math

from operations_Functions import *

class Data:
    def read_from_input(vessel_num,sectors,frames_num):
        xyz = []
    
        return xyz,frames_num
        
    def unkwown_movement(orth):
        xyz = []
        frames_num = 500
        operations_Functions.brownian_motion_simulation(xyz, [orth[0],orth[1],0], 3, frames_num,1, 1)
        return xyz,frames_num

