# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:21:17 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

list2d = [[12,41,14],[35,73,86]]


myId = mc.getPlayerEntityId("user1017")
x,y,z = mc.entity.getTilePos(myID)

startX = x

for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        x=x+1
    x=startX
    z=z+1