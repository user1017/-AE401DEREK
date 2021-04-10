# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:22:54 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()


while True:
    x,y,z=mc.player.getPos()
    a = mc.getBlock(x,y-1,z+1)
    b = mc.getBlock(x,y-1,z-1)
    c = mc.getBlock(x-1,y-1,z)
    d = mc.getBlock(x+1,y-1,z)
    if a==2 or b==2 or c==2 or d==2:
        mc.setBlock(x,y,z,38)
    