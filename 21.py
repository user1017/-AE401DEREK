# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:52:22 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

import time
#導入時間
time.sleep(5)

import random

while True:
    x,y,z=mc.player.getPos()
    x=x+random.uniform(-10,10)
    z=z+random.uniform(-10,10)
    y=y+30
    mc.spawnEntity(x,y,z,10)
    time.sleep(0.1)
    