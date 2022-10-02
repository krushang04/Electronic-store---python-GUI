from tkinter import *
from tkinter import messagebox
import stock_data as st
import customer1 as cus
from PIL import Image
from PIL import ImageTk
class Welcome:
    def __init__(self,master):
        self.master=master
        self.master.title("Welcome Page")
        self.load=Image.open('E:\\Sem - 4\\PSC\\Innovative Assignment\\gui\\stk.png')
        self.render=ImageTk.PhotoImage(self.load)
        self.img=Label(self.master,image=self.render)
        self.img.place(x=0,y=0)
        '''self.f1=Frame(self.master,borderwidth=5,relief=SUNKEN,bg="skyblue")
        self.f1.pack(side=TOP,fill="x")
        self.n=Label(self.f1,text="Welcome",fg="black",bg="skyblue",padx=20,pady=20,font=("calibri",15,"bold"),borderwidth=3)
        self.n.pack()'''
        #f2=Frame(new,borderwidth=5,relief=SUNKEN)
        #f2.pack(side=,fill="x")
        self.t=Label(self.master,text='Electronic Store Data Management & Customer Record',font=("calibri",20,"bold"),bg='white')
        self.t.place(x=125,y=200)
        self.stock=Button(self.master,text="Stock Data",bd='5',padx=30,pady=20,command=self.Stock,font=("calibri",15,"bold"),bg='white')
        self.stock.place(x=200,y=300)
        self.customer=Button(self.master,text="Customer Data",bd='5',padx=20,pady=20,command=self.Customer,font=("calibri",15,"bold"),bg='white')
        self.customer.place(x=400,y=300)
        
        
    def Stock(self):
        #self.f1.destroy()
        self.t.destroy()
        self.stock.destroy()
        self.customer.destroy()
        self.img.destroy()
        self.another2=st.Stock(self.master)
        

    def Customer(self):
        #self.f1.destroy()
        self.t.destroy()
        self.stock.destroy()
        self.customer.destroy()
        self.img.destroy()
        self.another3=cus.customer(self.master)