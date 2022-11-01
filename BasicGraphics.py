from tkinter import *
from IsoCam import IsoCam
from time import time, sleep
import math

root = Tk()
cam = IsoCam()
canvas = Canvas(root, bg="white", height=300, width=300)
canvas.pack()
drawn = []
def draw_cube():
    global drawn
    for line in drawn:
        canvas.delete(line)
    drawn = []
    for x in (-1, 1):
        for y in (-1, 1):
            p1 = cam.point_on_screen([x, y, -1])
            p2 = cam.point_on_screen([x, y, 1])
            drawn.append(canvas.create_line(p1.item(0)*50+150,p1.item(1)*50+150,p2.item(0)*50+150,p2.item(1)*50+150))
        for z in (-1, 1):
            p1 = cam.point_on_screen([x, -1, z])
            p2 = cam.point_on_screen([x, 1, z])
            drawn.append(canvas.create_line(p1.item(0)*50+150,p1.item(1)*50+150,p2.item(0)*50+150,p2.item(1)*50+150))
    for y in (-1, 1):
        for z in (-1, 1):
            p1 = cam.point_on_screen([-1, y, z])
            p2 = cam.point_on_screen([1, y, z])
            drawn.append(canvas.create_line(p1.item(0)*50+150,p1.item(1)*50+150,p2.item(0)*50+150,p2.item(1)*50+150))

    #old = canvas.create_line(p1.item(0)*10+150, p1.item(1)*10+150, p2.item(0)*10+150, p2.item(1)*10+150)
lastTime = time()
frames = 0
while True:
    cam.yaw = time()%math.tau
    cam.pitch = -time()*13/23%math.tau
    cam.roll = time()*7/13%math.tau
    cam.map_rotation()
    draw_cube()
    root.update()
