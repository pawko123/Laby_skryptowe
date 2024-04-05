import importlib
import mymath

wektor=[]
while True:
    liczba = input("Podaj kolejna liczbe wektora lub zakoncz wpisujac 'K'")
    if liczba.upper() == 'K':
        break
    wektor.append(int(liczba))
    importlib.reload(mymath.myalgebra)
print(wektor)