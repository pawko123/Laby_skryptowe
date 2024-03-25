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
    sekwencja_do_zgadniecia = random.choices([x for x in range(1, 4)], k=5)
    zgadl = False
    while not zgadl:
        sekwencja_gracza = []
        for x in range(5):
            liczba = input("Podaj liczbe od 1 do 3\n")
            sekwencja_gracza.append(liczba)
        zgadniete_liczby = 0
        liczby_na_innych_miejscach = 0
        kopia_sdz = sekwencja_do_zgadniecia.copy()
        for x in range(5):
            for y in range(5):
                if int(sekwencja_gracza[x]) == kopia_sdz[y]:
                    liczby_na_innych_miejscach += 1
                    kopia_sdz[y] = 'x'
            if int(sekwencja_gracza[x]) == sekwencja_do_zgadniecia[x]:
                zgadniete_liczby += 1
            else:
                sekwencja_gracza[x] = 'x'
        print("Zgadnieto " + str(zgadniete_liczby) + " z 5 liczb")
        print(sekwencja_gracza)
        print("Oraz " + str(liczby_na_innych_miejscach - zgadniete_liczby) + " znajduja sie na innych miejscach")
        if zgadniete_liczby >= 4:
            print("Wygrano gre Mastermind")
            zgadl = True
def zad11():
        dlugosc_sekwecji=int(input("Podaj dlugosc sekwencji do zgadniecia\n"))
        poczatek_zakresu=int(input("Podaj poczatek zakresu sekwencji do zgadniecia\n"))
        koniec_zakresu=int(input("Podaj koniec zakresu sekwencji do zgadniecia\n"))
        sekwencja_do_zgadniecia = random.choices([x for x in range(poczatek_zakresu, koniec_zakresu+1)], k=dlugosc_sekwecji)
        zgadl = False
        while not zgadl:
            sekwencja_gracza = []
            for x in range(dlugosc_sekwecji):
                liczba = input("Podaj liczbe od "+str(poczatek_zakresu)+" do "+str(koniec_zakresu)+"\n")
                sekwencja_gracza.append(liczba)
            zgadniete_liczby = 0
            liczby_na_innych_miejscach = 0
            kopia_sdz = sekwencja_do_zgadniecia.copy()
            for x in range(dlugosc_sekwecji):
                for y in range(dlugosc_sekwecji):
                    if int(sekwencja_gracza[x]) == kopia_sdz[y]:
                        liczby_na_innych_miejscach += 1
                        kopia_sdz[y] = 'x'
                if int(sekwencja_gracza[x]) == sekwencja_do_zgadniecia[x]:
                    zgadniete_liczby += 1
                else:
                    sekwencja_gracza[x] = 'x'
            print("Zgadnieto " + str(zgadniete_liczby) + " z "+str(dlugosc_sekwecji)+" liczb")
            print(sekwencja_gracza)
            print("Oraz " + str(liczby_na_innych_miejscach - zgadniete_liczby) + " znajduja sie na innych miejscach")
            if zgadniete_liczby >= (dlugosc_sekwecji-1):
                print("Wygrano gre Mastermind")
                zgadl = True
