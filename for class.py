# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 11:29:54 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

while True:
    hits = mc.events.pollProjectileHits()
    if len(hits)>0:
        hit = hits[0]
        x = hit.pos.x
        y = hit.pos.y
        z = hit.pos.z
        mc.spawnEntity(x,y,z,50)