# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:07:08 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

try:
    blockType=int(input("id:"))
    mc.setBlock(x,y,z,blockType)
except:
    mc.postToChat("只能輸入數字")
    