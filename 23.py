# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:05:35 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getPos()

#for i in range(20):
    #mc.setBlock(x+i,y-1,z+i,155)
    #mc.setBlock(x+i+1,y-1,z+i,155)
    #mc.setBlock(x+i+2,y-1,z+i,155)
    
for i in range(20):
    for j in range(3):
        mc.setBlock(x+i+j,y-1,z+i,155)
        