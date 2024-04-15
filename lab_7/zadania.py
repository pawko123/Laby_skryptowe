
class Osoba:
    def __init__(self,name="Jan",last_name="Kowalski",age=22):
        self.name = name
        self.last_name = last_name
        self.age = age
    def getName(self):
        return self.name
    def getLastName(self):
        return self.last_name
    def getAge(self):
        return self.age
o=Osoba()
class Student(Osoba):
    def __init__(self,indexNr,Osoba):
        super().__init__(Osoba.getName(),Osoba.getLastName(),Osoba.getAge())
        self.indexNr = indexNr
    def getIndexNr(self):
        return self.indexNr
s=Student(123,Osoba())
print(s.getName(),s.getLastName(),s.getAge(),s.getIndexNr())
class Note:
    def __init__(self,slownik_ocen):
        self.oceny = slownik_ocen
class Student2(Osoba):
    def __init__(self,indexNr,Osoba,oceny):
        super().__init__(Osoba.getName(),Osoba.getLastName(),Osoba.age)
        self.indexNr = indexNr
        self.oceny = oceny
oceny1=Note({"Matematyka":4,"Fizyka":3,"Informatyka":5,"Wf":4})
oceny2=Note({"Matematyka":3,"Fizyka":3,"Informatyka":3,"Wf":5})
s1=Student2(123,Osoba(),oceny1)
s2=Student2(124,Osoba("Pawel","Laskarzewski",22),oceny2)
print(s1.oceny.oceny)
print(s2.oceny.oceny)
class Employee(Osoba):
    def __init__(self,salary,position,Osoba):
        super().__init__(Osoba.getName(),Osoba.getLastName(),Osoba.getAge)
        self.salary = salary
        self.position = position
e=Employee(4000,"Junior Developer",Osoba())
print(e.salary)
print(e.position)
class WorkingStudent(Employee,Student):
    def __init__(self,salary,position,Osoba,oceny,nrindeksu):
        super().__init__(salary,position,Osoba)
        Student.__init__(self,)