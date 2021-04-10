# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:11:20 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    time.sleep(30)
