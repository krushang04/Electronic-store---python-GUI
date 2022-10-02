#create table madd454(itemid varchar2(10),itemname varchar2(20),brand varchar2(10)
#,quantity varchar2(10),priceperquantity varchar2(20));
from tkinter import *
from tkinter import messagebox
import welcome as wol
import cx_Oracle
con=cx_Oracle.connect("system/kp@localhost")
cur=con.cursor()
class Stock:
    def __init__(self,master):
        self.master=master
        self.master.config(bg='white')
        self.boladd=0
        self.boladding=0
        self.bolfill=0
        self.bolinsert=0
        self.bolsearch_data=0
        self.bolsearching=0
        self.bolavailable=0
        self.master.title("Stockdata")
        self.f1=Frame(self.master,borderwidth=5,relief=SUNKEN,bg='gray10')
        self.f1.pack(side=LEFT,fill="y")
        self.add=Button(self.f1,text="Add Item",command=self.add_data,fg='white',bg='black')
        self.add.pack(fill="x")
        self.search=Button(self.f1,text="Search Item",command=self.search_data,fg='white',bg='black')
        self.search.pack(fill="x")
        self.available=Button(self.f1,text="Available Item",command=self.available_data,fg='white',bg='black')
        self.available.pack(fill="x")
        self.mainmenu=Button(self.f1,text="<< Main Menu",command=self.welcome,fg='white',bg='black')
        self.mainmenu.pack(fill="x")
        #self.Itemid1=StringVar()
        #self.search.configure(state=DISABLED)
        #self.available.configure(state=DISABLED)
        #self.add.configure(state=DISABLED)
    def add_data(self):
         #   self.add.config(state=DISABLED)
            self.search.configure(state=NORMAL)
            self.available.configure(state=NORMAL)
            self.add.configure(state=DISABLED)
            self.boladd=1
            if self.bolsearch_data==1:
                self.search_data_destroy()
            if self.bolsearching==1:
                self.searching_destroy()
            if self.boladding==1:
                self.adding_destroy()
            if self.bolavailable==1:
                self.available_destroy()
            self.bolavailable=0
            self.bolsearch_data=0
            self.bolavailable=0
            self.bolsearching=0
            self.l1=Label(self.master,text="ItemId :",fg="black",bg='white')
            self.l1.place(x=150,y=20)
            self.l2=Label(self.master,text="ItemName :",fg="black",bg='white')
            self.l2.place(x=150,y=50)
            self.l3=Label(self.master,text="Brand:",fg="black",bg='white')
            self.l3.place(x=150,y=80)
            #self.l4=Label(self.master,text="Category :",fg="black")
           # self.l4.place(x=150,y=110)
            self.l5=Label(self.master,text="Quantity:",fg="black",bg='white')
            self.l5.place(x=150,y=110)
            self.l6=Label(self.master,text="Price per Quantity:",fg="black",bg='white')
            self.l6.place(x=150,y=140)
            self.Itemid=Entry(self.master,width=35)
            self.Itemid.place(x=300,y=20)
            self.ItemName=Entry(self.master,width=35)
            self.ItemName.place(x=300,y=50)
            self.Brand=Entry(self.master,width=35)
            self.Brand.place(x=300,y=80)
           # self.Category=Entry(self.master,width=35)
           # self.Category.place(x=220,y=110)
            self.Quantity=Entry(self.master,width=35)
            self.Quantity.place(x=300,y=110)
            self.price=Entry(self.master,width=35)
            self.price.place(x=300,y=140)
            self.addb=Button(self.master,width=10,text="Add",command=self.adding)
            self.addb.place(x=200,y=180)
            self.resetb=Button(self.master,width=10,text="Reset",command=self.reset)
            self.resetb.place(x=300,y=180)
           # self.add.config(state=NORMAL)
    def welcome(self):
        self.f1.destroy()
        #print(self.bol)
        if self.boladd==1:
            self.add_destroy()
        if self.boladding==1:
            self.adding_destroy()
        if self.bolsearch_data==1:
               self.search_data_destroy()
        if self.bolavailable==1:
            self.available_destroy()
        if self.bolsearching==1:
            self.searching_destroy()
        #self.close_database()
        self.another1=wol.Welcome(self.master)
    def adding(self):
        #cur.execute("insert")
        a_Itemid1=self.Itemid.get()
        a_ItemName1=self.ItemName.get()
        a_Brand1=self.Brand.get()
        a_Quantity1=self.Quantity.get()
        a_price1=self.price.get()
        self.adding_destroy()
        self.boladding=1
        self.lab2=Label(self.master,fg="red",text="Values inserted successfully",font="Helvetica 20 bold")

        if not a_Itemid1 or not a_ItemName1 or not a_Brand1  or not a_Quantity1:
            self.bolfill=1
            self.lab1=Label(self.master,text="Please fill all the field",fg="red",font="Helvetica 20 bold")
            self.lab1.place(x=175,y=300)   
        else:
            self.bolinsert=1
            if self.check():
                self.update()
                self.lab2.place(x=175,y=220)
                self.Itemid.delete(0,'end')
                self.ItemName.delete(0,'end')
                self.Brand.delete(0,'end') 
                self.Quantity.delete(0,'end')
                self.price.delete(0,'end')
            else:
                str1="insert into madd454 values('"+a_Itemid1+"','"+a_ItemName1+"','"+a_Brand1+"','"+a_Quantity1+"','"+a_price1+"')"
                self.lab2.place(x=175,y=220)
                cur.execute(str1)
                con.commit()
                self.Itemid.delete(0,'end')
                self.ItemName.delete(0,'end')
                self.Brand.delete(0,'end') 
                self.Quantity.delete(0,'end')
                self.price.delete(0,'end')
    def check(self):
        cur.execute("select * from madd454")
        russow=cur.fetchall()
        bool= False
        c_Itemid=self.Itemid.get()
        c_ItemName=self.ItemName.get()
        c_Brand=self.Brand.get()
        c_Quantity=self.Quantity.get()
        for i in russow:
            if i[0]==c_Itemid and i[1]==c_ItemName and i[2]==c_Brand:
                bool=True
                break;
        return bool
    def update(self):
        c_Itemid=self.Itemid.get()
        c_ItemName=self.ItemName.get()
        c_Brand=self.Brand.get()
        c_Quantity=self.Quantity.get()
        cur.execute("select * from madd454")
        undertaker=cur.fetchall()
        old_quant=0
        for i in undertaker:
            if i[0]==c_Itemid and i[1]==c_ItemName and i[2]==c_Brand:
                old_quant=int(i[3])
                break
        new_quant=old_quant + int(c_Quantity)
        new_quant=str(new_quant)
        stri="update madd454 set quantity='"+new_quant+"' where itemid='"+c_Itemid+"'"
        cur.execute(stri)
        con.commit()
        
            
            
    def reset(self):
        self.Itemid.delete(0,'end')
        self.ItemName.delete(0,'end')
        self.Brand.delete(0,'end') 
        self.Quantity.delete(0,'end')
        self.price.delete(0,'end')
    def search_data(self):
        self.search.configure(state=DISABLED)
        self.available.configure(state=NORMAL)
        self.add.configure(state=NORMAL)
        if self.boladd==1:
            self.add_destroy()
        if self.boladding==1:
            self.adding_destroy()
        if self.bolavailable==1:
            self.available_destroy
        if self.bolavailable==1:
            self.available_destroy()
        self.bolavailable=0
        self.boladd=0
        self.boladding=0
        self.bolavailable=0
        self.bolsearch_data=1
        self.sname=Label(self.master,text='Item-Id : ',font=("Helvetica",10,"bold" ),bg='white')
        self.sname.place(x=150,y=80)
        self.sname1=Entry(self.master,width=40)
        self.sname1.place(x=220,y=80)
        self.senter_button=Button(self.master,text="Enter",width=15,command=self.searching)
        self.senter_button.place(x=175,y=130)
        self.sback_button=Button(self.master,text="Reset",width=15,command=self.search_reset)
        self.sback_button.place(x=300,y=130)
    def searching(self):
        self.senter_button.configure(state=DISABLED)
        self.sname1.configure(state=DISABLED)
        self.bolsearching=1
        s_search=self.sname1.get()
        self.searching_listbox=Listbox(self.master, height = 10,  width = 60, bg = "grey", fg = "yellow",font="courier 11 bold")
        if s_search:
            str2="select * from madd454 where itemid='"+s_search+"'"
            cur.execute(str2)
            res = cur.fetchall()
            self.searching_listbox.insert(1,"Id   |Name          |Brand   |Quantity   |Priceperquantity  ")
            var=2
            for i in res:
                searc1=i[0].ljust(5)
                searc2=i[1].ljust(14)
                searc3=i[2].ljust(8)
                searc5=i[3].ljust(11)
                searc6=i[4].ljust(18)
                str=""+searc1+"|"+searc2+"|"+searc3+"|"+searc5+"|"+searc6+""
                self.searching_listbox.insert(var,str)
                var=var+1
            self.searching_listbox.place(x=125,y=200)
        else:  
            self.searching_listbox.insert(1,"")
            self.searching_listbox.insert(2,"") 
            self.searching_listbox.insert(3,"                 Enter id in the field") 
            self.searching_listbox.place(x=125,y=200)
    def available_data(self):
            self.search.configure(state=NORMAL)
            self.available.configure(state=DISABLED)
            self.add.configure(state=NORMAL)
            if self.boladd==1:
                self.add_destroy()
            if self.boladding==1:
                self.adding_destroy()
            if self.bolsearch_data==1:
                self.search_data_destroy()
            if self.bolsearching==1:
                self.searching_destroy()
            self.bolavailable=1
            self.available_listbox=Listbox(self.master,height=10,width=60,bg ="grey",fg="yellow",font="courier 11 bold")
            self.available_listbox.insert(1,"Id   |Name          |Brand   |Quantity   |Priceperquantity  ")

            str3="select * from madd454"
            #cur.execute("delete from add454 where itemid='+itemid1'")
            cur.execute(str3)
            res1 = cur.fetchall()
            var=2
            for i in res1:
                avail1=i[0].ljust(5)
                avail2=i[1].ljust(14)
                avail3=i[2].ljust(8)
                avail5=i[3].ljust(11)
                avail6=i[4].ljust(18)
                str=""+avail1+"|"+avail2+"|"+avail3+"|"+avail5+"|"+avail6+""
                self.available_listbox.insert(var,str)
                var=var+1
            self.available_listbox.place(x=125,y=200)
    def search_reset(self):
        self.senter_button.configure(state=NORMAL)
        self.sname1.configure(state=NORMAL)
        self.sname1.delete(0,'end')
        if self.bolsearching==1:
            self.searching_listbox.destroy()
    def add_destroy(self):
        self.l1.destroy()
        self.l2.destroy()
        self.l3.destroy()
        self.l5.destroy()
        self.l6.destroy()
        self.Itemid.destroy()
        self.ItemName.destroy()
        self.Brand.destroy()
        self.Quantity.destroy()
        self.price.destroy()
        self.addb.destroy()
        self.resetb.destroy()
    def search_data_destroy(self): 
        self.sname.destroy()
        self.sname1.destroy()
        self.senter_button.destroy()
        self.sback_button.destroy()
    def adding_destroy(self):
        if self.bolfill==1:
            self.lab1.destroy()
            self.bolfill=0
        if self.bolinsert==1:
            self.lab2.destroy()
            self.bolinsert=0
    def searching_destroy(self):
        self.searching_listbox.destroy()
    def available_destroy(self):
        self.available_listbox.destroy()
   #def close_database(self):
    #    if cur:
     #       cur.close()
      #  if con:
       #     con.close()'''

