import ast
class A:
    def method(self):
        print("A")
class B(A):
    pass
class C(A):
    def method(self):
        print("C")
class D(B,C):
    pass
d = D()
#d.method()
class Osoba:
    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def getName(self):
        return self.name
    def getLastName(self):
        return self.last_name
    def getAge(self):
        return self.age
o=Osoba("Jan","Kowalski",25)
class Student(Osoba):
    def __init__(self,indexNr,imie,nazwisko,age):
        Osoba.__init__(self,imie,nazwisko,age)
        self.indexNr = indexNr
    def getIndexNr(self):
        return self.indexNr
s=Student(123,"Jan","Kowalski",25)
#print(s.getName(),s.getLastName(),s.getAge(),s.getIndexNr())
class Note:
    def __init__(self,slownik_ocen):
        self.oceny = slownik_ocen
class Student2(Osoba):
    def __init__(self,indexNr,oceny,imie,nazwisko,age):
        Osoba.__init__(self,imie,nazwisko,age)
        self.indexNr = indexNr
        self.oceny = oceny
oceny1=Note({"Matematyka":4,"Fizyka":3,"Informatyka":5,"Wf":4})
oceny2=Note({"Matematyka":3,"Fizyka":3,"Informatyka":3,"Wf":5})
s1=Student2(123,oceny1,"Jan","Kowalski",25)
s2=Student2(124,oceny2,"Pawel","Laskarzewski",22)
#print(s1.oceny.oceny)
#print(s2.oceny.oceny)
class Employee(Osoba):
    def __init__(self,salary,position,imie,nazwisko,age):
        Osoba.__init__(self,imie,nazwisko,age)
        self.salary = salary
        self.position = position
e=Employee(4000,"Junior Developer","Pawel","Laskarzewski",22)
#print(e.salary)
#print(e.position)
class WorkingStudent(Employee,Student2):
    def __init__(self,salary,position,oceny,nrindeksu,imie,nazwisko,age):
        Employee.__init__(self,salary,position,imie,nazwisko,age)
        Student2.__init__(self,nrindeksu,oceny,imie,nazwisko,age)
WS=WorkingStudent(4000,"Junior Developer",oceny1,125,"Pawel","Laskarzewski",22)
#print(WS.salary,WS.position,WS.oceny.oceny,WS.name,WS.last_name,WS.age,WS.indexNr)
class Group:
    def __init__(self,students):
        self.students = students

    def zapisz_do_pliku(self):
        try:
            with open("grupa.csv","w") as plik:
                for student in self.students:
                    plik.write(str(student.indexNr)+";"+str(student.oceny.oceny)+";"+str(student.getName())+";"+str(student.getLastName())+";"+str(student.getAge())+"\n")
            plik.close()
        except IOError:
            print("Blad zapisu pliku")

s3=Student2(124,Note({"Matematyka":3,"Fizyka":3,"Informatyka":3,"Wf":3}),"Adam","Nowak",23)
studenci=[
    s1,
    s2,
    s3
]
grupa=Group(studenci)
#print(grupa.students[1].getName())
grupa.zapisz_do_pliku()
def odczytaj_z_pliku():
    try:
        with open("grupa.csv", "r") as plik:
            #celowe wywolanie bledu
            #raise FileNotFoundError
            napis = plik.read()
            lista = []
            students = napis.split("\n")
            students.pop(len(students)-1)
            for student in students:
                temp = student.split(";")
                lista.append(Student2(int(temp[0]), Note(ast.literal_eval(temp[1])), temp[2], temp[3], int(temp[4])))
            return Group(lista)
    except FileNotFoundError:
        print("Plik nie istnieje")
    except IOError as e:
        print(e)


grupa2=odczytaj_z_pliku()
#print(grupa2.students[2].oceny.oceny)
class BladOdczytu(Exception):
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku
    def __str__(self):
        return f"Blad odczytu pliku '{self.nazwa_pliku}'"

class BladZapisu(Exception):
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku

    def __str__(self):
        return f"Blad zapisu pliku '{self.nazwa_pliku}'"
try:
    with open("grupa.csv", "r") as file:
        raise BladOdczytu("plik.txt")
except BladOdczytu as e:
    print(e)
try:
    with open("grupa.csv", "w") as file:
        raise BladZapisu("plik.txt")
except BladZapisu as e:
    print(e)