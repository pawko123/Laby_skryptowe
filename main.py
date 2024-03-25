import importlib

import lab_2
import lab_3

import mymath

wektor=[]
while True:
    liczba = input("Podaj kolejna liczbe wektora lub zakoncz wpisujac 'K'")
    if liczba.upper() == 'K':
        break
    wektor.append(int(liczba))
    importlib.reload(mymath.myalgebra)
print(mymath.myalgebra.dodaj(wektor,wektor))
print(mymath.myalgebra.odejmij(wektor,wektor))
print(mymath.myalgebra.pomnoz(wektor,wektor))