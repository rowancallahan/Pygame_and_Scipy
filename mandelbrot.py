# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 01:33:27 2016

@author: RowanCallahan
"""


import numpy as np
import matplotlib.pyplot as pl

width =300
height =300
resolution = (width,height)

location = (0.275,0.0)
zoom = 1/20.0



x_param = ((location[0]-zoom),(location[0]+zoom))
y_param = ((location[1]+zoom),(location[1]-zoom))


color = np.linspace(20,50,40)

x_values = np.linspace(x_param[0],x_param[1],width)
y_values =np.linspace(y_param[0],y_param[1],height)
size = np.arange(0,width,1)


c = np.ones(resolution,"complex64")
colors = np.ones(resolution,"int")


for y in size:
    for x in size:
        c[y,x]=x_values[x]+ 1j*y_values[y]




counter = 0
for y in size:
    for x in size:
        counter = 0
        original = c[y,x]  
        colors[y,x]=1        
        while counter <36:           
            c[y,x]= c[y,x]**2 + original
            counter = counter +1
            if np.abs(c[y,x])>=2.01:
                colors[y,x] = color[counter]
                break




          
e = np.abs(c)>2.01



pl.imshow(np.abs(e),cmap="gray")

pl.imshow(colors,cmap="rainbow")
