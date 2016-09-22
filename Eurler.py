# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 07:32:53 2015

@author: isurwars
"""
import numpy as np
import matplotlib.pyplot as plt


#Fuerza a la que está sometida el sistema
def fx(x,px):
    return 0.0 #m/s**2
    
def fy(y,py):
    return -9.81 #m/s**2


#Inicializar variables
vx_ini = 10.0 #m/s 
vy_ini = 20.0  #m/s

x_ini = 0.0   #m
y_ini = 0.0   #m

m = 1.0       #Kg

ts = 0.01      #s
steps = 1000  #numero de pasos

vx = vx_ini
vy = vy_ini
x = x_ini
y = y_ini
for i in range(steps):
    vx += ts*fx(x,m*vx)/m
    vy += ts*fy(y,m*vy)/m
    x += ts*vx
    y += ts*vy
    if y<0.0 :
        break
    plt.plot(x,y,"ro")
plt.show()