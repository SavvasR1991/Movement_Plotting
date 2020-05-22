import os
import math
import random
import sys

from math import sin, cos, radians, pi
import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init
        
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
        if iteration == total: 
            print()
            
def random_rotation():
    choice = random.choice([-1,1])
    return choice
   
def random_rotation_2():
    choice = random.choice([-1,1,1,1,1,-1])
    return choice 
    
def random_rotation_wave_power():
    choice = random.choice([10,30,45,60])
    return choice
    
def random_disruption_factor():
    choice = random.choice([0,1,2,3,4])
    return choice
    
def point_pos(x0, y0, d, theta):
    theta_rad = np.deg2rad(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)

def distance(a,b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def is_in_range(a,c,radius):
    if ((c.x -a.x)*(c.x -a.x) + (c.y -a.y)*(c.y -a.y))< radius*radius:
        return True
    else:
        return False
        
def compass_direction(curr_x, curr_y, target_x,target_y):
    compass_brackets = ["N","NE","E","SE","S","SW","W","NW","N"]
    delta_x = target_x - curr_x
    delta_y = target_y - curr_y
    
    degrees_temp = math.degrees(math.atan2(delta_x,delta_y))
    if degrees_temp < 0 :
        degrees_final = 360 + degrees_temp
    else:
        degrees_final = degrees_temp
    compass_look_up = int(round(degrees_final/45))
    return compass_brackets[compass_look_up]
    
def angle_normalization(theta):
    if theta < 0:
        theta = 360 + theta
    elif theta > 360:
        theta = theta - 360 
    return theta   
    
def chase(test_mode):
    
    #----------- INITIALIZE VALUES FOR SIMULATOR -----------
   
    #Vessel attributes
    linear_velocity = 3
    linear_velocity_init = linear_velocity
    angular_velocity = 30
    radius = 2
    
    #Initial kinimatics
    theta_curr = 0
    theta_target = 0
    init_x = 0
    init_y = 0
    init_target_x = 0
    init_target_y = 0
    target_x = random_rotation()*60
    target_y = random_rotation()*70
    current_x = init_target_x
    current_y = init_target_y
    init_target_x = target_x
    init_target_y = target_y
    count = 0
    myradians = math.atan2(target_y-current_y, target_x-current_x)
    theta_target = math.degrees(myradians)
    theta_target = angle_normalization(theta_target)
    theta_curr = theta_target
    
    coor = []
    target_coor = []
    circle_w = []
    target_coor.append([target_x,target_y])
    #-------------------------------------------------------
    
    #-------------- START TARGET CHASE ---------------------
    while (count < 1000):
        #Get current actual angle from target
        coor.append([current_x,current_y])
        myradians = math.atan2(target_y-current_y, target_x-current_x)
        theta_target = math.degrees(myradians)
        theta_target = angle_normalization(theta_target)
            
        #Get possible water disruption
        if random_rotation_2() == 1:
            
            power = random_rotation_wave_power()
            if power == 10:
                color = 'aqua'
            elif power == 30:
                color = 'c'
            elif power ==45:
                color = 'b'
            else:
                color = 'r'
            rotation = random_rotation()*power
            tmp_theta_curr = theta_curr
            theta_curr = theta_curr + rotation   
            theta_curr = angle_normalization(theta_curr)
            if test_mode == 0:
                print("{:3}".format(str(count)) + "\033[91m : WAVE HIT ----> " + str(tmp_theta_curr)  +" "+str(rotation) +" -> " +str(theta_curr)+ "\033[0m")
             
            circle_w.append(plt.Circle((current_x,current_y),radius,color=color,alpha=0.5))
        
        #Check if target is in range
        if is_in_range( Point(current_x, current_y), Point(target_x, target_y),radius):
            if test_mode == 0:
                print("{:3}".format(str(count)) + " : [" + str("{:.3f}".format(current_x))+","+str("{:.3f}".format(current_y))+"] -> [" + str(target_x)+","+str(target_y)+"] ," + str(theta_curr)+"->"+str(theta_target) + " " + str(compass))
            coor.append([current_x,current_y])
            break
        else:
            current_x,current_y = point_pos(current_x,current_y,linear_velocity,theta_curr)

            
            
        compass = compass_direction(current_x,current_y,target_x,target_y)
        if test_mode == 0:
            print("{:3}".format(str(count)) + " : [" + str("{:.3f}".format(current_x))+","+str("{:.3f}".format(current_y))+"] -> [" + str(target_x)+","+str(target_y)+"] , diff:"+ str(distance(Point(current_x,current_y),Point(target_x,target_y)))+" " + str(theta_curr)+"->"+str(theta_target) + " " + str(compass))

        #Get current actual target x,y
        if True:
            target_x = target_x + random_rotation()*random_disruption_factor()
            target_y = target_y + random_rotation()*random_disruption_factor()
            plt.plot(target_x, target_y, 'yo')
            target_coor.append([target_x,target_y])
            
        #Counterbalance disrupted angle from waves disruption
        tmp_theta_curr = theta_curr
        sign = ""
        if abs(theta_target - theta_curr) > angular_velocity:
            theta_curr_left = theta_curr - angular_velocity
            theta_curr_left = angle_normalization(theta_curr_left)
            left_turn_x,left_turn_y = point_pos(current_x, current_y, linear_velocity, theta_curr_left)
            
            theta_curr_right = theta_curr + angular_velocity
            theta_curr_right = angle_normalization(theta_curr_right)
            right_turn_x,right_turn_y = point_pos(current_x, current_y, linear_velocity, theta_curr_right)
            
            if distance(Point(left_turn_x,left_turn_y),Point(target_x,target_y)) < distance(Point(right_turn_x,right_turn_y),Point(target_x,target_y)) :
                theta_curr = theta_curr_left
                sign = "-"
            else:
                theta_curr = theta_curr_right
                sign = "+"
            if test_mode == 0:
                print("{:3}".format(str(count)) + "\033[92m : Equalizing --> " + str(tmp_theta_curr)  +" "+sign+str(angular_velocity) +" -> " +str(theta_curr)+ "\033[0m")
        else:
            theta_curr = theta_target
               
        count = count + 1
        if test_mode == 0:
            print("")
    #-------------------------------------------------------
        
    #-------------Plot movement graph ----------------------
    x, y = zip(*coor)
    x_,y_ = zip(*target_coor)
    
    plt.plot(init_x, init_y, 'bo')
    plt.text(init_x, init_y, "Vessel Start")

    plt.plot(target_x, target_y, 'ro')
    plt.text(target_x, target_y, "X",color='r')
    
    plt.plot(init_target_x, init_target_y, 'go')
    plt.text(init_target_x, init_target_y, "Target Start",color='g')
    
    plt.scatter(x, y)
    plt.plot(x, y,color ='black')
    plt.plot(x_, y_)
    
    circle1=plt.Circle((current_x,current_y),radius,color='r',alpha=0.2)
    plt.plot(current_x, current_y, 'co')
    plt.text(current_x, current_y, "Vessel Stop")
    plt.gcf().gca().add_artist(circle1)
    for waves in circle_w:
        plt.gcf().gca().add_artist(waves)

    if count > 300:
        if test_mode == 0:
            plt.show()
        return -1
    else:
        if test_mode == 0:
            plt.show()
        return 0

    #-------------------------------------------------------
   
   
repeats = 1
test_mode = 0
if len(sys.argv) > 1:
    if str(sys.argv[1]) == "test":
        if str(sys.argv[2]).isdigit():
            repeats = int(sys.argv[2])
            test_mode = 1


test = [] 
for i in range(0, repeats):
    test.append(chase(test_mode))
    if test_mode == 1:
        printProgressBar(i+1, repeats, prefix = 'Progress:', suffix = 'Complete', length = 50)
fails = 0;
success = 0 
count = 0   
for i in test:
    if i == -1:
        print("{:4}".format(str(count)) + "\033[91m : FAILED\033[0m")
        fails = fails + 1
    else:
        print("{:4}".format(str(count)) + "\033[92m : SUCCESS\033[0m")
        success = success + 1
    count = count + 1
print("\033[91m \nFAILED  : " + str(fails)+ "\033[0m")
print("\033[92mSUCCESS : " + str(success)+ "\033[0m")
