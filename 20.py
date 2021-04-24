# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:32:52 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getPos()
mc.setSign(x,y,z,68,15,"哈囉")
