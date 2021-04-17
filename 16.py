# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:38:43 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

userName=input("輸入玩家名子")
message=input("message")
mc.postToChat("["+userName+"]"+message)