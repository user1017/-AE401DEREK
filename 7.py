# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:01:45 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
import time
time.sleep(5)
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,57)
time.sleep(0.5)
mc.setBlock(x,y+1,z,57)
time.sleep(0.5)
mc.setBlock(x,y+2,z,57)
time.sleep(0.5)
mc.setBlock(x,y+3,z,57)
time.sleep(0.5)
mc.setBlock(x,y+4,z,57)
time.sleep(0.5)
mc.setBlock(x,y+5,z,57)