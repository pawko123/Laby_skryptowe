def dodaj(a, b):
    return [a[x] + b[x] for x in range(len(a))] if len(a) == len(b) else "Inne dlugosci wektorow"


def odejmij(a, b):
    return [a[x] - b[x] for x in range(len(a))] if len(a) == len(b) else "Inne dlugosci wektorow"


def pomnoz(a, b):
    return [a[x] * b[x] for x in range(len(a))] if len(a) == len(b) else "Inne dlugosci wektorow"
