from tkinter import *
import datetime as d

def actualiser():
    h = d.datetime.now().hour
    m = d.datetime.now().minute
    s = d.datetime.now().second
    now.set(f"{h}:{m}:{s}")
    today.set([f"{da}-{month}-{y}"])
    menu.after(1000, actualiser)

menu = Tk()
menu.geometry("200x100")
menu.title("Horloge")
menu.config(background="black")

h = d.datetime.now().hour
m = d.datetime.now().minute
s = d.datetime.now().second
da = d.datetime.now().day
month = d.datetime.now().month
y = d.datetime.now().year

now = StringVar()
now.set([f"{h}:{m}:{s}"])
heure = Label(menu,textvariable=now,foreground="white",background="black").place(x = 70 , y =30)

today = StringVar()
today.set([f"{da}-{month}-{y}"])
day = Label(menu,textvariable=today,foreground="white",background="black").place(x = 70 , y =50)

actualiser()

menu.mainloop()