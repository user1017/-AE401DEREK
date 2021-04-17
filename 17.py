# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:07:33 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()
#魔法棒
import time
#導入時間
time.sleep(5)
#時間延遲5秒
x,y,z=mc.player.getTilePos()
#得到玩家位置
mc.setBlocks(x+10,y,z+10,x,y+10,z,155)
#建立方塊46 50*50*50
mc.setBlocks(x+10-1,y,z+10-1,x+1,y+9,z+1,0)
mc.setBlocks(x+1,y,z,x+2,y+3,z,0)
mc.setBlocks(x+1,y+10,z+1,x+9,y+10,z+9,169)
mc.setBlocks(x+1,y+5,z+1,x+9,y+5,z+9,169)
mc.setBlocks(x+9-1,y+5,z+9-1,x+2,y+5,z+2,0)