# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:04:55 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getPos()

def buildPyramid(x,y,z, base=25):
   
    height=(base//2)+1
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        
        x2=x+base-i
        z2=z+base-i
        mc.setBlocks(x1,y1,z1,x2,y,z2,24)

x,y,z=mc.player.getPos()
buildPyramid(x,y,z)
