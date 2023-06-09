#!python3

# Find an image to use as a sprite from the Internet.
# Modify the image (flipping horizontally is a quick way to do that) so that you have
# a second, different image. Use the tkObject.after() method to animate it.
# Note: You can find sprite sheets or tile sheets on the internet to help you!
import tkinter as tk
from PIL import Image,ImageTk

x=0
y=0

w = tk.Tk()
w.attributes("-topmost",True)
w.geometry("1000x1000")

c = tk.Canvas(width=380,height=280)
c.pack()
i=0
#840*283
def getSprite(x,y): 
    img = Image.open("assets/sprite1.png").convert("RGBA")
    xi = x*105
    yi = y*141.5
    img2 = img.crop([xi,yi,xi+105,yi+141.5])
    return ImageTk.PhotoImage(img2)

def spriteUp():
    global i
    i+=1
    i%=len(spri)
    c.itemconfig(img,image=spri[i])
    w.after(200,spriteUp)
image = tk.PhotoImage(file="assets/sprite1.png")

spri=[]
for i in range(7):
    firstX = i + 8*x
    spri.append(getSprite(firstX,y))
spri.append(getSprite(firstX + 1,y))

img = c.create_image(105,141.5,image=spri[0])
w.after(200,spriteUp())

w.mainloop()















"""import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()"""






"""rec = c.create_rectangle(50,50,80,80,fill="#aa0000")


def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)"""


w.mainloop()