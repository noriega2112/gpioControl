# Developer: Norman A. Cubilla
from Tkinter import *
from ttk import *
import tkFont
import tkMessageBox
import os
import time

v1=Tk()
v1.title("SCADA SYSTEM")
v1.geometry("800x400+0+0")

#------------------------------- Sensor-Mill ----------------------------------$
bgtext1=tkFont.Font(family="Helvetica",size=16)
label1=Label(v1,text="SENSOR-MILL",font=bgtext1).place(x=450,y=50)
img_on1=PhotoImage(file="on.gif")
button_sensor1on=Button(v1,image=img_on1).place(x=400,y=90)
img_off1=PhotoImage(file="off.gif")
button_sensoroff=Button(v1,image=img_off1).place(x=500,y=90)

#scada_update()
img_on=PhotoImage(file="on2.gif")
img_off=PhotoImage(file="off2.gif")

def update():
             pf=open("/home/pi/status.txt","r")
             for line in pf:
                            fields=line.split("\n")
                            field1=fields[0]
                            #field2=fields[1]
                            #field3=fields[2]
                            print(field1)
             
                            if (field1=="1"):
                                             button_on=Button(v1,image=img_on).place(x=80,y=100)
                                             current=time.strftime("%H:%M:%S")
                                             labelTiempo=Label(v1,text=" -- Tiempo new--").place(x=120,y=230)
                                             labeltime=Label(v1,text=current).place(x=120,y=250)
                                             v1.after(1000,update)
                            if (field1=="0"):
                                             button_on=Button(v1,image=img_off).place(x=80,y=100)
                                             current=time.strftime("%H:%M:%S")
                                             labelTiempo=Label(v1,text=" -- Tiempo new--").place(x=120,y=230)
                                             labeltime=Label(v1,text=current).place(x=120,y=250)
                                             v1.after(1000,update)                   
update()


v1.mainloop()
