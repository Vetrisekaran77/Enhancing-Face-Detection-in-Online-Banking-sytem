from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
r=Tk()
r.geometry("300x300")
r.config(bg="skyblue")


#=================1st page Button==============


Btn1=Button(r,text="Admin",font="veranda 12 ",bg="gray",fg="black")
Btn1.place(x=100,y=50)

btn2=Button(r,text="User",font="veranda 12 ",bg="gray",fg="black")
btn2.place(x=105,y=100)
def exit():
    r.destroy()

btn3=Button(r,text="Exit",font="veranda 12 ",bg="gray",fg="black",command=exit)
btn3.place(x=110,y=150)
r.mainloop()
#___________________________________________________________________________________
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
u=Tk()
u.geometry("500x500")
u.config(bg="Teal")

def submit():
    if name.get()=="" or dob.get()=="" or number.get()=="" or add.get()=="" or mail.get()=="":
        messagebox.showerror("Error","All fields Are Required")
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="testing")
        cur=con.cursor()
        cur.execute("insert into deatil (name,dob,number,add,mail)values (%s,%s,%s,%s,%s)",
                    (
                        name.get(),
                        dob.get(),
                        number.get(),
                        add.get(),
                        mail.get()
                        ))
        con.commit()
        con.close()
        messagebox.showinfo("DONE","Successfully saved")




    

#====================label and entry==========

name=Label(u,text="Name:",font="veranda 12 ")
name.place(x=100,y=80)

dob=Label(u,text="DOB:",font="veranda 12 ")
dob.place(x=100,y=120)


number=Label(u,text="Contact:",font="veranda 12 ")
number.place(x=100,y=160)

add=Label(u,text="Address:",font="veranda 12 ")
add.place(x=100,y=200)


mail=Label(u,text="Mail:",font="veranda 12 ")
mail.place(x=100,y=240)

name=StringVar()
dob=IntVar()
number=IntVar()
add=StringVar()
mail=StringVar()

En1=Entry(u,textvariable=name)
En1.place(x=170,y=80)

En2=Entry(u,textvariable=dob)
En2.place(x=170,y=120)

En3=Entry(u,textvariable=number)
En3.place(x=170,y=160)

En4=Entry(u,textvariable=add)
En4.place(x=170,y=200)

En5=Entry(u,textvariable=mail)
En5.place(x=170,y=240)


btn4=Button(u,text="Submit",command=submit)
btn4.place(x=150,y=280)

u.mainloop()





