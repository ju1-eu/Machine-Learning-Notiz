#!/usr/bin/env python
# coding: utf-8
# Variablen - Logik - Schleifen

# Variablen
zahl = 1
print(zahl)
print(type(zahl))

# Datentypen
v1 = 1
v2 = 1.0
v3 = 'Jan'
v4 = True

# Ausgabe
print("\nDatatypen:")
print(v1)
print(type(v1))
print(v2)
print(type(v2))
print(v3)
print(type(v3))
print(v4)
print(type(v4))

# Logik

zahl_input = input("Gebe eine Zahl von 1-10 ein! ")
print(type(zahl_input))
zahl_input = int(input("Gebe eine Zahl von 1-10 ein! "))
print(type(zahl_input))

if zahl_input == 4:
    print("Du hast gewonnen!")
elif zahl_input == 5 or zahl_input == 3:
    print("Knapp daneben!")
else:
    print("Du hast verloren!")


# Schleifen

# For Schleife

for i in range(3):
    zahl_input = int(input("Gebe eine Zahl von 1-10 ein! "))

    if zahl_input == 4:
        print("Du hast gewonnen!")
    elif zahl_input == 5 or zahl_input == 3:
        print("Knapp daneben!")
    else:
        print("Du hast verloren!")

# Weiteres zur For-Schleife

# for(int i = 0; i < 10; i+=2)
for i in range(0, 10, 2):
    print("i: ", i)

# While-Schleife

gewonnen = False
while(gewonnen == False):
    zahl_input = int(input("Gebe eine Zahl von 1-10 ein! "))

    if zahl_input == 4:
        print("Du hast gewonnen!")
        gewonnen = True
    elif zahl_input == 5 or zahl_input == 3:
        print("Knapp daneben!")
    else:
        print("Du hast verloren!")

print("Spiel beendet!")

input() # Pause