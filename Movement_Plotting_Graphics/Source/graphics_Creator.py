import os
import math 
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
import mpl_toolkits.mplot3d.art3d as art3d

from matplotlib import animation
from data_Creator import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle, PathPatch
pause = False

def make_helix(xyz):
    x, y, z= zip(*xyz)
    helix = np.vstack((x, y, z))
    return helix

def onClick(event):
    global pause
    pause = True

def update(num, dataLines, lines , data2, lines2) :
    for line, data in zip(lines, dataLines) :
        line.set_data(data[0:2, num-1:num])
        line.set_3d_properties(data[2,num-1:num])

    for i in range(0, len(data2)):
        for line1, data1 in zip(lines2[i], data2[i]) :
            line1.set_data(data1[0:2, num-1:num])
            line1.set_3d_properties(data1[2,num-1:num])
    return lines, lines2


def set_up_components(base, plane):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-plane, plane)
    ax.set_ylim(-plane, plane)
    ax.set_zlim(-plane, plane)

    return fig, ax, base[0], base[1], base[2]


def base_point(xc, yc, r, sectors):
    theta = 360 / sectors
    points = []
    for point in range(0, sectors):
        points.append([(xc + r*math.sin(math.pi * 2 * point *theta / 360)),(yc + r*math.cos(math.pi * 2 * point * theta / 360))])
    return points


def plot_sectors(ax, base_point_s, base, ship_high):
    for i in base_point_s:
        print(i)
        ax.plot([i[0], base[0]], [i[1], base[0]], [ship_high , ship_high], 'r',alpha= 1)


def plot_cylinder(ax, base, ship_radius, ship_high):
    Xc,Yc,Zc = data_for_cylinder_along_z(base[0], base[1],ship_radius,ship_high)
    ax.plot_surface(Xc, Yc, Zc, alpha=0.5)


def data_for_cylinder_along_z(center_x,center_y,radius,height_z):
    z = np.linspace(0, height_z, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid=np.meshgrid(theta, z)
    x_grid = radius*np.cos(theta_grid) + center_x
    y_grid = radius*np.sin(theta_grid) + center_y
    return x_grid, y_grid, z_grid


def plot_cycles_contours(ax, base, ship_radius, ship_high):
    p = Circle((base[0], base[1]), ship_radius, alpha= 0.2)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    p = Circle((base[0], base[1]), ship_radius,color='black', alpha= 0.5,  linewidth=2, fill=False)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0+ship_high, zdir="z")


def create_base(base_coordinates, ship_radius, ship_high, sectors, plane):

    fig,ax,ship_coordinates_x, ship_coordinates_y, ship_coordinates_z = set_up_components(base_coordinates, plane)

    base_point_s = base_point(ship_coordinates_x, ship_coordinates_y, ship_radius, sectors)

    plot_sectors(ax, base_point_s, base_coordinates, ship_high)

    plot_cylinder(ax, base_coordinates, ship_radius, ship_high)

    plot_cycles_contours(ax, base_coordinates, ship_radius, ship_high)

    return ax, fig


def start_animation(ax, fig, sectors):
    xyz = Data.unkwown_movement()
    data = [make_helix(xyz)]
    lines = [ax.plot(data[0][0,0:1], data[0][1,0:1], data[0][2,0:1], 'o')[0]]

    data1 = []
    lines1 = []
    for i in range(0, sectors):
        xyz = Data.unkwown_movement()
        data1.append([make_helix(xyz)])
        lines1.append([ax.plot(data1[i][0][0,0:1], data1[i][0][1,0:1], data1[i][0][2,0:1], 'o',color='b')[0]])

    fig.canvas.mpl_connect('button_press_event', onClick)
    ani = animation.FuncAnimation(fig, update,frames=500, fargs=(data, lines, data1 ,lines1), interval=1, blit=False, repeat=True)
    plt.show()

def simulation_graphics_animation(base_coordinates, ship_radius, ship_high, sectors, plane): 

    ax, fig = create_base(base_coordinates, ship_radius, ship_high, sectors, plane)

    start_animation(ax, fig, sectors)
  














