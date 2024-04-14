# -*- coding: UTF-8 -*-
#zad5
def zad5():
    def dodaj(a,b):
        return a+b
    def odejmij(a,b):
        return a-b
    def mnozenie(a,b):
        return a*b
    def dzielenie(a,b):
        return a/b
    wynik=dodaj(dzielenie(dodaj(4,mnozenie(2,odejmij(5,10))),odejmij(mnozenie(32,11),4)),2)
    print(wynik)
#zad5()
#zad6
def zad6():
    def ceil(x):
        if x == int(x):
            return int(x)
        elif x > 0:
            return x // 1 + 1
        else:
            return x // 1

    def floor(x):
        if x == int(x):
            return int(x)
        elif x > 0:
            return x // 1
        else:
            return x // 1 - 1

    liczby = [3.14, 6.78, -2.5, 10.0, 0.5, 7, -4]
    for liczba in liczby:
        print(f"Liczba: {liczba}, zaokraglenie w gore: {ceil(liczba)}, zaokraglenie w doł: {floor(liczba)}")
#zad6()
#zad7
def zad7():
    class Osoba:
        def __init__(self,imie,nazwisko):
            self.imie=imie
            self.nazwisko=nazwisko
        def przywitaj(self):
            print("Witaj "+self.imie+" "+self.nazwisko)
    typosoba1=type(Osoba.przywitaj)
    Osoba.przywitaj="text"
    typosoba2=type(Osoba.przywitaj)
    typprint=type(print("napis"))
    print(typprint)
    print(typosoba1)
    print(typosoba2)
#zad7()
#zad8
def zad8():

    liczby = list(map(lambda x: 2*x, range(1, 11)))
    print(liczby)
#zad8()
#zad9
def zad9():
    class Punkt:
        def __init__(self,x=1,y=1):
            self.x=x
            self.y=y
        def wyswietl(self):
            print(f"Punkt znajduje sie w ({self.x},{self.y})")
    punkt1=Punkt(4,2)
    punkt2=Punkt(2,1)
    punkt3=Punkt(4,4)
    punkt1.wyswietl()
    class Odcinek:
        def __init__(self,Punkt1=Punkt(),Punkt2=Punkt()):
            self.Punkt1=Punkt1
            self.Punkt2=Punkt2
        def dlugosc_odcinka(self):
            return ((self.Punkt1.x-self.Punkt2.x)**2+(self.Punkt1.y-self.Punkt2.y)**2)**0.5
    odcinek1=Odcinek(punkt1,punkt2)
    dlugosc=odcinek1.dlugosc_odcinka()
    print(f"Dlugosc odcinka: {dlugosc}")
    class Trojkat:
        def __init__(self,Punkt1=Punkt(),Punkt2=Punkt(),Punkt3=Punkt()):
            self.Punkt1=Punkt1
            self.Punkt2=Punkt2
            self.Punkt3=Punkt3
            self.Odcinek1=Odcinek(punkt1,punkt2)
            self.Odcinek2=Odcinek(punkt2,punkt3)
            self.Odcinek3=Odcinek(punkt3,punkt1)
        def obwod(self):
            return self.Odcinek1.dlugosc_odcinka()+self.Odcinek2.dlugosc_odcinka()+self.Odcinek3.dlugosc_odcinka()
        def pole(self):
            obwod=self.obwod()
            p=obwod/2
            return (p*(p-self.Odcinek1.dlugosc_odcinka())*(p-self.Odcinek2.dlugosc_odcinka())*(p-self.Odcinek3.dlugosc_odcinka()))**0.5


    Trojkat=Trojkat(punkt1,punkt2,punkt3)
    obwod=Trojkat.obwod()
    print(f"Obwod Trojkata {obwod}")
    pole=Trojkat.pole()
    print(f"Pole trojkata: {pole}")
#zad9()
def zad10():
    class Wektor:
        def __init__(self,x=1,y=1):
            self.x=x
            self.y=y
        def __add__(self,other):
            return Wektor(self.x+other.x,self.y+other.y)
        def __sub__(self,other):
            return Wektor(self.x-other.x,self.y-other.y)
        def __mul__(self,scalar):
            return Wektor(self.x*scalar,self.y*scalar)

        def __rmul__(self, scalar):
            return self.__mul__(scalar)
        def hadarman_product(self,other):
            return Wektor(self.x*other.x,self.y*other.y)
        def __str__(self):
            return f'({self.x},{self.y})'
    wektor1=Wektor(4,2)
    wektor2=Wektor(2,1)
    print(wektor1+wektor2)
    print(wektor1-wektor2)
    print(wektor1*3)
    print(4*wektor2)
    print(wektor1.hadarman_product(wektor2))
#zad10()
#zad11
def zad11():
    class Osoba:
        _id=1
        __wiek=25
        def __init__(self,imie,nazwisko):
            self.imie=imie
            self.nazwisko=nazwisko
    print(dir(Osoba))
#zad11()
#zad12
def zad12():
    class Prostokat:
        def __init__(self,x=1,y=1,w=1,h=1):
            self.x=x
            self.y=y
            self.w=w
            self.h=h
    class Okno:
        def __init__(self,nazwa="okienko",kolor="czarny",prostokat=Prostokat()):
            self.nazwa=nazwa
            self.kolor=kolor
            self.prostokat=prostokat
    Okno1=Okno()
    print(Okno1.prostokat.x)
#zad12()
#zad13
def zad13():
    class Prostokat:
        def __init__(self, x=1, y=1, w=1, h=1):
            self.x = x  # współrzędna x lewego górnego rogu
            self.y = y  # współrzędna y lewego górnego rogu
            self.w = w  # szerokość prostokąta
            self.h = h  # wysokość prostokąta
    class Okno(Prostokat):
        def __init__(self, nazwa="okienko", kolor="czarny", x=1, y=1, w=1, h=1):
            super().__init__(x, y, w, h)
            self.nazwa = nazwa
            self.kolor = kolor
    Okno1=Okno()
    print(Okno1.x)
#zad13()
#zad14
def zad14():
    class Osoba:
        def __init__(self, imie, nazwisko):
            self.imie = imie
            self.nazwisko = nazwisko

    class Student(Osoba):
        def __init__(self, nr_indeksu, oceny, imie, nazwisko):
            super().__init__(imie, nazwisko)
            self.nr_indeksu = nr_indeksu
            self.oceny = oceny

    class Pracownik(Osoba):
        def __init__(self, stanowisko, wynagrodzenie,imie=None, nazwisko=None):
            super().__init__(imie, nazwisko)
            self.stanowisko = stanowisko
            self.wynagrodzenie = wynagrodzenie

    class PracujacyStudent(Student, Pracownik):
        def __init__(self, nr_indeksu, oceny, stanowisko, wynagrodzenie,imie, nazwisko):
            Student.__init__(self, nr_indeksu, oceny,imie, nazwisko)
            Pracownik.__init__(self,stanowisko, wynagrodzenie, imie, nazwisko)

    WS=PracujacyStudent(100,[5,4,2,4,5],"Junior Developer",3000,"Pawel","Laskarzewski")
    print(WS.nr_indeksu)
    print(WS.oceny)
    print(WS.stanowisko)
    print(WS.wynagrodzenie)
    print(WS.imie)
    print(WS.nazwisko)
zad14()