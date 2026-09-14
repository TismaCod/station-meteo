import random

#Choix du niveau entre 1 (100 - 999), niveau 2 (1000-9999) et niveau 3 (10000 - 99999)
niv = input("Choisir le niveau : ")
if niv == "1":
        passwd = str(random.randint(100,999))
if niv == "2":
        passwd = str(random.randint(1000,9999))
if niv == "3":
        passwd = str(random.randint(10000,99999))
print(passwd)

#Fonction permet de calculer le nobre de caracteres correct et incorrect entre n et v
def char_checker(n,v): 
    correct = 0
    incorrect = 0
    for i in range(len(n)):
        if n == v:
            pass
        else:
            if n[i] == v[i]:
                correct += 1
            else:
                incorrect += 1
    return correct,incorrect

#Initie find qui, si est False, considera que le mdp n'a pas ete trouve
#Initie tentative qui compte a quel numero de tentative on est
find = False
tentative = 0

#check[1] est egal a la valeur incorrect dans la fonction char_checker et check[0] egal a la valeur correct
#Si la valeur incorrect check[1] est egal a 0, alors le mdp a ete trouve
for i in range(10):
    guess = input("\nEntrer votre proposition : ")
    check = char_checker(passwd,guess)
    if check[1] == 0:
        print("\n==========\nBRAVO !\nCode trouve : ",passwd,"\nNombre de tentatives : ",tentative,"\n==========\n")
        find = True
        break
    else:
        print("Chiffres bien places : ",check[0],"Chiffres mal places : ",check[1])
        tentative += 1

if find == False:
    print("\n==========\nPerdu !\nLe code etait : ",passwd,"\n==========\n")
