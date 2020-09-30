#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pretty turtles
"""


from turtle import *
import random

colormode(255)
 
panel = Screen()
w = 750
h = 750
panel.setup(width=w, height=h)
pencolor('black')

pendown()
VAR = 2

if 0 == VAR % 2:
    purple = Turtle()
    color ("purple")
    down ()
    
    purple. goto(-70, -90)
    right(20)
    
    up()
    
if 1 == VAR % 2:
    yellow = Turtle()
    color ([255,255,0])
    goto(94, 86)
    down ()
    left (20)
    
    #dot(200)
    #backward(20)
    #up()
    
    yellow. goto(-230, 63)
    
    down()
    forward(20)
        