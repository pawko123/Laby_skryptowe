import random

import numpy as np


def zad5():
    l = [x for x in range(1, 21)]
    np = [x for x in l if x % 2]
    print(np)


def zad6():
    macierz = [[i  * j  for i in range(1,5)] for j in range(1,5)]
    print(np.matrix(macierz))


def zad7():
    tensor = [[[i / j  / k  for i in range(1,4)] for j in range(1,4)] for k in range(1,4)]
    print(np.array(tensor))


def zad8():
    slownik = {
        'jan@example.com': 'Jan Kowalski',
        'anna@example.com': 'Anna Nowak',
        'adam@example.com': 'Adam Wisniewski',
        'ewa@example.com': 'Ewa Dabrowska'
    }
    print(sorted(slownik.items()))


def zad9():
    studenci = [
        {'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 24, 'oceny': [random.randint(2, 5) for x in range(10)]},
        {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 22, 'oceny': [random.randint(2, 5) for x in range(10)]},
        {'imie': 'Adam', 'nazwisko': 'Wisniewski', 'wiek': 21, 'oceny': [random.randint(2, 5) for x in range(10)]},
        {'imie': 'Ewa', 'nazwisko': 'Dabrowska', 'wiek': 21, 'oceny': [random.randint(2, 5) for x in range(10)]}
    ]
    srednia_ocen_studenta = [sum(x['oceny']) / len(x['oceny']) for x in studenci]
    srednia_ocen_wszystkich = [sum(srednia_ocen_studenta) / len(srednia_ocen_studenta)]
    mediana_wieku = np.median([x['wiek'] for x in studenci])
    mediana_dlugosci_nazwiska = np.median([len(x['nazwisko']) for x in studenci])
    print(srednia_ocen_studenta)
    print(srednia_ocen_wszystkich)
    print(mediana_wieku)
    print(mediana_dlugosci_nazwiska)


def zad10():
    sekwencja_do_zgadniecia=random.choices([x for x in range(1, 4)], k=5)
    print(sekwencja_do_zgadniecia)
