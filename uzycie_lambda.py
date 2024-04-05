# Funkcja lambda
dodaj_lambda = lambda a, b: a + b
liczby = [1, 2, 3, 4, 5]
liczby2=[6,7,8,9,0]
#przyklady dla funkcji map
podwojenie = map(lambda x:x*2,liczby)
dodanie_tabel = map(lambda x,y:x+y,liczby,liczby2)
#wywolania
print(dodaj_lambda(3,4))
print(list(podwojenie))
print(list(dodanie_tabel))