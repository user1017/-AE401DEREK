# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:17:10 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

import random
import time

while True:
    x,y,z=mc.player.getTilePos()
    #y=y+10
    x=x+random.randrange(-1,1)
    z=z+random.randrange(-1,1)
    
    
    mc.spawnEntity(x,y+3,z,7)
    time.sleep(5)