import tkinter as tk
from typing import Text
import numpy as np
import csv
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("1000x1000")
w.attributes('-topmost',True)
c = tk.Canvas(height=1500,width=1500,bg="#ffdddd")
c.pack()
f=open('map1')
map1=f.readlines

for i in range(1,15):
    for fd
#c.create_rectangle(300,300,320,340, fill='white')


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
