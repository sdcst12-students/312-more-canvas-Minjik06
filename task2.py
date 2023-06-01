import tkinter as tk
from PIL import ImageTk,Image
import numpy as np
import array
import os
import csv
import pandas as pd

"""
Task 2
Read the map2.txt file and convert to a map that you can navigate a
rectangle object through. Use images for your map.
You will want to make sure that your rectangle is above the map tiles
Legend:
0 Water
1 Plains
2 Forest
3 Hills
4 Mountains
5 Swamp
6 City
"""
w = tk.Tk()
w.geometry("925x1500")
w.attributes('-topmost',True)
c = tk.Canvas(height=925,width=1500,bg="#ffdddd")
c.pack()
f = open('map2.txt')



csv_filename = 'map2.txt'
with open(csv_filename) as f:
    reader = csv.reader(f)
    lst = list(reader)
    print(lst)
    for i in range(len(lst)):
        print(i,lst[i])
#map2 = np.loadtxt('map2.txt', skiprows=1, delimiter=',')
#map2=np.genfromtxt("map2.txt", dtype="int")
#print(map2)

img1 = tk.PhotoImage(file="assets/map.plains.png")
img2 = tk.PhotoImage(file="assets/map.forest.png")
img3 = tk.PhotoImage(file="assets/map.hills.png")
img4 = tk.PhotoImage(file="assets/map.mountain.png")
img5 = tk.PhotoImage(file="assets/map.swamp.png")
img6 = tk.PhotoImage(file="assets/map.city.png")

def getImage(x,y):
    img0 = Image.open("assets/map.water.png").convert("RGBA")
    img1 = Image.open("assets/map.plains.png").convert("RGBA")
    img2 = Image.open("assets/map.forest.png").convert("RGBA")
    img3 = Image.open("assets/map.hills.png").convert("RGBA")
    img4 = Image.open("assets/map.mountain.png").convert("RGBA")
    img5 = Image.open("assets/map.swamp.png").convert("RGBA")
    img6 = Image.open("assets/map.city.png").convert("RGBA")
    print(x,y)
    if lst[x][y]=='0':
        return ImageTk.PhotoImage(img0)
    if lst[x][y]=='1':
        return ImageTk.PhotoImage(img1)
    if lst[x][y]=='2':
        return ImageTk.PhotoImage(img2)
    if lst[x][y]=='3':
        return ImageTk.PhotoImage(img3)
    if lst[x][y]=='4':
        return ImageTk.PhotoImage(img4)
    if lst[x][y]=='5':
        return ImageTk.PhotoImage(img5)
    if lst[x][y]=='6':
        return ImageTk.PhotoImage(img6)


map = []
walls = []
img = []
j=0
i=0
print(len(lst))
for j in range(len(lst)):
    for i in range(len(lst[j])):
        if j == 0:
            print(i,j,lst[j])
        img.append(getImage(j,i))
        walls.append(c.create_image(i*30+32,j*30+32,image=img[-1]))

       

w.mainloop()