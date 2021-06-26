# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 11:29:46 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

while True:
    chat = mc.events.pollChatPosts()
    
    if len (chat) >0:
        mc.postToChat(chat[0])
        
        strChat = str(chat[0])
        
        lenth = len(strChat)
        
        comma1 = strChat.find(",",0)
        
        comma2 = strChat.find(",",comma1+1)
        
        senderID = strChat[comma1+1:comma2]
        
        senderID = int (senderID)
        
        message = strChat[comma2+1+1:lenth-1]
        
        playerName = mc.entity.getName(senderID)
        
        x,y,z = mc.entity.getTilePos(senderID)
        
        mc.setSign(x,y,z,63,0,playerName,"",message)