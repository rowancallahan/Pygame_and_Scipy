# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 16:16:19 2016

@author: RowanCallahan
"""

import math
import pygame
import sys

class moon:
    
    
    speed = [0,0]
    
    def __init__(self,(x,y),size,weight):
        self.position = [x,y]
        self.size = size
        self.weight = weight
    def gravitate(self,body_weight,(body_x, body_y),framerate=30):
        position = (body_x, body_y)
        self.distance_vec = [self.position[0]-position[0], self.position[1]-position[1]]
        distance = math.hypot(self.distance_vec[0], self.distance_vec[1])       
        scalar = (body_weight*self.weight)/((distance**2)*framerate)# f= m*a a= meters*s^-2 if program iterated thirty times persecond then acceleration will be in m*s^-2
        self.speed[0]-= self.distance_vec[0]*scalar/distance # Decomposing vector along x and y
        self.speed[1]-= self.distance_vec[1]*scalar/distance
        
    def toc(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        
        


pygame.init()

size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('circle interaction code')

circle_color =  (255,0,0)
orbiter1 = moon((164,250),5,5)
orbiter1.speed=[0.2,1.7]
clocker = pygame.time.Clock()

font = pygame.font.Font(None, 20)
bitmap = font.render('Butts',True, (255,255,255))

distance_between = str(math.hypot(orbiter1.position[0],orbiter1.position[1]))

points_counter = 0
orbit_points = [[164,250],[163,249]]


while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    clocker.tick(30)    
    orbiter1.gravitate(1050,(250,250))
    orbiter1.gravitate(100,(0,0))    
    orbiter1.toc()
    
    
    distance_between = 'Distance Between: ' + str(int(math.hypot(orbiter1.distance_vec[0],orbiter1.distance_vec[1])))
    distance_counter = font.render(distance_between,True, (255,255,255))

    
    screen.fill((0,0,0))
    position_touple = (int(orbiter1.position[0]),int(orbiter1.position[1]))
    
    position_array = [int(orbiter1.position[0]),int(orbiter1.position[1])]
    
    points_counter += 1

    if points_counter>=15:
        orbit_points.append(position_array)
        points_counter = 0    
    
    
    pygame.draw.circle(screen,circle_color,position_touple,orbiter1.size)
    pygame.draw.circle(screen,circle_color,(250,250),orbiter1.size)
    screen.blit(distance_counter, (0,20))
    pygame.draw.aalines(screen,circle_color,False, orbit_points)
    pygame.display.flip()
