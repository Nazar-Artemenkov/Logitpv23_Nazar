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

#N = float(input("Длина участка:"))
#M = float(input("Ширина участка:"))

#diagonal_lenght = sqrt(N**2 + M**2)
#print(f"Длина диагонали:{diagonˇal_lenght} метров ")

#6
#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#    try:
#       teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#       kiirus = teepikkus/aeg
#       print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    except :
#       print("Viga andmetaga!")

#except :
#    print("On vaja ainult numbrid sisestada!")


#7 
#number1 = float(input("Введите любое число:"))
#number2 = float(input("Введите любое число:"))
#number3 = float(input("Введите любое число:"))
#number4 = float(input("Введите любое число:"))
#number5 = float(input("Введите любое число:"))

#average = (number1 + number2 + number3 + number4 + number5) / 5
#print(f"Среднее арефметическое: {average}")

#8
#print("  @..@")
#print(" (----)")
#print("( \__/ )")
#print("^^ \"\" ^^")

#9
#try:
#     a = int(input("Введите сторону А:"))
#     try:
#       b = int(input("Введите сторону B:"))
#       try:
#         c = int(input("Введите сторону С:"))
#         P = a + b + c
#         print(f"Периметр треугольника: {P}")
#       except :
#         print("viga muutujaga!")
#     except :
#      print("viga muutujaga!")
#except :
#    print("On vaja täisarv kasutada")

#try:
#    c = int(input("Введите сторону С:"))
#except :
#    print("viga muutujaga!")


#10
#try:
#    P=int(input("sõbrade kogus:"))
#except :
#    pass
#Pitsa_hind= 12.90


#Protsenti = 10

#jootraha = (Protsenti / 100) * Pitsa_hind

#kokku_maksta = Pitsa_hind + jootraha

#kokku = kokku_maksta / P
#print(f"kokku maksta: {kokku:.2f} euro")


#try:
#    s1 = float(input("введите длину первой стороны квадрата:"))
#    s2 = float(input("введите длину первой стороны квадрата:"))
#    if s1 == s2 :
#        print("Это квадрат!")
#    else :
#        print("Это не квадрат!")
#except :
#    print("Гдето ошибка посмотрите тип как вы указали данные")



#from random import *
#from datetime import *
#a=10
#b=2.3
#c="programma"
#d="11111"
#print(b.as_integer())
#print(c.isalpha())
#print(d.isdecimal())

print("Tere! olen sinu uus sõber - Python!")
nimi = input("Sisestage oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = input((nimi + "!Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
if vastus == "1":
    pikkus = float(input("sisestage oma pikkus meetrites: "))
    mass = float(input("Sisestage oma kaal kilogrammides: "))
    indeks = mass / (0.01 * pikkus) ** 2
    print(nimi + "Sinu keha indeks on: {:.1f}".format(indeks))
    if indeks < 16:
        print("Tervisele ohtlik alakaal")
    elif 16 <= indeks< 19:
        print("Alakaal")
    elif 19 <= indeks < 25:
        print("Normaalkaal")
    elif 25 <= indeks < 30:
        print("Ülekaal")
    elif 30 <= indeks <35:
        print("Rasvumine")
    elif 35 <= indeks < 40:
        print("Tugev rasvumine")
    else:
        print("Tervisele ohtlik rasvumine")
else:
    print("Aitah, et külastasid seda programmi!")
