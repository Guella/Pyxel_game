# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 13:55:00 2025

@author: salma
"""

import pyxel
import random as rand

###################################
########## CONSTANTS ##############
###################################

WIDTH = 350
HEIGHT = 180

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 5
PLAYER_BASE_SPEED = 2

OBSTACULO_MIN_WIDTH = 2
OBSTACULO_MAX_WIDTH = 6
OBSATCULO_MIN_HEIGTH = 5
OBSATCULO_MAX_HEIGTH = 10

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.is_alive = True
        
class Obstaculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = rand.randint(OBSTACULO_MIN_WIDTH, OBSTACULO_MAX_WIDTH)
        self.h = rand.randint(OBSATCULO_MIN_HEIGTH, OBSATCULO_MAX_HEIGTH)

class Jogo:
 def __init__(self):
     pyxel.init(WIDTH, HEIGHT, title="Jogo", fps = 60)
     self.y = HEIGHT/2
     self.r = 10
     self.dir = 0
     self.speed = 2
     self.x = 20
     pyxel.run(self.update, self.draw)
 def update(self):
     # if self.x == 160 - self.r and self.dir == 0:
     #     self.dir = 1
     # elif self.x == 0 + self.r and self.dir == 1:
     #     self.dir = 0
     # elif self.x < 160 - self.r and self.dir == 0:
     #     self.x = (self.x + 1) % pyxel.width
     # elif self.x > 0 + self.r and self.dir == 1:
     #     self.x = (self.x - 1) % pyxel.width
     if pyxel.btn(pyxel.KEY_LSHIFT):
         self.speed = 4
     else:
         self.speed = 2
     if pyxel.btn(pyxel.KEY_RIGHT):
         if self.x >= WIDTH - (self.r + self.speed):
             pass
         else:
             self.x = (self.x + self.speed) % pyxel.width
     elif pyxel.btn(pyxel.KEY_LEFT):
         if self.x <= 0 + (self.r + self.speed):
             pass
         else:
             self.x = (self.x - self.speed) % pyxel.width
     if pyxel.btn(pyxel.KEY_DOWN):
         if self.y >= HEIGHT - (self.r + self.speed):
             pass
         else:
             self.y = (self.y + self.speed) % pyxel.width
     elif pyxel.btn(pyxel.KEY_UP):
         if self.y <=  0 + (self.r + self.speed):
             pass
         else:
             self.y = (self.y - self.speed) % pyxel.width
 def draw(self):
     pyxel.cls(0)
     pyxel.circ(self.x, self.y, self.r, 5)

Jogo()