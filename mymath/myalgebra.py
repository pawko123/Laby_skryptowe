def dodaj(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))] \
        if len(a) == len(b) and len(a[0]) == len(b[0]) else "Nie można dodać macierzy różnych rozmiarów"


def odejmij(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))] \
        if len(a) == len(b) and len(a[0]) == len(b[0]) else "Nie można odjac macierzy różnych rozmiarów"


def pomnoz(a, b):
    return [[sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))] \
        if len(a[0]) == len(b) else "Nie można mnozyc macierzy podanych rozmiarów"


print(pomnoz([[4, 2], [4, 3]], [[5, 4, 6], [8, 5, 3]]))
print(pomnoz([[4, 2, 3], [4, 3, 3]], [[5, 4, 6], [8, 5, 3]]))
print(odejmij([[1, 2], [3, 4]], [[5, 3], [1, 1]]))
