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

arv1=float(input("Arv1: "))
t=input("tehe: ")
arv2=float(input("Arv2: "))
vastus=eval(str(arv1)+t+str(arv2))
print(arv1,t,arv2,"=",vastus)
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))
