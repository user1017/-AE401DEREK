# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:44:51 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
import time
time.sleep(5)
x,y,z=mc.player.getTilePos()
mc.setBlock(x-1,y-1,z+1,57)
time.sleep(0.5)
mc.setBlock(x,y-1,z+1,57)
time.sleep(0.5)
mc.setBlock(x+1,y-1,z+1,57)
time.sleep(0.5)
mc.setBlock(x+1,y-1,z,57)
time.sleep(0.5)
mc.setBlock(x+1,y-1,z-1,57)
time.sleep(0.5)
mc.setBlock(x,y-1,z-1,57)
time.sleep(0.5)
mc.setBlock(x-1,y-1,z-1,57)
time.sleep(0.5)
mc.setBlock(x-1,y-1,z,57)