zen_pythona = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious
way to do it.
Although that way may not be obvious at first unless
you’re Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a
good idea.
Namespaces are one honking great idea—let’s do more
of those!"""
def zad1():
    print("Hello world")
def zad2():
    print(zen_pythona)
def zad3(a,b):
    print(f'{a+b=}')
    print(f'{a-b=}')
    print(f'{a*b=}')
    print(f'{a/b=}')
def zad4():
    a = [x for x in range(0,10)]
    b = [complex(0,x) for x in range(0,10)]
    c = [x/10 for x in range(0,10)]
    print(a)
    print(b)
    print(c)
def zad5():
    print(zen_pythona.upper())
def zad6():
    print(zen_pythona.title())

def zad7():
    print(zen_pythona.replace(" ", "").replace("\t", "").replace("\n", ""))

def zad8():
    liczba = 45
    print(f"Liczba 45 binarnie: {bin(liczba)}")
    print(f"Liczba 45 ósemkowo: {oct(liczba)}")
    print(f"Liczba 45 szesnastkowo: {hex(liczba)}")
