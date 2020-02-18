from tkinter import *
import os
import pickle
import webbrowser
from modif import modif

rayon = 40
numCanister = int()
def readCanister():
    fichier = open("data","rb")
    global conf_canister1,conf_canister2,conf_canister3,conf_canister4,conf_canister5,conf_canister6
    conf_canister1 = pickle.load(fichier)
    conf_canister2 = pickle.load(fichier)
    conf_canister3 = pickle.load(fichier)
    conf_canister4 = pickle.load(fichier)
    conf_canister5 = pickle.load(fichier)
    conf_canister6 = pickle.load(fichier)
    fichier.close()

def writeCanister():
    fichier = open("data","wb")
    pickle.dump(conf_canister1,fichier)
    pickle.dump(conf_canister2,fichier)
    pickle.dump(conf_canister3,fichier)
    pickle.dump(conf_canister4,fichier)
    pickle.dump(conf_canister5,fichier)
    pickle.dump(conf_canister6,fichier)
    fichier.close()

readCanister()

def suprimer(event):
    i , y =  0 , 1
    while y <7 :
        if eval("conf_canister"+str(y))["viso"] == 7 :
            while i < 7 :
                if eval("conf_canister"+str(y))[str(i)]["name"] == sup.get() :
                    eval("conf_canister"+str(y))[str(i)]["name"] = ""
                    eval("conf_canister"+str(y))[str(i)]["stock"] = 0
                    eval("conf_canister"+str(y))[str(i)]["num"] = ""
                    eval("conf_canister"+str(y))[str(i)]["lait"] = ""
                    eval("conf_canister"+str(y))[str(i)]["TP"] = ""
                    eval("conf_canister"+str(y))[str(i)]["TB"] = ""
                    eval("conf_canister"+str(y))[str(i)]["impl"] = ""
                    eval("conf_canister"+str(y))[str(i)]["long"] = ""
                    eval("conf_canister"+str(y))[str(i)]["vitess"] = ""
                    eval("conf_canister"+str(y))[str(i)]["tempera"] = ""
                    eval("conf_canister"+str(y))[str(i)]["loco"] = ""
                    writeCanister()
                    insertScroll()
                i+=1
            i=0
        else :
            while i < 12 :
                if eval("conf_canister"+str(y))[str(i)]["name"] == sup.get() :
                    eval("conf_canister"+str(y))[str(i)]["name"] = ""
                    eval("conf_canister"+str(y))[str(i)]["stock"] = 0
                    eval("conf_canister"+str(y))[str(i)]["num"] = ""
                    eval("conf_canister"+str(y))[str(i)]["lait"] = ""
                    eval("conf_canister"+str(y))[str(i)]["TP"] = ""
                    eval("conf_canister"+str(y))[str(i)]["TB"] = ""
                    eval("conf_canister"+str(y))[str(i)]["impl"] = ""
                    eval("conf_canister"+str(y))[str(i)]["long"] = ""
                    eval("conf_canister"+str(y))[str(i)]["vitess"] = ""
                    eval("conf_canister"+str(y))[str(i)]["tempera"] = ""
                    eval("conf_canister"+str(y))[str(i)]["loco"] = ""
                    writeCanister()
                    insertScroll()
                i+=1
            i = 0
        y+=1
    y = 0

def insertScroll():
    readCanister()
    listb.delete(0,50)
    i , y =  0 , 1
    while y <7 :
        if eval("conf_canister"+str(y))["viso"] == 7 :
            while i < 7 :
                if eval("conf_canister"+str(y))[str(i)]["name"] != "" :
                    listb.insert(END,eval("conf_canister"+str(y))[str(i)]["name"])
                i+=1
            i=0
        else :
            while i < 12 :
                if eval("conf_canister"+str(y))[str(i)]["name"] != "" :
                    listb.insert(END,eval("conf_canister"+str(y))[str(i)]["name"])
                i+=1
            i = 0
        y+=1
    y = 0

def ttstock():
    i , y , ttsctock =  0 , 1 , 0
    while y <7 :
        if eval("conf_canister"+str(y))["viso"] == 7 :
            while i < 7 :
                ttsctock += eval("conf_canister"+str(y))[str(i)]["stock"]
                i+=1
            i=0
        else :
            while i < 12 :
                ttsctock += eval("conf_canister"+str(y))[str(i)]["stock"]
                i+=1
            i = 0
        y+=1
    y = 0
    return ttsctock

def lien(event):
     webbrowser.open_new(event.widget.cget("text"))
def chiffre(chaine):
    result = ""
    for i in chaine:
        if i in "0123456789" :
            result += i
    return result


def affInfo(i,n):
    entour(n,i)
    cani = eval("conf_canister"+str(n))
    infoName.configure(text="name :"+cani[i]["name"])
    infoStock.configure(text="stock :"+str(cani[i]["stock"])+" sur "+str(ttstock()))
    infoNuméro.configure(text="numéro du taureau :"+cani[i]["num"])
    infoLait.configure(text="lait :"+str(cani[i]["lait"]))
    infoTP.configure(text="TP :"+str(cani[i]["TP"]))
    infoTB.configure(text="TB :"+str(cani[i]["TB"]))
    infoImplantationArr.configure(text="implantation arrière :"+str(cani[i]["impl"]))
    infoLongeurTrayons.configure(text="longueur des trayons :"+str(cani[i]["long"]))
    infoVitesseTraite.configure(text="vitesse de traite :"+str(cani[i]["vitess"]))
    infoTemperament.configure(text="tempérament :"+str(cani[i]["tempera"]))
    infoLocomotion.configure(text="locomotion :"+str(cani[i]["loco"]))
    infoLien.configure(text="https://primholstein.com/index/index-fiche-taureau/"+chiffre(cani[i]["num"])+"-FR/",fg="blue",cursor="hand2")
    infoLien.bind("<Button-1>",lien)

def entour(canister,visotube):
    cani = eval("conf_canister"+str(canister))[str(visotube)]
    can.create_oval(cani["x"]-50,cani["y"]-50,cani["x"]+50,cani["y"]+50,dash=(3,3),outline="yellow",width=5)

def scrollAff(event):
    r = listb.curselection()
    nom = listb.get(r)
    i , y =  0 , 1
    while y <7 :
        if eval("conf_canister"+str(y))["viso"] == 7 :
            while i < 7 :
                if eval("conf_canister"+str(y))[str(i)]["name"] == nom :
                    affInfo(str(i),y)
                    eval("canister"+str(y)+"()")
                    entour(y,i)
                i+=1
            i=0
        else :
            while i < 12 :
                if eval("conf_canister"+str(y))[str(i)]["name"] == nom :
                    affInfo(str(i),y)
                    eval("canister"+str(y)+"()")
                    entour(y,i)
                i+=1
            i = 0
        y+=1
    y = 0

def click(event):
    cani = eval("conf_canister"+str(numCanister))
    i = 0
    if numCanister <= 3 :
        for i in "0123456" :
            if cani[i]["x"]-rayon<event.x <cani[i]["x"]+rayon and cani[i]["y"]-rayon< event.y <cani[i]["y"]+rayon :
                eval("canister"+str(numCanister)+"()")
                affInfo(i,numCanister)
    else :
        for i in ["0","1","2","3","4","5","6","7","8","9","10","11"] :
            if cani[i]["x"]-rayon<event.x <cani[i]["x"]+rayon and cani[i]["y"]-rayon< event.y <cani[i]["y"]+rayon :
                eval("canister"+str(numCanister)+"()")
                affInfo(i,numCanister)


def num_viso():
    readCanister()
    insertScroll()
    can.delete(ALL)
    can.create_oval(20,20,480,480,fill="grey")
    cani = eval("conf_canister"+str(numCanister))
    if cani["viso"] == 7 :
        for i in "0123456" :
            can.create_oval(cani[i]["x"]-rayon,cani[i]["y"]-rayon,cani[i]["x"]+rayon,cani[i]["y"]+rayon,fill=cani[i]["color"])
            can.create_text(cani[i]["x"],cani[i]["y"],text=i)
    else :
        for i in ["0","1","2","3","4","5","6","7","8","9","10","11"] :
            can.create_oval(cani[i]["x"]-rayon,cani[i]["y"]-rayon,cani[i]["x"]+rayon,cani[i]["y"]+rayon,fill=cani[i]["color"])
            can.create_text(cani[i]["x"],cani[i]["y"],text=i)

def color_button(bt):
    b1.configure(bg="grey")
    b2.configure(bg="grey")
    b3.configure(bg="grey")
    b4.configure(bg="grey")
    b5.configure(bg="grey")
    b6.configure(bg="grey")
    if bt == b1 :
        b1.configure(bg="red")
    elif bt == b2 :
        b2.configure(bg="red")
    elif bt == b3 :
        b3.configure(bg="red")
    elif bt == b4 :
        b4.configure(bg="red")
    elif bt == b5 :
        b5.configure(bg="red")
    else :
        b6.configure(bg="red")

def canister1():
    global numCanister
    numCanister = 1
    num_viso()
    color_button(b1)

def canister2():
    global numCanister
    numCanister = 2
    num_viso()
    color_button(b2)

def canister3():
    global numCanister
    numCanister = 3
    num_viso()
    color_button(b3)

def canister4():
    global numCanister
    numCanister = 4
    num_viso()
    color_button(b4)

def canister5():
    global numCanister
    numCanister = 5
    num_viso()
    color_button(b5)

def canister6():
    global numCanister
    numCanister = 6
    num_viso()
    color_button(b6)

fen = Tk()

fen.title("Plan de Cuve")
frame_can=Frame(fen)
can =Canvas(frame_can,width=500,height=500)
can.bind("<Button-1>",click)
can.grid()
frame_can.grid(column=0,row=1,rowspan =2)


frame_button = Frame(fen)
b1 = Button(frame_button,text="1",font=12,width=5,height=5,command=canister1,bg="grey")
b2 = Button(frame_button,text="2",font=12,width=5,height=5,command=canister2,bg="grey")
b3 = Button(frame_button,text="3",font=12,width=5,height=5,command=canister3,bg="grey")
b4 = Button(frame_button,text="4",font=12,width=5,height=5,command=canister4,bg="grey")
b5 = Button(frame_button,text="5",font=12,width=5,height=5,command=canister5,bg="grey")
b6 = Button(frame_button,text="6",font=12,width=5,height=5,command=canister6,bg="grey")

b1.grid(column=0,row=0)
b2.grid(column=1,row=0)
b3.grid(column=2,row=0)
b4.grid(column=3,row=0)
b5.grid(column=4,row=0)
b6.grid(column=5,row=0)
frame_button.grid(column=0,row=0)

frame_info = Frame(fen)
infoName = Label(frame_info)
infoStock = Label(frame_info)
infoNuméro = Label(frame_info)
infoLait = Label(frame_info)
infoTP = Label(frame_info)
infoTB = Label(frame_info)
infoImplantationArr = Label(frame_info)
infoLongeurTrayons = Label(frame_info)
infoVitesseTraite = Label(frame_info)
infoTemperament = Label(frame_info)
infoLocomotion = Label(frame_info)
infoLien = Label(frame_info)
infoName.grid(column=0,row=0,sticky=W,padx=15)
infoStock.grid(column=0,row=1,sticky=W,padx=15)
infoNuméro.grid(column=0,row=2,sticky=W,padx=15)
infoLait.grid(column=0,row=3,sticky=W,padx=15)
infoTP.grid(column=0,row=4,sticky=W,padx=15)
infoTB.grid(column=0,row=5,sticky=W,padx=15)
infoImplantationArr.grid(column=1,row=0,padx=15,sticky=W)
infoLongeurTrayons.grid(column=1,row=1,padx=15,sticky=W)
infoVitesseTraite.grid(column=1,row=2,padx=15,sticky=W)
infoTemperament.grid(column=1,row=3,padx=15,sticky=W)
infoLocomotion.grid(column=1,row=4,padx=15,sticky=W)
infoLien.grid(column=1,row=5,padx=15,sticky=W)

frame_info.grid(column=1,row=2,sticky=N)

frame_bar =Frame(fen)

scroll = Scrollbar(frame_bar)
listb = Listbox(frame_bar,width = 75,height = 10)
insertScroll()
listb.pack(side = LEFT, fill = Y)
scroll.pack(side = RIGHT, fill = Y)
frame_bar.grid(column=1,row=0,pady = 5 , padx = 15)
listb.bind("<ButtonRelease-1>",scrollAff)

frame_button2 = Frame(fen)
Button(frame_button2,text="modifier",command=modif).grid(column=0,row=2,padx=50)
sup = Entry(frame_button2)
sup.bind("<Return>", suprimer)
Label(frame_button2,text="suprimer :").grid(column=1,row=0)
sup.grid(column=1,row=2)

frame_button2.grid(column=1,row=1,sticky=N)

fen.mainloop()
