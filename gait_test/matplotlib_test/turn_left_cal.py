#!/usr/bin/env python3
from math import pi, sin, cos, sqrt, acos, atan2, atan
import numpy as np


def cal_turn_left_coords():
    
    stride = 30
    stride_L = 10
    stride_R = 40
    
    raise_feet = 30
    raise_left= 10
    stand = 85

    #中间变量设定
    x1_s=0;x2_s=0;x3_s=0;x4_s=0;y1_s=0;y2_s=0;y3_s=0;y4_s=0
    xs=0
    faai=0.25
    Ts=1
    
    fl_center = -30
    hl_center = -30
    fr_center = -30
    hr_center = -5

    f_stand = stand 
    h_stand = stand 
    xl_up_inc = 0.01*2*stride_L/(Ts*faai)
    xl_dn_inc = 0.01*2*stride_L/(Ts-Ts*faai)
    xr_up_inc = 0.01*2*stride_R/(Ts*faai)
    xr_dn_inc = 0.01*2*stride_R/(Ts-Ts*faai)


    def cal_w(t):  
        nonlocal x1_s,x2_s,x3_s,x4_s,y1_s,y2_s,y3_s,y4_s
            #开始步态计算s


        if t == 0: #迈出腿2
            
            #输出y
            y1_s = f_stand
            y2_s = f_stand
            y3_s = h_stand
            y4_s = h_stand

            #输出x
            x1_s = fr_center + 0.5*stride
            x2_s = fl_center - stride
            x3_s = hl_center + stride
            x4_s = hr_center + 0*stride
            
            print('start, ', end='')

        elif t>0 and t<Ts*faai:    #迈出腿 3 
            sigma=2*pi*t/(faai*Ts)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            zep=raise_left*(1-cos(sigma))/2

            #输出y
            y1_s = f_stand
            y2_s = f_stand
            y3_s = h_stand - zep
            y4_s = h_stand 
            #输出x
            x1_s += xl_dn_inc
            x2_s += xr_dn_inc 
            x3_s += -xl_up_inc 
            x4_s += xr_dn_inc

            print('leg 3, ', end='')


        elif t>=Ts*faai and t<2*Ts*faai:    #迈出腿1
            t=t-faai*Ts
            sigma=2*pi*t/(faai*Ts)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            zep=raise_left*(1-cos(sigma))/2

            #输出y
            y1_s = f_stand - zep
            y2_s = f_stand 
            y3_s = h_stand
            y4_s = h_stand 
            #输出x
            x1_s += -xl_up_inc
            x2_s += xr_dn_inc
            x3_s += xl_dn_inc 
            x4_s += xr_dn_inc

            print('leg 1, ', end='')


        elif t>=2*Ts*faai and t<3*Ts*faai:    #迈出腿4
            t=t-faai*Ts*2
            sigma=2*pi*t/(faai*Ts)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            # zep=h*(1-cos(sigma))/2
            zep=raise_left*(1-cos(sigma))/2

            #输出y
            y1_s = f_stand
            y2_s = f_stand 
            y3_s = h_stand 
            y4_s = h_stand - zep
            #输出x
            x1_s += xl_dn_inc
            x2_s += xr_dn_inc
            x3_s += xl_dn_inc
            x4_s += -xr_up_inc

            print('leg 4, ', end='')
            print([x1_s,y1_s],[x2_s,y2_s],[x4_s,y4_s],[x3_s,y3_s])

        elif t>=3*Ts*faai and t<4*Ts*faai:    #迈出腿2
            t=t-faai*Ts*3
            sigma=2*pi*t/(faai*Ts)
            # zep=h*((sigma-sin(sigma))/(2*pi))
            zep=raise_feet*(1-cos(sigma))/2

            #输出y
            y1_s = f_stand 
            y2_s = f_stand - zep
            y3_s = h_stand 
            y4_s = h_stand 
            #输出x
            x1_s += xl_dn_inc
            x2_s += -xr_up_inc 
            x3_s += xl_dn_inc 
            x4_s += xr_dn_inc 

            print('leg 2, ', end='')

        else:
            return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

        print([x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s])
        return [[x1_s,y1_s],[x2_s,y2_s],[x3_s,y3_s],[x4_s,y4_s]]

    date =[]
    for t in np.arange(0.0,1.001,0.01):
        t = round(t,2)
        result = cal_w(t)
        date.append(result)
    return date


