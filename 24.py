# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:37:22 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getPos()

mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
mc.setBlocks(x,y,z,x,y+4,z,17)