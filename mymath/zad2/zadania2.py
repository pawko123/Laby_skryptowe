def dodaj(a, b):
    return [a[x] + b[x] for x in range(len(a))] if len(a) == len(b) else "Inne dlugosci wektorow"
def odejmij(a, b):
    return [a[x] - b[x] for x in range(len(a))] if len(a) == len(b) else "Inne dlugosci wektorow"
def pomnoz(a, b):
    return [a[x] * b[x] for x in range(len(a))] if len(a) == len(b) else "Inne dlugosci wektorow"
a=[1,5,2,4,1]
b=[2,2,4,1]
print(dodaj(a,a))
print(dodaj(a,b))
print(odejmij(b,b))
print(odejmij(a,b))
print(pomnoz(b,b))
print(pomnoz(a,b))
"""
a=[1,5,2,4,1]
b=[2,2,4,1]
print(dodaj(a,a))
print(dodaj(a,b))
print(odejmij(b,b))
print(odejmij(a,b))
print(pomnoz(b,b))
print(pomnoz(a,b))
"""