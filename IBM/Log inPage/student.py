from tkinter import*
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
r=Tk()
r.geometry("800x600")
r.config(bg="pink")

#===========function sign in =========
def action():
    if Name.get()=="" or Regno.get()=="" or Dob.get()=="" or Tamil.get()=="" or English.get()=="" or Maths.get()==""  or computer.get()=="" or Socail.get()=="":
        messagebox.showerror("Error","All feilds are reqired")
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="mark")
        cur=con.cursor()
        cur.execute("insert into list(Name,Regno,Dob,Tamil,English,Maths,computer,Socail) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        Name.get(),
                        Regno.get(),
                        Dob.get(),
                        Tamil.get(),
                        English.get(),
                        Maths.get(),
                        computer.get(),
                        Socail.get()
                        ))
        
        con.commit()
        con.close()
        messagebox.showinfo("SUCCESS","successfully saved")

def delete():
    r.destroy()
#_________________function log in ________________
def log():
    if Name.get()=="" or Regno.get()=="":
        messagebox.showerror("error","ENTER VALID DEATILS")
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="mark")
        cur=con.cursor()
        cur.execute("select * from list where Name=%s and Regno=%s",(Name.get(),Regno.get()))
        row=cur.fetchone()

    if row==None:
            messagebox.showerror("Error","Invaliad name and dob")
    else:
            messagebox.showinfo("success","Successfully Log in")
            deshboard()
    con.commit()
    con.close()
                    


#______________________DASHBOARD______________________________________
def deshboard():
    des = Tk()
    des.title("User Panel App")	
    des.maxsize(width=800 ,  height=500)
    des.minsize(width=800 ,  height=500)
    des['bg']='pink'
    heading=Label(des,text= f"STUDENT NAME : {Name.get()}", font="veranda 13 bold")
    heading.place(x=220,y=50)
    con=pymysql.connect(host="localhost",user="root",password="",database="mark")
    cur=con.cursor()
    cur.execute("select * from list where Name='"+ Name.get() + "'")
    row=cur.fetchall()
    for data in row:
        
       uname=Label(des,text=f" Name :{data[0]}",font='veranda 12 bold')
       uname.place(x=50,y=120)

       ureg=Label(des,text=f"Reg No : {data[1]}",font="veranda 12 bold")
       ureg.place(x=50,y=150)

       udeob=Label(des,text=f" DOB  : {data[2]}",font="veranda 12 bold")
       udeob.place(x=50,y=180)

       utamil=Label(des,text=f" TAMIL : {data[3]}",font="veranda 12 bold")
       utamil.place(x=50,y=210)

       uenglish=Label(des,text=f" ENGLISH : {data[4]}",font="veranda 12 bold")
       uenglish.place(x=50,y=240)

       umaths=Label(des,text=f" MATHS : {data[5]}",font="veranda 12 bold")
       umaths.place(x=50,y=270)

       ucomputer=Label(des,text=f" COMPUTER : {data[6]}",font="veranda 12 bold")
       ucomputer.place(x=50,y=300)

       usocail=Label(des,text=f" SOCAIL: {data[7]}",font="veranda 12 bold")
       usocail.place(x=50,y=330)

       
   



    



    
                        
#=================sign in page label============
head=Label(r,text="Student Mark List",font="Arial 20 bold",bg="gray")
head.place(x=250,y=50)

FName=Label(r,text="Name:",font="Arial 12 bold ",bg="pink")
FName.place(x=120,y=140)

FRegno=Label(r,text="Register  No:",font="Arial 12 bold ",bg="pink")
FRegno.place(x=120,y=180)

FDob=Label(r,text="Dob:",font="Arial 12 bold ",bg="pink")
FDob.place(x=120,y=220)

FTamil=Label(r,text="Tamil:",font="Arial 12 bold ",bg="pink")
FTamil.place(x=120,y=260)

FEnglish=Label(r,text="English:",font="Arial 12 bold ",bg="pink")
FEnglish.place(x=120,y=300)

FMaths=Label(r,text="Maths:",font="Arial 12 bold ",bg="pink")
FMaths.place(x=120,y=340)


Fcomputer=Label(r,text="Computer:",font="Arial 12 bold ",bg="pink")
Fcomputer.place(x=120,y=380)

FSocail=Label(r,text="Socail:",font="Arial 12 bold ",bg="pink")
FSocail.place(x=120,y=420)

#=============sign in entry======================
Name=StringVar()
Regno=IntVar()
Dob=IntVar()
Tamil=IntVar()
English=IntVar()
Maths=IntVar()
computer=IntVar()
Socail=IntVar()


name=Entry(r,textvariable=Name)
name.place(x=300,y=140)

regno=Entry(r,textvariable=Regno)
regno.place(x=300,y=180)

dob=Entry(r,textvariable=Dob)
dob.place(x=300,y=220)
          
tamil=Entry(r,textvariable=Tamil)
tamil.place(x=300,y=260)
            
english=Entry(r,textvariable=English)
english.place(x=300,y=300)

maths=Entry(r,textvariable=Maths)
maths.place(x=300,y=340)

computer=Entry(r,textvariable=computer)
computer.place(x=300,y=380)

socail=Entry(r,textvariable=Socail)
socail.place(x=300,y=420)

#===============sign in Btn=========================

btn=Button(r,text="Submit",command=action)
btn.place(x=300,y=450)

btn2=Button(r,text="Switch",command=delete)
btn2.place(x=600,y=30)

r.mainloop()

#================finish sign up==============================================================
from tkinter import*
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
l=Tk()
l.geometry("300x300")
l.config(bg="gray")


lhead=Label(l,text='Stuednt Log In',font="veranda 15 italic")
lhead.place(x=80,y=30)

username=Label(l,text='Name:',font='veranda 12 bold',bg="gray")
username.place(x=50,y=80)


RegNo=Label(l,text='Reg No:',font='veranda 12 bold',bg='gray')
RegNo.place(x=50,y=120)

Name=StringVar()
Regno=IntVar()

En1=Entry(l,textvariable=Name)
En1.place(x=120,y=80)

En2=Entry(l,textvariable=Regno)
En2.place(x=120,y=120)


Btn1=Button(l,text="Log In",command=log)
Btn1.place(x=120,y=180)



l.mainloop()












