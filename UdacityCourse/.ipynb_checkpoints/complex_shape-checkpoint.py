# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 15:44:18 2017

@author: Felix
"""

import turtle


def create_square(some_turtle):  
    for i in range(1, 5):    
        some_turtle.forward(100)
        some_turtle.right(90)

    
def create_art():
    
    turtle.bgcolor("red")
    
    adam = turtle.Turtle()  # create/initiates computer memory that did not exisit before - 
                            # alling the init FUNCTION in the CLASS Turtle():
    
    adam.shape("turtle")
    adam.color("green")
    adam.speed(15)

    for i in range(1, 37):
        create_square(adam)
        adam.right(10)
        
    turtle.exitonclick()
               
create_art()