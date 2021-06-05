# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:59:35 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

import random

for i in range(100):
    r=random.randrange(1,5)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,35,1)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,35,1)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x+4,y,z+4,35,1)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,35,1)
        z=z-4