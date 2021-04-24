# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:05:24 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        mc.postToChat("恭喜獵到"+str(block))
        