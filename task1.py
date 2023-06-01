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
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()


csv_filename = 'map1.txt'
with open(csv_filename) as f:
    reader = csv.reader(f)
    lst = list(reader)
    print(lst)
    for i in range(len(lst)):
        print(i,lst[i])


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