# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:13:37 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

import random

for i in range(100):
    r=random.randrange(1,7)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,326)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,326)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,326)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,326)
        z=z-4
    elif r==5:
        mc.setBlocks(x,y+4,z,x,y,z,326)
        y=y+4
    elif r==6:
        mc.setBlocks(x,y-4,z,x,y,z,326)
        y=y-4
        