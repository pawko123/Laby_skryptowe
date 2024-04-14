# zad1
inw = """Litwo! Ojczyzno moja! ty jestes jak zdrowie.
Ile cie trzeba cenic, ten tylko sie dowie,
Kto cie stracil. Dzis pieknosc twa w calej ozdobie
Widze i opisuje, bo tesknie po tobie."""


# zad2
def zad2():
    inw_plik = open("inwokacja.txt", 'r')
    print(inw_plik.readline())
    inw_plik.close()


# zad2()
# zad3
inw_plik = open("inwokacja.txt", 'r')
lista = [x.replace("\n", "") for x in inw_plik.readlines()]
polaczona_lista = '_'.join(lista)
#print(polaczona_lista)
inw_plik.close()


# zad4
def zad4():
    print("\nMałymi literami:")
    for x in lista: print(x.lower())

    print("\nWielkimi literami:")
    for x in lista: print(x.upper())

    print("\nKazdy wers z duzej")
    for x in lista: print(x.capitalize())

    print("\nCo drugi wers z wielkiej litery, co drugi z malej:")
    for x in range(len(lista)): print(lista[x].capitalize() if x % 2 == 0 else lista[x].lower())

    def duzamala(linia):
        wynik = ''
        for x in range(len(linia)): wynik += linia[x].upper() if x % 2 == 0 else linia[x].lower()
        return wynik

    print("\nCo druga litera wielka, co druga mala:")
    for x in lista: print(duzamala(x))

    print("\nCo druga litera:")
    for x in lista: print(x[::2])

    print("\nOdwrocona kolejnosc")
    for x in lista[::-1]: print(x)


#zad4()
# zad5
def zad5():
    inw1,inw2,inw3,inw4 = "","","",""
    for x in lista: inw1 += x.upper()
    for x in lista: inw2 += x.lower()
    for x in lista: inw3 += x.capitalize()
    for x in lista[::-1]: inw4 += x
    print(inw2 == inw1)
    print(inw2 > inw1)
    print(inw2 < inw1)
    print(inw3 == inw3)
    print(inw4>inw3)
    print(inw2>inw3)

#zad5()
# zad6
def zad6():
    print(inw.replace(' ', ''))
#zad6()

# zad7
def zad7():
    slowa = inw.split()
    for x in range(len(slowa)):
        plik = open(f'slowa/slowonr_{x + 1}.txt', 'w')
        plik.write(slowa[x])
        plik.close()
#zad7()
# zad8
def zad8():
    kopia = inw.replace('a', '{}')
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    acount = inw.count('a')
    print(kopia.format(*[alfabet[x % len(alfabet)] for x in range(acount)]))
#zad8()
# zad9
def zad9():
    index = 1
    kopia = ""
    slownik = {}
    for znak in range(len(inw)):
        if inw[znak] == 'w':
            kopia += "{w" + str(index) + "}"
            slownik[f'w{index}'] = f'0x{format(index, "04X")}'
            index += 1
        else:
            kopia += inw[znak]

    print(kopia.format(**slownik))
#zad9()
# zad10
def zad10():
    formatka = """Witaj {imie} {nazwisko},
Dziękujemy za złożenie zamowienia w naszym sklepie internetowym. Poniżej znajduje się lista zamówionych produktow:
    
{lista_produktow}
SUMA: {sumacalkowita} zł
    
Pozdrawiamy,
Zespół TwojFantastycznySklep"""
    produkty = [
        {"nazwa": "Ksiazka", "ilosc": 1, "cena": 100},
        {"nazwa": "Zeszyt", "ilosc": 2, "cena": 8}
    ]
    zamowienie = {"imie": "Pawel", "nazwisko": "Laskarzewski", "produkty": produkty,
                  "cena_calosciowa": sum([x["cena"] * x["ilosc"] for x in produkty])}

    def listing_produktow(produkty):
        listing = ""
        for produkt in produkty:
            listing += "- {nazwa}, szt {ilosc}, cena {cenazaszt} zł,  {lacznasuma} zł\n".format(nazwa=produkt["nazwa"],
            ilosc=produkt["ilosc"], cenazaszt=produkt["cena"], lacznasuma=produkt["cena"] * produkt["ilosc"])
        return listing

    print(formatka.format(imie=zamowienie["imie"], nazwisko=zamowienie["nazwisko"],
                          lista_produktow=listing_produktow(zamowienie["produkty"]),
                          sumacalkowita=zamowienie["cena_calosciowa"]))
#zad10()

# zad11
def zad11():
    tekst = """Zen Pythona
Piękny jest lepszy niż brzydki.
Wyraźny jest lepszy niż niejasny.
Prosty jest lepszy niż skomplikowany.
Skomplikowany jest lepszy niż zagnieżdżony.
Płaski jest lepszy niż zagnieżdżony.
Rzadki jest lepszy niż gęsty.
Czytelność ma znaczenie.
Specjalne przypadki nie są na tyle specjalne, aby łamać reguły.
Chociaż praktyczność pokona czystość.
Błędy nigdy nie powinny pozostać niezauważone.
Mimo że milczenie jest akceptowane, nie zgadzaj się na nie.
W razie wątpliwości, zastosuj zasadę jednoznaczności."""
    plik = open('plik.txt', 'w')
    plik.write(tekst)
#zad11()

# zad12
def zad12():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    plik = open(nazwa_pliku, "r")
    print(f"Zawartość pliku '{nazwa_pliku}':")
    print(plik.read())
    plik.close()
#zad12()
# zad13
def zad13():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    try:
        # Otwarcie pliku
        plik = open(nazwa_pliku, "r")
        print(f"Zawartość pliku '{nazwa_pliku}':")
        print(plik.read())
        plik.close()
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")
#zad13()
# zad14
def zad14():
    plik = open('plik.txt', "r")
    sekwencja = [x.replace('\n', '') for x in plik.readlines()]
    for x in range(len(sekwencja)): sekwencja[x] += '!\n' if x % 2 == 0 else '?\n'
    nazwa_pliku2 = input("Podaj nazwe pliku do ktorego zapisac:")
    plik = open(nazwa_pliku2, "w")
    plik.writelines(sekwencja)
    plik.close()
#zad14()
# zad15
def zad15():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    try:
        # Otwarcie pliku
        plik = open(nazwa_pliku, "r")
        linie = plik.readlines()
        index = int(input("Podaj ktora linie tekstu wyswietlic:"))
        try:
            print(linie[index - 1])
        except IndexError:
            print("Linijka z poza zakresu")
        plik.close()
    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")

zad15()
