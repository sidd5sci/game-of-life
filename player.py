

import time,math,random
import pygame
from physics import *
from vector import *

'''
timer controls different assets of game 
for how long the asset remain in the game
'''
class timer:

    def __init__(self,name = 'none',beg = 100.0,end = 00.0,rate = 5.0):
        self.name = name
        self.begAt = beg # beg value is > 0
        self.timer = beg
        self.endAt = end # end value is < 100
        self.rate = rate # rate vale can be any
    def update(self):
        self.timer -= self.rate
        self.checkEnd()
    def checkEnd(self):
        if self.timer <= self.endAt:
           self.timer = self.endAt
    def beginTimer(self,name = 'none',beg = 100.0,end = 00.0,rate = 5.0):
        self.name = name
        self.begAt = beg # beg value is > 0
        self.timer = beg
        self.endAt = end # end value is < 100
        self.rate = rate # rate vale can be any
    def setEnd(self,endAt):
        self.endAt = endAt
    def setbeg(self,beg):
        self.begAt = beg
    def setName(self,name):
        self.name = name
'''
player class
'''
class player(physics):

    def __init__(self,pos):
        super(self,player).__init__(pos)
        self.health = 100
        self.timers = [] # list of all the timers 
        self.activeState = 'right'
        self.velocity.asign(0,0,0)
    def loadPlayer(self):
        # loading the player static state
        self.left = pygame.image.load('')
        self.right = pygame.image.load('')
        self.up = pygame.image.load('')
        self.down = pygame.image.load('')
        
        # loading player walking states
        self.walkLeft = pygame.image.load('')
        self.walkRight = pygame.image.load('')
        self.walkUp = pygame.image.load('')
        self.walkDown = pygame.image.load('')
        # loading jumping states
        self.jumpUp = pygame.image.load('')
        self.jumpDown = pygame.image.load('')
    def createTimer(self,name,beg,end,rate):
        t = timer(name,beg,end,rate)
        self.timer.appen(t)
    def loadPlayerAssets(self):
        self.hair = pygame.image.load('')
    def move(self):
        if self.activeState == 'left':
          screen.pygame.blit()
        if self.activeState == 'right':
          screen.pygame.blit()
        if self.activeState == 'up':
          screen.pygame.blit()
        if self.activeState == 'down':
          screen.pygame.blit()
    def playerAi(self):
        pass
    def bound(self,window):
        if self.pos[0] < window[0]:
           self.pos[0] = window[0]
        if self.pos[0]+w > window[3]:
           self.pos[0] = w+window[0]
    def attack(self,attacId):
        pass
    def pickUpAsset(self,assetId):
        pass
    def dropAsset(self,assetId):
        pass
    def pathFind(self):
        pass