# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:53:40 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

blockType = int(input("要放的方塊id:"))
mc.setBlock(x,y,z,blockType)