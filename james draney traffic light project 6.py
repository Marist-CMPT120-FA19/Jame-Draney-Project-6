#traffic light with functions
#project 6
#lets get it
#lets ball

from graphics import *

win=GraphWin("Traffic Light", 200, 200)

def draw_lamp(color,x,y,radius):
    circ=Circle(Point(x,y),radius)
    circ.setFill(color)
    circ.setOutline("black")
    circ.draw(win)

def draw_light_body(x,y,length,width):
    rect=Rectangle(Point(x,y),Point(length,width))
    rect.setFill("white")
    rect.setOutline("black")
    rect.draw(win)
    

def draw_traffic_light(x,y):
    draw_light_body(15,50,80,200)
    draw_lamp("red",45,75,20)
    draw_lamp("yellow",45,125,20)
    draw_lamp("green",45,175,20)


draw_traffic_light(30,30)

    
