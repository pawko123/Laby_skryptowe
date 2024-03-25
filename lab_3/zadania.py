from random import randint
from statistics import median

import numpy as np


def zad5():
    l = [x for x in range(1, 21)]
    np = [x for x in l if x % 2]
    print(np)


def zad6():
    macierz = [[i * j for i in range(1, 5)] for j in range(1, 5)]
    print(np.matrix(macierz))


def zad7():
    tensor = [[[i / j / k for i in range(1, 4)] for j in range(1, 4)] for k in range(1, 4)]
    print(np.array(tensor))


def zad8():
    slownik = {"email4@gmail.com": "Pawel Laskarzewski",
               "email2@gmail.com": "Kuba Martynski",
               "email3@gmail.com": "Norbert Przyjemski",
               "email1@gmail.com": "Adrian Wojewski"}
    print(sorted(slownik.items()))


def zad9():
    studenci = [
        {"Imie": "Pawel", "Nazwisko": "Laskarzewski", "wiek": 22, "oceny": [randint(2, 5) for x in range(10)]},
        {"Imie": "Adrian", "Nazwisko": "Wojewski", "wiek": 20, "oceny": [randint(2, 5) for x in range(10)]},
        {"Imie": "Norbert", "Nazwisko": "Przyjemski", "wiek": 21, "oceny": [randint(2, 5) for x in range(10)]},
        {"Imie": "Kuba", "Nazwisko": "Martynski", "wiek": 23, "oceny": [randint(2, 5) for x in range(10)]},
    ]
    srednia_ocen = [sum(x["oceny"]) / len(x["oceny"]) for x in studenci]
    srednia_wszystkich = sum(srednia_ocen) / len(srednia_ocen)
    mediana_wieku = median([x["wiek"] for x in studenci])
    mediana_dlugosci_nazwiska = median(len(x["Nazwisko"]) for x in studenci)
    print(srednia_ocen)
    print(srednia_wszystkich)
    print(mediana_wieku)
    print(mediana_dlugosci_nazwiska)
