import numpy as np
def zad5():
    l=[x for x in range(1,21)]
    np=[x for x in l if x % 2]
    np2=l[0:20:1]
    print(np)
def zad6():
    macierz=[[(i+1)*(j+1) for i in range(4)] for j in range(4)]
    print(np.matrix(macierz))
def zad7():
    tensor=[[[(i+1)*(j+1)*(k+1) for i in range(4)] for j in range(4)]for k in range(4)]
    print(tensor)