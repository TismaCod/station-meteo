import random

niv = input("Choisir le niveau : ")
if niv == "1":
        passwd = str(random.randint(100,999))
if niv == "2":
        passwd = str(random.randint(1000,9999))
if niv == "3":
        passwd = str(random.randint(10000,99999))
print(passwd)

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

find = False
for i in range(10):
    guess = input("\nEntrer votre proposition : ")
    check = char_checker(passwd,guess)
    if check[1] == 0:
        print("\nBRAVO !\n")
        find = True
        break
    else:
        print("Chiffres bien places : ",check[0],"Chiffres mal places : ",check[1])

if find == False:
    print("PERDU ! Le code etait ",passwd)
