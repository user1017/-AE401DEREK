# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:26:31 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

from random import choice

cards_symbol = ["梅花","方塊","愛心","黑桃"]
cards_number = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K",]
py1_card=[]
py2_card=[]

def Player1(status):
    if status =="not ok":
        print("get ready")
    elif status == "ok":
        print("ok")
    else:
        print("error: try again")
        
Player1(input("Please enter your ststus(ok or not ok):"))
       
for i in range(1,5):
    card_cmbine = [choice(cards_symbol)+choice(cards_number)]
    py1_card.append(card_cmbine)
    
print(py1_card)

mc.setSign(x,y,z,63,0,"player1's card",py1_card[0],py1_card[1],py1_card[2])



def Player2(status):
    if status =="not ok":
        print("get ready")
    elif status == "ok":
        print("ok")
    else:
        print("error: try again")
        
Player2(input("Please enter your ststus(ok or not ok):"))
       
for i in range(1,5):
    card_cmbine = [choice(cards_symbol)+choice(cards_number)]
    py2_card.append(card_cmbine)
    
print(py2_card)

mc.setSign(x,y,z,63,0,"player2's card",py2_card[0],py2_card[1],py2_card[2])
