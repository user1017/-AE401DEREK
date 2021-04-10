# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:02:03 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

a=0
while a<20:
    mc.setBlocks(x+30,y-1,z,x-30,y-10,z,19)
    z=z-5
    a=a+1