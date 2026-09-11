import random
L = []
for i in range(25):
       L.append(random.randint(-5,35))

print('===== MESURES =====\n')
for i in L:
       print('Mesure : ',i)

somme = sum(L)/24

for i in L:
       alerte = 0
       if i >= 30:
              alerte += 1

print('\n===== BILAN METEO =====\n')
print('Temperature minimale : ',min(L),'\nTemperature maximale : ',max(L),'\nTemperature moyenne : ',somme)
print("Nombres d'alertes : ",alerte)
print('\n Humidite : ',random.randint(20,90))
