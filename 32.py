# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:12:52 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getPos()

number=1

for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
        
        number=number*2
        