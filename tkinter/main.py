from tkinter import *

w=Tk()

w.geometry('500x350')

w.title('windows')

w.resizable(0,0)

j=0
r=200

for i in range(5):
    c=str(224499+r)
    Frame(w, width=100, height=350, bg="#"+c).place(x=j,y=0)
    j=j+100

    r=r+1000

w.mainloop()
