from tkinter import *
from tkinter import messagebox
import welcome as wel
from PIL import Image
from PIL import ImageTk

class Login:
    def __init__(self,master):
        
        self.master=master
        self.load=Image.open('E:\\Sem - 4\\PSC\\Innovative Assignment\\gui\\lg.png')
        self.render=ImageTk.PhotoImage(self.load)
        self.img=Label(self.master,image=self.render)
        self.img.place(x=0,y=0)
        
        '''self.logi=Label(self.master,bg ='lightyellow',fg='black',font=("Helvetica",15,"bold"))
        self.logi.place(x = 240,y = 100)'''
        
        self.Usernamel = Label(self.master, bg ='white',fg='black',text ="Username ",font=("Helvetica",10 ))
        self.Usernamel.place(x = 500, y = 180)
 
        self.Username = Entry(self.master, width = 35,bg="white")
        self.Username.place(x = 600, y = 180, width = 100)
  
        self.passwordl= Label(self.master,bg ='white',fg='black', text ="Password ",font=("Helvetica",10))
        self.passwordl.place(x = 500, y = 220)
 
        self.password = Entry(self.master, width = 35,relief=SUNKEN,show="*",bg="white")
        self.password.place(x = 600, y = 220, width = 100)
 
        self.submitbtn = Button(self.master, text ="Login",bg="#c334eb",fg='black',command=self.verify)
        self.submitbtn.place(x = 550, y = 275, width = 80)
        
        
    def verify(self):
        user=self.Username.get()
        pass1=self.password.get()
        
        if user=="admin" and pass1=="123":
            self.login()
        else:
            messagebox.showinfo("logininfo", "Invalid!Username or password") 
            
    def login(self):
        self.submitbtn.destroy()
        #self.logi.destroy()
        self.Usernamel.destroy()
        self.Username.destroy()
        self.passwordl.destroy()
        self.password.destroy()
        self.img.destroy()
        self.another=wel.Welcome(self.master)