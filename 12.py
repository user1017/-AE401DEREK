# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:38:01 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

import time

while True:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)