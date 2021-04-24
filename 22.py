# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:08:02 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.createExplosion(x,y,z)