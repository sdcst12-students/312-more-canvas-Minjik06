import tkinter as tk
from typing import Text
import numpy as np
import csv
from PIL import ImageTk,Image
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("950x530")
w.attributes('-topmost',True)
c = tk.Canvas(height=530,width=950,bg="#ffdddd")
c.pack()
f=open('map1.txt')
map1=f.readlines()


"""def getImage(x,y):
    img = Image.open("assets/map.swamp.png").convert("RGBA")
    xi = x*64
    yi = y*64
    img2 = img.crop([xi,yi,xi+64,yi+64])
    return ImageTk.PhotoImage(img2)"""

walls=[]
img = [[]]
k=0
p=0
for i in range(1,2):
    for i in range(len(map1)):
        print(map1[i])
        p=0
        k+=30
        for j in range(len(map1[i])):
            p+=30
            if map1[i][j]=="*":
                print(f"map1: {j},{i}")
                c.create_rectangle(j+p,i+k,j+p+30,i+k+30, fill='green')
            
    
#c.create_rectangle(i+p,10+j+k,i+p+5,10+j+k+5, fill='green')
#c.create_rectangle(300,300,320,340, fill='white')
"""
for i in range(1,2):
    for i in range(len(map1)):
        print(map1[i])
        k=0
        p+=10
        for j in range(len(map1[i])):
            if map1[i][j]=="*":
                print(f"map1: {j},{i}")
                
                k+=20
"""
"""i=i+k
            j=j+k
            c.create_rectangle(i,j,i+5,j+5, fill='white')
            k*7"""
#c.create_rectangle(i*i,j*j,i*i+5,j*j+5, fill='white')
"""sv_filename = 'map1.txt'
with open(csv_filename) as f:
    reader = csv.reader(f)
    lst = list(reader)
    print(lst)
    for i in range(len(lst)):
        print(i,lst[i])

lis=""
for i in range(15):
    lis = f"{lis}\n{lst[i][0]}"
print(lis)"""


#c.create_text(400, 100, text=lis, fill="black",font=('Helvetica 45 bold'))
#c.pack()



w.mainloop()



#or i in range(29):



"""f = open('map1.txt')
f=f.readlines()
print(f)

k=[15][29]

for i in range(15):
    for j in range(29):
        f[i]=str(f[i])
        f[i].__len__(j) = k[i][j]
print(k)

w.mainloop()"""
