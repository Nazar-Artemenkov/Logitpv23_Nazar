#1

#n = int(input("Введите число домов от 1 до 9: "))
## Запрашиваем у пользователя количество домов.
## Рисуем дом, повторяя каждую строку соответствующее количество раз.
#for i in range(n):
#    print("   ~~~~~   ", end="")
#print()
#for i in range(n):
#    print("  /_____\\  ", end="")
#print()
#for i in range(n):
#    print("  | []  |  ", end="")
#print()
#for i in range(n):
#    print("    -----  ", end="")
#print()



#2


# Hinnete klass 1
clas1 = [90, 85, 88, 92, 78]
# Hinnete klass 2
clas2 = [87, 89, 76, 94, 80]
# Arvutame keskmise hinde igas klassis
avg1 = sum(clas1) / len(clas1)  # Klassi 1 keskmine hinne
avg2 = sum(clas2) / len(clas2)  # Klassi 2 keskmine hinne
# Väljastame tulemused
print(f"Esimene klass: Keskmiselt {avg1}")
print(f"Teine klass: Keskmiselt {avg2}")
# Вывод результатов
print(f"Keskmine hinne esimeses klassis: {avg1}")
print(f"Keskmine hinne teises klassis: {avg2}")


#3

import random

## Loome juhuslike hinnete nimekirja
#hinded = [random.randint(60, 100) for _ in range(10)]
## Initsialiseerime muutujad minimaalse ja maksimaalse hinnete jaoks
#min_hinne = float('inf')  # Seame min_hinne väärtuseks lõpmatuse
#max_hinne = float() 
## Iga hinne võrreldakse min_hinne ja max_hinne'ga
#for hinne in hinded:
#    # Kui hinne on väiksem kui hetke min_hinne, siis uuendame min_hinne
#    if hinne < min_hinne:
#        min_hinne = hinne  
#    # Kui hinne on suurem kui hetke max_hinne, siis uuendame max_hinne
#    if hinne > max_hinne:
#        max_hinne = hinne  
## Väljastame tulemused
#print(f"Otsene nimekiri hinnetest: {hinded}")
#print(f"Minimaalne hinne: {min_hinne}")
#print(f"Maksimaalne hinne: {max_hinne}")



#5

## Küsime kasutajalt x minimaalset, maksimaalset ja sammu
#min_x = float(input("Sisestage x minimaalne väärtus: "))
#max_x = float(input("Sisestage x maksimaalne väärtus: "))
#samm = float(input("Sisestage samm: "))
## Väljastame tabeli päise
#print("   x   |   y   ")
#print("----------------")
## Itereerime x väärtuste kaudu, arvestades kasutaja sisendit
#current_x = min_x
#while current_x <= max_x:
#    y = -0.5 * current_x + current_x  # Arvutame funktsiooni väärtuse
#    print(f"{current_x:.1f}   |  {y:.2f}")
#    current_x += samm






print("*** ARVUMÄMGUD ***") 
# Ввод целого числа от пользователя с обработкой ошибок
while True:
    try:
        a = abs(int(input("Введите целое число => ")))
        break
    except ValueError:
        print("Введите целое число")
# Проверка, является ли введенное число нулем
if a == 0:
    print("Нулевое число не интересно")
else:
    # Инициализация переменных и уведомление пользователя
    print("Определение четных и нечетных цифр в числе")
    print()
    c = b = a
    even_count = 0
    odd_count = 0
    # Подсчет четных и нечетных цифр
    while b > 0:
        if b % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        b = b // 10
   # Вывод количества четных и нечетных цифр
    print("Четные цифры:", even_count)
    print("Нечетные цифры:", odd_count)
    print()
    # Переворот числа
    print("*Переворот* числа")
    print()
    reversed_number = 0
    while a > 0:
        digit = a % 10
        a = a // 10
        reversed_number = reversed_number * 10 + digit
    print("*Перевернутое* число", reversed_number)
    print()
    # Проверка гипотезы Коллатца
    print("Проверка гипотезы Коллатца")
    print()
    if c % 2 == 0:
        print("c - четное. Деление на 2.")
    else:
        print("c - нечетное. Умножение на 3, добавление 1, деление на 2.")
    while c != 1:
        if c % 2 == 0:
            c = c // 2
        else:
            c = (3 * c + 1) // 2
        print(c, end=" ")
    print()
    print("Гипотеза верна")

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