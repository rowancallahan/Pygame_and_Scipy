# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 20:55:34 2016

@author: RowanCallahan
"""
import numpy as np
import math
import pygame
import sys

class boid:
    
    
    
    def __init__(self, (x,y),to_center=100,dodge=10,match_speed=8, velocity=[0,0], hunger=80,max_speed=10):
        self.position = [x,y]
        self.velocity = velocity
        self.to_center = to_center
        self.dodge = dodge
        self.match_speed = match_speed
        self.hunger = hunger
        self.max_speed = max_speed
        
        
    def flock(self,boid_array):
        
        flock_vec = [0.0,0.0]
        size = len(boid_array) -1.0#we are excluding one the boid we are using from our center calculations
        
        for b in boid_array:
            if b != self:
                flock_vec = np.add(flock_vec,self.position)
        
        flock_vec = np.divide(flock_vec,size)
        
        return np.divide(np.subtract(flock_vec,self.position),b.to_center)

    def avoid(self,boid_array):
        c = [0.0,0.0]
        for b in boid_array:
            if b != self:
                if math.hypot(b.position[0]-self.position[0],b.position[1] -self.position[1]) <10:
                    c = np.subtract(c, np.subtract(b.position,self.position))
        return c

    def match(self,boid_array):
        
        flock_velocity = [0.0,0.0]
        size = len(boid_array) -1.0
        
        for b in boid_array:
            if b != self:
                flock_velocity = np.add(flock_velocity,b.velocity)
        flock_velocity = np.divide(flock_velocity,size)
        
        return np.divide(np.subtract(flock_velocity, self.velocity),self.match_speed)
        
    def speed_limit(self):

        abs_speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

        if abs_speed > self.max_speed:
            self.velocity=np.multiply(np.divide(self.velocity,math.hypot(self.velocity[0],self.velocity[1])),self.max_speed)

    def feed(self, (food_x,food_y)):
        food_location = [food_x,food_y]
        return np.divide(np.subtract(food_location,self.position),self.hunger)

    def update(self, boid_array,(food_x,food_y)):
        
        food = [food_x,food_y]        
        
        rule1 = self.flock(boid_array)
        rule2 = self.avoid(boid_array)
        rule3 = self.match(boid_array)
        rule4 = self.feed(food)

        
        rules_vec = [rule1[0]+rule2[0] +rule3[0]+rule4[0], rule1[1]+rule2[1]+rule3[1]+rule4[1]]       
        
        self.velocity = np.add(self.velocity, rules_vec)
        self.speed_limit()
        self.position = np.add(self.position, self.velocity)
        

import numpy as np

class swarm:
    boid_array = []
    
    def __init__(self,swarm_size,(screen_x,screen_y), to_center=100, dodge=10, match_speed=8, member_size=5,food=(0,0),hunger=(60)):
        swarm_points = np.random.rand(swarm_size,2)
        self.window = [screen_x,screen_y]
        self.member_size = member_size
        self.swarm_size =swarm_size
        self.to_center = to_center
        self.dodge = dodge
        self.match_speed = match_speed
        self.food = food
        self.hunger = hunger
        
        for b in np.arange(swarm_size):
            member = boid((swarm_points[b,0]*self.window[0],swarm_points[b,1]*self.window[1]),to_center=self.to_center, dodge=self.dodge, match_speed=self.match_speed)
            self.boid_array.append(member)
            
    def animate(self,screen,food=(350,350)):
        
        self.food=food        
        
        for b in self.boid_array:
            b.update(self.boid_array,self.food)
            location_touple = (int(b.position[0]),int(b.position[1]))
            pygame.draw.circle(screen,(255,0,0,0),location_touple,self.member_size)




pygame.init()
size = (700,700)
square_window = pygame.display.set_mode(size)
a =swarm(40,size,food=(350,350))
clocking = pygame.time.Clock()
pygame.display.set_caption('boids')

counter = 0

point1 = int(a.boid_array[1].position[0])
point2 = int(a.boid_array[1].position[1])
point3 = int(a.boid_array[1].position[0])+1
point4 = int(a.boid_array[1].position[1])+1

points = [[point1,point2],[point3,point4]]

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    clocking.tick(30)
    square_window.fill((0,0,0))
    
    
    counter += 1
    point5 = int(a.boid_array[1].position[0])
    point6 = int(a.boid_array[1].position[1])
    positions_array = [point5,point6]
    if counter>=5:
        points.append(positions_array)
        points_counter = 0    
    
    
    food_position_tuple= pygame.mouse.get_pos()   
    
    
    a.animate(square_window,food=food_position_tuple)
    pygame.draw.circle(square_window,(255,0,0,0),food_position_tuple,10)
    pygame.draw.aalines(square_window,(255,0,255,0),False, points)    
    
    pygame.display.flip()