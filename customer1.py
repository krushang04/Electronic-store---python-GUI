# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 00:24:43 2021
 create table add4541(name varchar2(10),itemname varchar2(10),contactno varchar2(15),emailid varchar2(15),quantity varchar2(10),bill varchar2(15));
@author: patelDhruv
create table madd4541(name varchar2(30),itemname varchar2(30),contactno varchar2(16)
                      ,dat varchar2(15),quantity varchar2(10),bill varchar2(15));
"""
from tkinter import *
from tkinter import messagebox
import welcome as wol
import cx_Oracle
con=cx_Oracle.connect("system/kp@localhost")
cur=con.cursor()
class customer:
    def __init__(self,master):
        self.master=master
        self.master.config(bg='white')
        self.boladdd=0
        self.boldisplay=0
        self.bolsearch=0
        self.boladding=0
        self.bolfill=0
        self.bolinsert=0
        self.bolsearching=0
        #self.boldisplay=0
        self.master.title('Customer Data')
        self.f11=Frame(self.master,borderwidth=5,relief=SUNKEN,bg='gray10')
        self.f11.pack(side=LEFT,fill='y')
        self.add=Button(self.f11,text="Add Record",command=self.add1_data,fg='white',bg='black')
        self.add.pack(fill='x')
        self.display=Button(self.f11,text="Display",command=self.display,fg='white',bg='black')
        self.display.pack(fill='x')
        self.search=Button(self.f11,text="Search",command=self.search,fg='white',bg='black')
        self.search.pack(fill='x')
        self.mainmenu=Button(self.f11,text="<< Main Menu",command=self.welcome,fg='white',bg='black')
        self.mainmenu.pack(fill="x")
    def welcome(self):
        self.f11.destroy()
        #print(self.bol)
        if self.boladdd==1:
            self.add_destroy()
        if self.boldisplay==1:
            self.display_destroy()
        if self.bolsearch==1:
               self.search_destroy()
        if self.boladding==1:
            self.adding_destroy()
        if self.bolsearching==1:
            self.searching_destroy()
        #self.close_database()
        self.another5=wol.Welcome(self.master)
    def add1_data(self):
        self.search.configure(state=NORMAL)
        self.display.configure(state=NORMAL)
        self.add.configure(state=DISABLED)
        
        if self.boldisplay==1:
            self.display_destroy()
        if self.bolsearch==1:
               self.search_destroy()
        if self.boladding==1:
            self.adding_destroy()
        if self.bolsearching==1:
            self.searching_destroy()
            
        self.boladdd=1
        self.bolsearch=0
        self.boldisplay=0
        self.boladding=0
        self.bolsearching=0
        
        self.l11=Label(self.master,text='Name',fg='black',bg='white')
        self.l11.place(x=150,y=20)
        self.name=Entry(self.master,width=35)
        self.name.place(x=220,y=20)
        
        self.l12=Label(self.master,text='Item Name ',fg='black',bg='white')
        self.l12.place(x=150,y=50)
        self.Item=Entry(self.master,width=35)
        self.Item.place(x=220,y=50)
        
        self.l13=Label(self.master,text='Contact no',fg='black',bg='white')
        self.l13.place(x=150,y=80)
        self.cntno=Entry(self.master,width=35)
        self.cntno.place(x=220,y=80)
        
        self.l14=Label(self.master,text='Date ',fg='black',bg='white')
        self.l14.place(x=150,y=110)
        self.dat=Entry(self.master,width=35)
        self.dat.place(x=220,y=110)
        
        self.l16=Label(self.master,text='Quantity',fg='black',bg='white')
        self.l16.place(x=150,y=140)
        self.qty=Entry(self.master,width=35)
        self.qty.place(x=220,y=140)
        
        #self.l15=Label(self.master,text='Bill',fg='black')
        #self.l15.place(x=150,y=170)
        
        self.addd=Button(self.master,text='Add',command=self.adding,padx=50)
        self.addd.place(x=275,y=220)
        
        #self.gbill=Button(self.master,text='Generate Bill')
        #self.gbill.place(x=200,y=220)
    def adding(self):
        self.boladding=1
        self.adding_destroy()
        a_namec=self.name.get()
        a_itemc=self.Item.get()
        a_numc=self.cntno.get()
        a_datc=self.dat.get()
        a_quantityc=self.qty.get()
        self.lab2=Label(self.master,fg="red",text="",font="Helvetica 20 bold")
        if not a_itemc or not a_namec or not a_numc  or not a_datc or not a_quantityc :
            self.bolfill=1
            self.lab1=Label(self.master,text="Please fill all the field",fg="red",font="Helvetica 20 bold")
            self.lab1.place(x=175,y=300)   
        else:
            self.bolinsert=1
            bill=self.generate_bill()
            v=self.checkstock()
            if v==1:
                self.update()
                bill=str(bill)
                self.lab2.configure(text="You have to pay Rs "+bill+" ")
                self.lab2.place(x=175,y=300)
                str1="insert into madd4541(name,itemname,contactno,dat,quantity,bill) values('"+a_namec+"','"+a_itemc+"','"+a_numc+"','"+a_datc+"','"+a_quantityc+"','"+bill+"')"
                cur.execute(str1)
                con.commit()
                self.name.delete(0,'end')
                self.Item.delete(0,'end')
                self.cntno.delete(0,'end') 
                self.dat.delete(0,'end')
                self.qty.delete(0,'end')
            elif v==0:
                self.lab2.configure(text="This item is not available in stock")
                self.lab2.place(x=175,y=300)
                self.name.delete(0,'end')
                self.Item.delete(0,'end')
                self.cntno.delete(0,'end') 
                self.dat.delete(0,'end')
                self.qty.delete(0,'end')
            else:
                v=str(v)
                self.lab2.configure(text="Only "+v+" quantity are remaining")
                self.lab2.place(x=175,y=300)
    def generate_bill(self):
        g_itemname=self.Item.get()
        g_quantityc=self.qty.get()
        cur.execute("select * from madd454")
        phenomenon=cur.fetchall()
        price=0
        for i in phenomenon:
            if i[1]==g_itemname:
                price=int(i[4])
        price  =price*int(g_quantityc) 
        return price            
    def print_bill(self):
        a_namec=self.name.get()
        a_itemc=self.Item.get()
        a_numc=self.cntno.get()
        a_datc=self.dat.get()
        a_quantityc=self.qty.get()
        self.print_listbox=Listbox(self.master,height=10,width=70,bg ="grey",fg="yellow",font="courier 11 bold")
        self.print_listbox.insert(1,"Shop name= Electronic Management system")
        self.print_listbox.insert(2," -  - BILL -  -  ")
        self.print_listbox.insert(3,"Name               : "+a_namec+"")
        self.print_listbox.insert(4,"Item purchaed      : "+a_itemc+"")
        self.print_listbox.insert(5,"phone number       : "+a_numc+"")
        self.print_listbox.insert(6,"Date               : "+a_datc+"")
        self.print_listbox.insert(7,"Quantity purchased : "+a_quantityc+"")
        self.print_listbox.place(x=70,y=20)
    def checkstock(self):
        cur.execute("select * from madd454")
        russow=cur.fetchall()
        bool1=0
        c_itemname=self.Item.get()
        c_Quantity=self.qty.get()
        for i in russow:
            if i[1]==c_itemname:
                if int(c_Quantity)<=int(i[3]):
                    bool1=1
                else :
                    bool1=int(i[3])
                break;
        return bool1
    def update(self):
        u_itemname=self.Item.get()
        u_quantityc=self.qty.get()
        old_quant=0
        id1='0'
        cur.execute("select * from madd454")
        undertaker=cur.fetchall()
        for i in undertaker:
            if i[1]==u_itemname:
                old_quant=int(i[3])
                id1=i[0]
                break
        new_quant=old_quant-int(u_quantityc)
        new_quant=str(new_quant)
        stri="update madd454 set quantity='"+new_quant+"' where itemid='"+id1+"'"
        cur.execute(stri)
        con.commit()
        
    def display(self):
        self.search.configure(state=NORMAL)
        self.display.configure(state=DISABLED)
        self.add.configure(state=NORMAL)
        if self.boladdd==1:
            self.add_destroy()
        if self.bolsearch==1:
               self.search_destroy()
        if self.boladding==1:
            self.adding_destroy()
        if self.bolsearching==1:
            self.searching_destroy()
        self.boladdd=0
        self.bolsearch=0
        self.boladding=0
        self.bolsearching=0
        self.boldisplay=1
        self.available_listbox=Listbox(self.master,height=10,width=70,bg ="grey",fg="yellow",font="courier 11 bold")
        self.available_listbox.insert(1,"Name |Itemname       |Number      |Date       |Quantity|Bill     ")
        str3="select * from madd4541"
        cur.execute(str3)
        res1 = cur.fetchall()
        var=2
        for i in res1:
            avail1=i[0].ljust(5)
            avail2=i[1].ljust(15)
            avail3=i[2].ljust(12)
            avail4=i[3].ljust(11)
            avail5=i[4].ljust(8)
            avail6=i[5].ljust(9)
            str=""+avail1+"|"+avail2+"|"+avail3+"|"+avail4+"|"+avail5+"|"+avail6+""
            self.available_listbox.insert(var,str)
            var=var+1
        self.available_listbox.place(x=125,y=100)
    def search(self):
        self.search.configure(state=DISABLED)
        self.display.configure(state=NORMAL)
        self.add.configure(state=NORMAL)
        if self.boladdd==1:
            self.add_destroy()
        if self.boldisplay==1:
            self.display_destroy()
        if self.boladding==1:
            self.adding_destroy()
        if self.bolsearching==1:
            self.searching_destroy()
            
        self.bolsearch=1
        self.boladdd=0
        self.boldisplay=0
        self.boladding=0
        self.bolsearching=0
        
        self.l2=Label(self.master,text='Search by Name : ',fg='black',bg='white')
        self.l2.place(x=150,y=20)
        self.sname=Entry(self.master,width=35)
        self.sname.place(x=270,y=20)
        
        self.searchb=Button(self.master,text='search',command=self.searching)
        self.searchb.place(x=250,y=70)
        
        self.resetb=Button(self.master,text='reset',command=self.search_reset)
        self.resetb.place(x=350,y=70)
    def searching(self):
        self.searchb.configure(state=DISABLED)
        self.sname.configure(state=DISABLED)
        s_search=self.sname.get()
        self.searching_listbox=Listbox(self.master, height = 10,  width = 70, bg = "grey", fg = "yellow",font="courier 11 bold")
        self.bolsearching=1
        if s_search:
            str2="select * from madd4541 where name='"+s_search+"'"
            cur.execute(str2)
            res = cur.fetchall()
            self.searching_listbox.insert(1,"Name |Itemname       |Number      |Date       |Quantity|Bill")
            var=2
            for i in res:
                searc1=i[0].ljust(5)
                searc2=i[1].ljust(15)
                searc3=i[2].ljust(12)
                searc4=i[3].ljust(11)
                searc5=i[4].ljust(8)
                searc6=i[5].ljust(9)
                str=""+searc1+"|"+searc2+"|"+searc3+"|"+searc4+"|"+searc5+"|"+searc6+""
                self.searching_listbox.insert(var,str)
                var=var+1
            self.searching_listbox.place(x=110,y=200)
        else:  
            self.searching_listbox.insert(1,"")
            self.searching_listbox.insert(2,"") 
            self.searching_listbox.insert(3,"                 Enter id in the field") 
            self.searching_listbox.place(x=125,y=200)
    def search_reset(self):
        self.searchb.configure(state=NORMAL)
        self.sname.configure(state=NORMAL)
        self.sname.delete(0,'end')
        if self.bolsearching==1:
            self.searching_listbox.destroy()
        
    def add_destroy(self):
        self.l11.destroy()
        self.l12.destroy()
        self.l13.destroy()
        self.l14.destroy()
        #self.l15.destroy()
        self.l16.destroy()
        self.name.destroy()
        self.Item.destroy()
        self.cntno.destroy()
       # self.bill.destroy()
        self.dat.destroy()
        self.qty.destroy()
        #self.bill.destroy()
        self.addd.destroy()
       # self.gbill.destroy()
       # self.addm.destroy()
       # self.back.destroy()
        
    def display_destroy(self):
        self.available_listbox.destroy()
            
    def search_destroy(self):
        self.l2.destroy()
        self.sname.destroy()
        self.searchb.destroy()
        self.resetb.destroy()
        
    def adding_destroy(self):
        if self.bolfill==1:
            self.lab1.destroy()
        if self.bolinsert==1:
            self.lab2.destroy()
            
    def searching_destroy(self):
          self.searching_listbox.destroy()
    #def close_database(self):
     #   if cur:
      #      cur.close()
       # if con:
        #    con.close()'''
    