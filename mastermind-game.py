import random
passwd = str(random.randint(1000,9999))
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

for i in range(10):
    guess = input("\nEntrer votre proposition : ")
    check = char_checker(passwd,guess)
    if check[1] == 0:
        print("\nBRAVO !\n")
        break
    else:
        print("Chiffres bien places : ",check[0],"Chiffres mal places : ",check[1])
