# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:55:48 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
x=123
y=456
z=789
mc.player.setTilePos(x,y,z)

