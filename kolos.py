# -*- coding: UTF-8 -*-
#finally-za pomoca tego slowa definiujemy blok instrukcji ktory ma sie wykonac po bloku try-catch np.
#try:
    #kod
#catch rodzajbledu:
#   #obsluga bledu
#finally:
#   print("Koniec")
#none-dziala jak null w innych jezykach, wskazuje na to ze zmienna nie ma wartosci np. imie=None
#lambda-sluzy do tworzenia jednolinijkowej funkcji bez nazwy np. lambda x:2*x
#def-sluzy do definiowania funkcji np.def funkcja():
#iter-funkcja wbudowana ktora sluzy do zwracania iteratora z obiektu iterowalnego,ktory przechodzi po kolejnych elementach w petli
lista=["czerwony","niebieski","zielony"]
krotka=("czerwony","niebieski","zielony")
slownik={1:"czerwony",2:"niebieski",3:"zielony"}
zbior={"czerwony","niebieski","zielony"}
#krotka jest jedynie niezmienna
#zbior jest uporzadkowany, nie dopuszcza duplikatow,ale jest zmienny
#lista nie jest uporzadkowana,jest zmienna,pozwala na duplikaty
#zbior jest nieindeksowany i uporzadkowany
#slownik nie moze miec duplikatow


ciag = "ciag0z0zerami0"
def ilosc_zer(ciag):
    pozycja=[]
    for x in range(len(ciag)):
        if ciag[x]=="0":
            pozycja.append(x)
    print (len(pozycja), pozycja)
ilosc_zer(ciag)


i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

macierz=[[(i*j)/(2*i) if i!=0 else 0 for j in range(5)] for i in range(5)]
print(macierz)
#type() - zwraca typ oobiektu np.
x = 3
type(x)
#len() - zwraca długość obiektu np len(x)
#upper() - zmienia wszystkie znaki na duże np. napis.upper()
#replace() - zamienia konkretny ciag znakow na inny. x.replace(" ","") usunie z x wszystkie spacje

napis="test%%%   test"
a=napis[::-1]
b=napis.replace("%"," ")
c=napis.replace(" ","")
print(a,b,c)