#print("tere maailm!".center(75,"-"))
#nimi=input("mis on sinu nimi on?").capitalize() #python->Python
#print("tere" +nimi+ "!")
#print("tere", nimi+"!")
#print("Tere {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled?"))                      #"21"!=21
#print("Tere {0}! Sa oled {1} asstat vana".format(nimi, vanus))
#type(nimi)
#type(vanus)
#print("Muutuja nimi=",nimi,type(nimi))
#print("Muutuja vanus=",vanus,type(vanus))

#arv1=float(input("Arv1: "))
#t=input("tehe: ")
#arv2=float(input("Arv2: "))
#vastus=eval(str(arv1)+t+str(arv2))
#print(arv1,t,arv2,"=",vastus)
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))

#vanus=18
#eesnimi="Jaak"
#pikkus=16.5
#kas_kaib_koolis=True

#print("Muutuja vanus=",vanus,"on", type(vanus))
#print("Muutuja esnimi=",eesnimi,"on", type(eesnimi))
#print("Muutuja kas_kaib_koolis=",kas_kaib_koolis,"on", type(kas_kaib_koolis))

#import math
from random import *
#kokku=randint(1,100)
#print("laual peal on",kokku, "kommid Mitu tahad süüa?")
#kommid=int(input(""))
#kokku-=kommid
#print("Nüüd kokku on",kokku)

from math import *
#u=float(input("Ümbermõõt: "))
#d=round(u/pi,2)
#print("läbimõõt", d)

N = float(input("Длина участка:"))
M = float(input("Ширина участка:"))

diagonal_lenght = sqrt(N**2 + M**2)
print(f"Длина диагонали:{diagonal_lenght} метров ")