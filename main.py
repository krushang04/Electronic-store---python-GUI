from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import cx_Oracle
import login as log
con=cx_Oracle.connect("system/kp@localhost")
cur=con.cursor()
root=Tk()
root.geometry('800x600')
root.title("Login Page")
'''load=Image.open('E:\\Sem - 4\\PSC\\Innovative Assignment\\gui\\bg11.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)'''
run=log.Login(root)

root.mainloop()
if cur:
    cur.close()
if con:
    con.close()