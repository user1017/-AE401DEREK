# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:45:07 2021

@author: Derek
"""
from mcpi.minecraft import Minecraft
mc= Minecraft.create()


line1=[]
line2=[]
line3=[]

for i in range(1,4):
    line1.append(1*i)
    
for i in range(1,4):
    line2.append(2*i)
    
for i in range(1,4):
    line3.append(3*i)
    
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))
    