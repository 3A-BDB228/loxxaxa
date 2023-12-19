import tkinter
from tkinter import *



xp = 5
love_d = 0
xp_happiness = 7
xer=0
x1=0
x2=0
x3=0
x4=0
def clicked():
    global xp
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp}/10\nСчастье {xp_happiness}/10")
    xarac.grid(column=1, row=0)
    btn.grid_remove()
    window.image = PhotoImage(file='F:\gbubu7.png')
    lada2 = Label(window, image=window.image)
    lada2.grid(row=0, column=0)

    btn1.grid(column=1,row=1)
    btn2.grid(column=2,row=1)



def clicked2():
    global btn1
    btn1.grid_remove()
    btn2.grid_remove()
    window.image = PhotoImage(file='F:\gbubu6.png')#подошли к типу
    lada3 = Label(window, image=window.image)
    lada3.grid(row=0, column=0)
    btn3.grid(column=1,row=1)




def clicked4():
    global btn1
    btn3.grid_remove()
    window.image = PhotoImage(file='F:\gbubu9.png')
    lada4 = Label(window, image=window.image)
    lada4.grid(row=0, column=0)
    btn4.grid(column=1, row=1)#kola
    btn5.grid(column=2, row=1)#dollluk
    btn6.grid(column=3, row=1)#sugu
    btn7.grid(column=4, row=1)#energetik


def clicked5():
    global xp_happiness
    xp_happiness = xp_happiness + 4
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp }/10\nСчастье {xp_happiness }/10")
    xarac.grid(column=1, row=0)
    btn4.grid_remove()
    btn5.grid_remove()
    btn6.grid_remove()
    btn7.grid_remove()
    btn_lol.grid(column=1, row=1)
def clicked6():
    global xp
    xp= xp-2
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp}/10\nСчастье {xp_happiness}/10")
    xarac.grid(column=1, row=0)
    btn4.grid_remove()
    btn5.grid_remove()
    btn6.grid_remove()
    btn7.grid_remove()
    btn_lol.grid(column=1, row=1)
def clicked7():
    global xp
    xp=xp-4
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp}/10\nСчастье {xp_happiness}/10")
    xarac.grid(column=1, row=0)
    btn4.grid_remove()
    btn5.grid_remove()
    btn6.grid_remove()
    btn7.grid_remove()
    btn_lol.grid(column=1, row=1)
def clicked8():
    global love_d
    love_d=love_d+1
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp }/10\nСчастье {xp_happiness }/10")
    xarac.grid(column=1, row=0)
    btn4.grid_remove()
    btn5.grid_remove()
    btn6.grid_remove()
    btn7.grid_remove()
    btn_lol.grid(column=1,row=1)




def clicked3(): #после типа или не подходили
    global btn1
    btn1.grid_remove()
    btn2.grid_remove()
    window.image = PhotoImage(file='F:\gbubu10.png')
    lada5 = Label(window, image=window.image)
    lada5.grid(row=0, column=0)
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp}/10\nСчастье {xp_happiness}/10")
    xarac.grid(column=1, row=0)


def clicked9():
    btn_lol.grid_remove()

    window.image = PhotoImage(file='F:\gbubu11.png')
    lada6 = Label(window, image=window.image)
    lada6.grid(row=0, column=0)
    btn_lol2.grid(column=1,row=1)
def clicked10():
    window.image = PhotoImage(file='F:\gbubu12.png')
    lada6 = Label(window, image=window.image)
    lada6.grid(row=0, column=0)
    btn_lol2.grid_remove()
    btnx1.grid(column=1,row=1)
    btnx2.grid(column=2,row=1)

def lol1():
    global love_d
    love_d = love_d+4
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp }/10\nСчастье {xp_happiness }/10")
    xarac.grid(column=1, row=0)
    window.image = PhotoImage(file='F:\gbubu13.png')
    lada7 = Label(window, image=window.image)
    lada7.grid(row=0, column=0)
def lol2():
    global love_d
    love_d = love_d + 7
    xarac = Label(window, text=f" Любовь {love_d}/10\nЗдоровье {xp }/10\nСчастье {xp_happiness }/10")
    xarac.grid(column=1, row=0)
    window.image = PhotoImage(file='F:\gbubu13.png')
    lada8 = Label(window, image=window.image)
    lada8.grid(row=0, column=0)


window = Tk()
window.title("Лагерь")
window.geometry('1200x768')
window.resizable(False,False)
ikonca = tkinter.PhotoImage(file='F:\ikonka3.png')
window.iconphoto(False,ikonca)
btn = Button(window, text="Далее...", command=clicked)
btn.grid(column=1, row=1)
window.image = PhotoImage(file='F:\gbubu8.png')
lada = Label(window, image=window.image)
lada.grid(row=0, column=0)
btn1 = Button(window,text= "  1  ",command=clicked2)
btn2 = Button(window,text= "  2  ", command=clicked3)
btn3 = Button(window,text="Далее...", command=clicked4)

btn4 = Button(window,text="  1  ", command=clicked5)
btn5 = Button(window,text="  2  ", command=clicked6)
btn6 = Button(window,text="  3  ", command=clicked7)
btn7 = Button(window,text="  4  ", command=clicked8)
btnx1= Button(window,text="  1  ",command=lol1)
btnx2= Button(window,text="  2  ",command=lol2)
btn_lol = Button(window,text="Далее...", command=clicked9)
btn_lol2 = Button(window,text="Далее...",command=clicked10)
window.mainloop()