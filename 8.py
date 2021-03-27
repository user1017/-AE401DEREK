# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:37:54 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
import time
time.sleep(5)
x,y,z=mc.player.getTilePos()

mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,11)
    