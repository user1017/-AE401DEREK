# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:58:28 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

from time import sleep

while True:
    mc.executeCommand("time add 50")
    time.sleep(0.05)