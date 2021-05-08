# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:19:10 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getPos()

def plantTree (x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
for i in range(10):
    for j in range(5):
        plantTree(x+i*5,y,z+j*5)
    
        

    