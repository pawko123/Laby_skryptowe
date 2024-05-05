import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import quad
from scipy.misc import derivative
from scipy.optimize import curve_fit


#zad1
def zad1():
    A=np.array([[1,2],[4,5],[7,8]])
    print(A)
    B=np.identity(3,int)*2
    print(B)
    C=np.array([2,1,0])
    print(C)
    D=np.array([[3,2,1],[0,5,6],[8,-1,2]])
    print(D)
    print('B+D')
    print(B+D)
    print('3A')
    print(3*A)
    print('-2C')
    print(-2*C)
    print('BA')
    print(B @ A)
    print('DB')
    print(D @ B)
    print('2A + B - C')
    print('Nie mozna z powodu zlych wymiarow')
    #print(2 * A + B - C)
    print('CD - DC')
    print(C @ D - D @ C)
    print('2B - D')
    print(2 * B - D)
    print('DD')
    print(D @ D)
    print('BB + DD')
    print(B @ B + D @ D)
    print('4A')
    print(4 * A)
    print('AB')
    print('nie mozna z powodu zlych wymiarow')
    #print(A @ B)
    print('B^2')
    print(B @ B)
    print('A^2')
    print('nie mozna z powodu zlych wymiarow')
    #print(A @ A)
    print('C/C')
    print('nie mozna z powodu zlych wymiarow')
    #print(C/C)
#zad1()
#zad2
def zad2():
    A = np.array([[1, 2], [4, 5], [7, 8]])
    B = np.identity(3, int) * 2
    C = np.array([2, 1, 0])
    D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])
    print(np.transpose(A))
    print(np.transpose(B))
    print(np.transpose(C))
    print(np.transpose(D))
#zad2()
#zad3
def zad3():
    A = np.array([[1, 2], [4, 5], [7, 8]])
    B = np.identity(3, int) * 2
    C = np.array([2, 1, 0])
    D = np.array([[3, 2, 1], [0, 5, 6], [8, -1, 2]])
    print(np.trace(A))
    print(np.trace(B))
    #print(np.trace(C)) musi byc macierza kwadratowa
    print(np.trace(D))
#zad3()
#zad4
def zad4():
    x=np.linspace(-2*np.pi,2*np.pi,1000)
    plt.plot(x, np.sin(x), label='sin(x)', color='blue')
    plt.plot(x, np.sin(x + np.pi / 4), label='sin(x + pi/4)', color='red')
    plt.plot(x, np.sin(x + np.pi / 3), label='sin(x + pi/3)', color='green')
    plt.plot(x, np.sin(x + np.pi / 2), label='sin(x + pi/2)', color='purple')

    plt.plot(x, np.cos(x), label='cos(x)', color='black', linestyle='dashed')
    plt.plot(x, np.cos(x + np.pi / 4), label='cos(x + pi/4)', color='orange', linestyle='dashed')
    plt.plot(x, np.cos(x + np.pi / 3), label='cos(x + pi/3)', color='brown', linestyle='dashed')
    plt.plot(x, np.cos(x + np.pi / 2), label='cos(x + pi/2)', color='pink', linestyle='dashed')

    plt.legend()

    plt.show()
#zad4()
#zad5
def zad5():
    def f(x):
        return x**2

    def pochodna(f, x, x0):
        return f(x0) + derivative(f, x0) * (x - x0)

    x=np.linspace(-3,2,100)
    y=f(x)
    points=[-2,0,1]

    plt.plot(x,y, label='f(x)=x^2', color='blue')
    for point in points:
        pochodna_punktu = pochodna(f, x, point)
        plt.plot(x, pochodna_punktu, label=f'Pochodna dla x = {point}', linestyle='--')
    plt.legend()
    plt.show()
#zad5()
#zad6
def zad6():
    def model(x, a, b, c):
        return a*np.log(x+b)+c

    x=np.array([0.1,0.4,0.7,1.0,1.3,1.6,1.92,2.22,2.53,2.83,3.14,3.44,
3.74,4.05,4.35,4.66,4.96,5.26,5.57,5.87,6.18,6.48,6.78,7.09,7.39,
7.7,8.0,8.3,8.61,8.91,9.22,9.52,9.83,10.13,10.43,10.74,11.04,11.35,
11.65,11.95,12.26,12.56,12.87,13.17,13.47,13.78,14.08,14.39,14.69,
15])
    y=np.array([0.09,0.57,0.97,1.29,1.57,1.82,2.04,2.24,2.42,2.58,2.74,
2.88,3.01,3.13,3.25,3.36,3.47,3.57,3.66,3.75,3.84,3.92,4.00,4.08,
4.15,4.22,4.29,4.36,4.42,4.48,4.54,4.60,4.66,4.72,4.77,4.82,4.87,
4.92,4.97,5.02,5.06,5.11,5.15,5.20,5.24,5.28,5.32,5.36,5.40,5.44])
    popt,pcov = curve_fit(model, x, y)
    print(f"Parametry modelu a={popt[0]}, b={popt[1]}, c={popt[2]}")
#zad6()
#zad7
def zad7():
    def model(x, a, b, c):
        return a * np.log(x + b) + c

    x = np.array([0.1, 0.4, 0.7, 1.0, 1.3, 1.6, 1.92, 2.22, 2.53, 2.83, 3.14, 3.44,
                  3.74, 4.05, 4.35, 4.66, 4.96, 5.26, 5.57, 5.87, 6.18, 6.48, 6.78, 7.09, 7.39,
                  7.7, 8.0, 8.3, 8.61, 8.91, 9.22, 9.52, 9.83, 10.13, 10.43, 10.74, 11.04, 11.35,
                  11.65, 11.95, 12.26, 12.56, 12.87, 13.17, 13.47, 13.78, 14.08, 14.39, 14.69,
                  15])
    y = np.array([0.09, 0.57, 0.97, 1.29, 1.57, 1.82, 2.04, 2.24, 2.42, 2.58, 2.74,
                  2.88, 3.01, 3.13, 3.25, 3.36, 3.47, 3.57, 3.66, 3.75, 3.84, 3.92, 4.00, 4.08,
                  4.15, 4.22, 4.29, 4.36, 4.42, 4.48, 4.54, 4.60, 4.66, 4.72, 4.77, 4.82, 4.87,
                  4.92, 4.97, 5.02, 5.06, 5.11, 5.15, 5.20, 5.24, 5.28, 5.32, 5.36, 5.40, 5.44])
    popt, pcov = curve_fit(model, x, y)
    plt.scatter(x, y, label='Punkty', color='blue')
    plt.plot(x, model(x, *popt), label='Model', color='red')
    plt.legend()
    plt.show()
#zad7()
#zad8
def zad8():
    def model(x, a, b, c):
        return a * np.log(x + b) + c

    x = np.array([0.1, 0.4, 0.7, 1.0, 1.3, 1.6, 1.92, 2.22, 2.53, 2.83, 3.14, 3.44,
                  3.74, 4.05, 4.35, 4.66, 4.96, 5.26, 5.57, 5.87, 6.18, 6.48, 6.78, 7.09, 7.39,
                  7.7, 8.0, 8.3, 8.61, 8.91, 9.22, 9.52, 9.83, 10.13, 10.43, 10.74, 11.04, 11.35,
                  11.65, 11.95, 12.26, 12.56, 12.87, 13.17, 13.47, 13.78, 14.08, 14.39, 14.69,
                  15])
    y = np.array([0.09, 0.57, 0.97, 1.29, 1.57, 1.82, 2.04, 2.24, 2.42, 2.58, 2.74,
                  2.88, 3.01, 3.13, 3.25, 3.36, 3.47, 3.57, 3.66, 3.75, 3.84, 3.92, 4.00, 4.08,
                  4.15, 4.22, 4.29, 4.36, 4.42, 4.48, 4.54, 4.60, 4.66, 4.72, 4.77, 4.82, 4.87,
                  4.92, 4.97, 5.02, 5.06, 5.11, 5.15, 5.20, 5.24, 5.28, 5.32, 5.36, 5.40, 5.44])
    popt, pcov = curve_fit(model, x, y)
    integral,error=quad(lambda x:model(x,*popt),1,3)
    print(f"Calka oznaczona z zakresu (1, 3) dla modelu wynosi: {integral}")
    plt.plot(x, model(x, *popt), label='Model', color='red')
    x_calka= np.linspace(1,3,100)
    y_calka=model(x_calka,*popt)
    plt.fill_between(x_calka,y_calka, label='Pole Calki',alpha=0.5)
    plt.legend()
    plt.show()
zad8()