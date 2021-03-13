# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:45:29 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
import random

while True:
    x,y,z=mc.player.getTilePos()
    #y=y+10
    x=x+random.randrange(-20,20)
    z=z+random.randrange(-20,20)
    
    
    mc.spawnEntity(x,y,z,13)