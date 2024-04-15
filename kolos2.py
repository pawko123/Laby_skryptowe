# -*- coding: UTF-8 -*-
ciag="ciaz0z0zerami0"
lista=[]
licznik=0
for i in range(len(ciag)):
    if(ciag[i]=='0'):
        lista.append(i)
        licznik+=1
print(licznik)
print(lista)
liczby=[1,2,3,4,5,6,7,8,9,10]
lista=list(map(lambda x:2*x,liczby))
print(lista)