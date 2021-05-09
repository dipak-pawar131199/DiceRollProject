# import modules

from tkinter import *
from random import *
from PIL import ImageTk,Image
from os import *

root=Tk()
# create canvas object on root window
canvas = Canvas(root, width=300, height=300,bg='red')
canvas.pack()
rl=[] # empty list to store img objects
img=PhotoImage(file='Image/empty.png')
rl.append(img) # add img object into list
img=PhotoImage(file='Image/one.png')
rl.append(img)
img=PhotoImage(file='Image/two.png')
rl.append(img)
img=PhotoImage(file='Image/three.png')
rl.append(img)
img=PhotoImage(file='Image/four.png')
rl.append(img)
img=PhotoImage(file='Image/five.png')
rl.append(img)
img=PhotoImage(file='Image/six.png')
rl.append(img)
#print (rl)

canvas.create_image(55,50, anchor=NW, image=rl[0])
def rolldice():
        ''' Funtion to rolldice '''
           
        r=randint(1,6) # create random number 1 to 6
        canvas.create_image(55,50, anchor=NW, image=rl[r])

    
button=Button(root,text="CLICK",command=rolldice,bg='green')
button.pack()

root.title("Welcome to rolling dice")
root.geometry('400x340')
mainloop()