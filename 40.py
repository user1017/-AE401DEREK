# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:04:44 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

from random import choice

mineral=[14,15,16,56,73,129]

r = choice(mineral)

myID = mc.getPlayerEntityId("user1017")
x,y,z=mc.entity.getTilePos(myID)

mc.setBlock(x,y,z,r)