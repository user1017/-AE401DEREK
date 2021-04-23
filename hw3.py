# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:53:05 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

n=int(input("要蓋幾*幾的房子"))

mc.setBlocks(x+n,y+n,z+n,x,y,z,155)
mc.setBlocks(x+n-1,y,z+n-1,x+1,y+n-1,z+1,0)
mc.setBlocks(x+1,y,z,x+2,y+3,z,0)
mc.setBlocks(x+1,y+n,z+1,x+n-1,y+n,z+n-1,169)