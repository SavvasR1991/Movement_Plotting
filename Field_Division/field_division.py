import os
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

def sub_rectangles(factor_x, factor_y,westlimit=0, southlimit=0, eastlimit=2, northlimit=2):
    table=list()
    lat_adj_factor=(northlimit-southlimit)/factor_x
    lon_adj_factor=(eastlimit-westlimit)/factor_y
    lat_list=[]
    lon_list=[]
    for i in range(factor_x+1):
        lon_list.append(westlimit)
        westlimit+=lon_adj_factor
    for i in range(factor_y+1):
        lat_list.append(southlimit)
        southlimit+=lat_adj_factor
    for i in range(0,len(lon_list)-1):
        for j in range(0,len(lat_list)-1):
            table.append([(lon_list[i],lat_list[j]),(lon_list[i+1],lat_list[j]),(lon_list[i],lat_list[j+1]),(lon_list[i+1],lat_list[j+1])]) 
    return table

def create_2d_grid(x1,y1,x3,y3, factor_x, factor_y):
    angle = 0
    mx = x1 + (x3 - x1) * 0.5
    my = y1 + (y3 - y1) * 0.5

    cos = math.cos(-angle)
    sin = math.sin(-angle)

    x1u = cos * (x1-mx) - sin * (y1-my) + mx
    y1u = sin * (x1-mx) + cos * (y1-my) + my
    x3u = cos * (x3-mx) - sin * (y3-my) + mx
    y3u = sin * (x3-mx) + cos * (y3-my) + my

    width  = abs(x3u - x1u)

    cos = math.cos(angle)
    sin = math.sin(angle)

    x2u = x1u
    y2u = y3u
    x4u = x3u
    y4u = y1u

    x2 = cos * (x2u-mx) - sin * (y2u-my) + mx
    y2 = sin * (x2u-mx) + cos * (y2u-my) + my
    x4 = cos * (x4u-mx) - sin * (y4u-my) + mx
    y4 = sin * (x4u-mx) + cos * (y4u-my) + my

    return sub_rectangles(factor_x, factor_y,x2, y2,x4, y4)


def create_3d_grid(x1,y1,z1,x3,y3,z3, factor_x, factor_y, factor_z):
    t = create_2d_grid(x1, y1, x3,y3,factor_x,factor_y) 
    z_dis = abs(abs(z3) - abs(z1))
    z_segments = float(z_dis) / float(factor_z) 
    t_3d = []
    for f in range(0, factor_z):
        for i in t:
            t_c =[]
            for j in i:
                t_c.append([j[0],j[1],z1])
            for j in i:
                t_c.append([j[0],j[1],z1 + z_segments])
            t_3d.append(t_c)
        z1 = z1 + z_segments
    return t_3d

def create_grid(NW_x, NW_y, NW_z, SE_x,SE_y,SE_z, factor_x, factor_y, factor_z):
    if SE_z == NW_z:
        t = create_2d_grid(NW_x, NW_y, SE_x,SE_y, factor_x, factor_y)
    else:
        t = create_3d_grid(NW_x, NW_y, NW_z, SE_x,SE_y,SE_z, factor_x, factor_y, factor_z)
    return t

def plot_graph(t, NW_z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    rectangles = []
    count = 1
    for i in t :
        points = []
        for j in i:
            if len(j) == 3:
                ax.scatter(j[0], j[1], j[2])
                points.append([j[0], j[1],j[2]]) 
            else:
                ax.scatter(j[0], j[1], NW_z)
                points.append([j[0], j[1], NW_z]) 
        x_text =  (points[0][0] + points[1][0])/2        
        y_text =  (points[1][1] + points[2][1])/2 
        if len(j) == 3: 
            z_text =  (points[0][2] + points[4][2])/2  
        else:
            z_text =  NW_z  
        ax.text(x_text,y_text,z_text,str(count))      
        count += 1
        rectangles.append(points)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

def main():
    #For 2d grid just set NW_z == SE_z
    NW_x = 3
    NW_y = 3
    NW_z = 3 

    SE_x_up = 50
    SE_y_up = -50
    SE_z_up = 30

    factor_x = 3
    factor_y = 3
    factor_z = 2

    t = create_grid(NW_x, NW_y, NW_z, SE_x_up, SE_y_up, SE_z_up, factor_x, factor_y, factor_z) 
    plot_graph(t,NW_z)

if __name__ == "__main__":
    main()

