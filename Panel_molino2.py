from Tkinter import*
from ttk import*
import tkFont
import tkMessageBox
import os
import subprocess
import time
v1=Tk()
v1.geometry("600x530+400+0")
v1.title("Examen final")


def save():

         tab=StringVar()
         hi=horai.get()
         mi=mini.get()
         hf=horaf.get()
         mf=minf.get()
         dia="*"
         mes="*"
         ano="*"
         tab=" "
         user="root"

         path="/home/pi/motoron.sh"
         path2="/home/pi/motoroff.sh"
         cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path))
         print(str(cadena))

         #tkMessageBox.showinfo("Save",message="Horario Programado con Exito")
         os.system("sudo chmod -R 777 /etc/cron.d/tarea") 
         pf=open(r'/etc/cron.d/tarea','w') 
         pf.write(cadena) 
         pf.write("\n") 
         pf.close() 
         cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2)) 
         print(str(cadena2)) 
         os.system("sudo chmod -R 777 /etc/cron.d/tarea2") 
         pf2=open(r'/etc/cron.d/tarea2','w') 
         pf2.write(cadena2) 
         pf2.write("\n") 
         pf2.close()
         os.system("sudo chmod -R 755 /etc/cron.d/tarea")
         os.system("sudo chmod -R 755 /etc/cron.d/tarea2")
         os.system("sudo /etc/init.d/cron restart")

def toplevel():
    global horai
    global horaf
    global mini
    global minf
    v1=Toplevel()
    v1.title("Configurar Horarios")
    v1.geometry("450x300+550+0")
    mini=StringVar()
    minf=StringVar()
    horai=StringVar()
    horaf=StringVar()
    texttop=tkFont.Font(family="Helvetica",size=10,weight="bold")
    texttop2=tkFont.Font(family="Helvetica",size=9,weight="bold")
    label1top=Label(v1,text="HORARIO DE ACTIVACION & DESACTIVACION",font=texttop).place(x=50,y=10)
    label2top=Label(v1,text="HORA INICIAL :",font=texttop2).place(x=110,y=70)
    caja2=Entry(v1,textvariable=horai,width=20).place(x=215,y=70)
    label3top=Label(v1,text="MINUTO INICIAL :",font=texttop2).place(x=110,y=110)
    TextBox2=Entry(v1,textvariable=mini,width=20).place(x=215,y=110)
    label4top=Label(v1,text="HORA FINAL :",font=texttop2).place(x=110,y=150)
    TextBox3=Entry(v1,textvariable=horaf,width=20).place(x=215,y=150)
    label5top=Label(v1,text="MINUTO FINAL :",font=texttop2).place(x=110,y=190)
    TextBox4=Entry(v1,textvariable=minf,width=20).place(x=215,y=190)
    # Boton Guardar
    imgsave=PhotoImage(file="save.png")
    botosettings=Button(v1,image=imgsave,command=save,width=50).place(x=215,y=220,height=50)
    # Boton Salir 
    botonclose=Button(v1,text="Salir",command=v1.destroy).place (x=295,y=220,height=50)
    # Reloj Time
    def update():
           current=time.strftime("%H:%M:%S")
           labelTiempo=Label(v1,text=" -- Tiempo --").place(x=110,y=230)
           labeltime=Label(v1,text=current).place(x=120,y=250)
           v1.after(1000,update)
    update()     
    v1.mainloop()



######## sensor 1 ########

def save2():

         tab=StringVar()
         hi=horai.get()
         mi=mini.get()
         hf=horaf.get()
         mf=minf.get()
         dia="*"
         mes="*"
         ano="*"
         tab=" "
         user="root"

         path="/home/pi/sensor1on.sh"
         path2="/home/pi/sensor1off.sh"
         cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path))
         print(str(cadena))

         tkMessageBox.showinfo("Save",message="Horario Programado con Exito")
         os.system("sudo chmod -R 777 /etc/cron.d/sensor1on")
         pf=open(r'/etc/cron.d/sensor1on','w')
         pf.write(cadena)
         pf.write("\n")
         pf.close()
         cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
         print(str(cadena2))
         os.system("sudo chmod -R 777 /etc/cron.d/sensor1off")
         pf2=open(r'/etc/cron.d/sensor1off','w')
         pf2.write(cadena2)
         pf2.write("\n")
         pf2.close()
         os.system("sudo chmod -R 755 /etc/cron.d/sensor1on")
         os.system("sudo chmod -R 755 /etc/cron.d/sensor1off")
         os.system("sudo /etc/init.d/cron restart")

def toplevel2():
    # Las variables Globales siempre deben de declarse al inicio de cada metodo o funcion
    # Para que no generen advertencias o warning ejemplo:syntaxwarning name is assigned to before global declaration
    global horai
    global horaf
    global mini
    global minf
    v1=Toplevel()
    v1.title("Configurar Horarios")
    v1.geometry("450x300+200+200")
    mini=StringVar()
    minf=StringVar()
    horai=StringVar()
    horaf=StringVar()
    # Declarar Variables Globales para ser usadas dentro de cualquier funcion o metodo
    texttop=tkFont.Font(family="Helvetica",size=10,weight="bold")
    texttop2=tkFont.Font(family="Helvetica",size=9,weight="bold")
    label1top=Label(v1,text="HORARIO DE ACTIVACION & DESACTIVACION DE AULA 1",font=texttop).place(x=50,y=10)
    label2top=Label(v1,text="HORA INICIAL :",font=texttop2).place(x=110,y=70)
    caja2=Entry(v1,textvariable=horai,width=20).place(x=215,y=70)
    label3top=Label(v1,text="MINUTO INICIAL :",font=texttop2).place(x=110,y=110)
    TextBox2=Entry(v1,textvariable=mini,width=20).place(x=215,y=110)
    label4top=Label(v1,text="HORA FINAL :",font=texttop2).place(x=110,y=150)
    TextBox3=Entry(v1,textvariable=horaf,width=20).place(x=215,y=150)
    label5top=Label(v1,text="MINUTO FINAL :",font=texttop2).place(x=110,y=190)
    TextBox4=Entry(v1,textvariable=minf,width=20).place(x=215,y=190)
    # Boton Guardar
    imgsave=PhotoImage(file="save.png")
    botosettings=Button(v1,image=imgsave,command=save2,width=50).place(x=215,y=220,height=50)
    # Boton Salir 
    botonclose=Button(v1,text="Salir",command=v1.destroy).place (x=295,y=220,height=50)
    # Reloj Time
    def update():
           current=time.strftime("%H:%M:%S")
           labelTiempo=Label(v1,text=" -- Tiempo --").place(x=110,y=230)
           labeltime=Label(v1,text=current).place(x=120,y=250)
           v1.after(1000,update)
    update()     
    v1.mainloop()

    

def on(gpio):
         x = 350
         if gpio == 17:
            y = 90
         elif gpio == 21:
            y = 220
         elif gpio == 27:
            y = 350
         text_d1=tkFont.Font(family="Helvetica",size=10)
         label_d1=Label(v1,text="-- ON --",font=text_d1).place(x=x,y=y)
         os.system("sudo /home/pi/Desktop/lenguajes/on"+str(gpio)+".sh &")
         print(gpio)
def off(gpio):
          text_d2=tkFont.Font(family="Helvetica",size=10)
          x = 350
          if gpio == 17:
              y = 90
          elif gpio == 21:
              y = 220
          elif gpio == 27:
              y = 350
          label_d2=Label(v1,text="-- OFF --",font=text_d2).place(x=x,y=y)
          os.system("sudo /home/pi/Desktop/lenguajes/off"+str(gpio)+".sh &")     

def time():
             text_t4=tkFont.Font(family="Helvetica",size=10)
             label_t4=Label(v1,text="-- Time --",font=text_t4).place(x=350,y=450)
                 
               
title_text=tkFont.Font(family="Helvetica",size=15,weight="bold")

label50=Label(v1,text="Encendido y apagado GPIOS",font=title_text).place(x=75,y=10)
############################### Asignar imagenes a Raspi ######################################
bgtext1 = tkFont.Font(family="Helvetica",size=12,weight="bold")
# Posicion de los botones
text = 170
x1 = 50
x2 = 150
x3 = 250 
# declaracion imagenes
img_on=PhotoImage(file="off.png")
img_off=PhotoImage(file="on.png")
img_settings=PhotoImage(file="settings.png")
#------------------------------- GPIO 17 -----------------------------------------------
label1=Label(v1,text="PIN - 17",font=bgtext1).place(x=text,y=50)
button_sensor1on=Button(v1,image=img_on,command=lambda: on(17)).place(x=x1,y=90,width=90,height=80)
button_sensoroff=Button(v1,image=img_off,command=lambda: off(17)).place(x=x2,y=90,width=90,height=80)
button_settings=Button(v1,image=img_settings,command=toplevel2).place(x=x3,y=90,width=90,height=80)

# --------------------------------GPIO 21 ------------------------------------------------
label2=Label(v1,text="PIN - 21",font=bgtext1).place(x=text,y=190)

button_sensor2on=Button(v1,image=img_on,command=lambda: on(21)).place(x=x1,y=220,width=90,height=80)

button_sensoroff2=Button(v1,image=img_off,command=lambda: off(21)).place(x=x2,y=220,width=90,height=80)

button_settings2=Button(v1,image=img_settings,command=toplevel2).place(x=x3,y=220,width=90,height=80)

# --------------------------------GPIO 27 ------------------------------------------
label3=Label(v1,text="PIN - 27",font=bgtext1).place(x=text,y=320)

button_sensor3on=Button(v1,image=img_on,command=lambda: on(27)).place(x=x1,y=350,width=90,height=80)

button_sensor3off=Button(v1,image=img_off,command=lambda: off(27)).place(x=x2,y=350,width=90,height=80)

button_settings3=Button(v1,image=img_settings,command=toplevel2).place(x=x3,y=350,width=90,height=80)

#Boton de salir
quit_image=PhotoImage(file="exit.png")
quit_button=Button(v1,image=quit_image,command=v1.destroy).place(x=x3+50,y=450,height=60,width=60)

v1.mainloop()
