'''
Exceptie = clase speciale din Python folosite atunci cand ceva nu merge bine in cod
Folosim try-except pentru a gestiona posibilele exceptii(erori) aruncate in codul nostru,
astfel incat programul sa NU se opreasca

'''
#
# lista_numere = [1,2,3,4,5]
# # print(lista_numere[10]) # va sari o eroare pentru ca in lista nu exista indexul 10
# # print("Am trecut de exceptie")  # Nu se executa acest cod
# try:
#     print(lista_numere[10])
# except Exception as e:
#     print(e)
#
# print("Am trecut de exceptie")
#
# try:
#     print(lista_numere[10])
# except IndexError as error:
#     print("Index Error: ",error)
#
# # try:
# #     print(lista_numere[10])
# # except NotImplementedError as e:  # aceasta exceptie nu este prinsa in try.
# #     print(e)
# numar_studenti = int(input("Introduceti numarul de studenti: "))
# lista_studenti = []
#
# for student in range(numar_studenti):
#     if student > 5:
#         print(lista_studenti)
#         raise IndexError("Nr de stundeti sa nu fie peste 5")
#     lista_studenti.append("Vlad")
#     print(student)
#
# print(lista_studenti)

###Mostenire

'''
mostenire =  capacitatea unei clase de a impartasi atat metode cat si atribute din alta clasa
clasa copil mosteneste clasa parinte astfelclasa copil preia metodele si atributele din clasa parinte
clasa copil poate avea oricate metode sau atribute in plus fata de clasa parinte
clasa parinte nu mosteneste nimic de la clasa/clasele copil
In python o clasa copil poate mosteni mai multe clase parinte cu virgula intre ele
class copil(Parinte1, Parinte2, Parinte3)

in clasa copil putem apela clasa parinte folosind super()
'''
class Person:
    def __init__(self, nume, varsta, adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa
    def anu_nasterii(self):
        return 2023 - self.varsta

    def descriere(self):
        print(self.nume, self.varsta, self.adresa)

class Student(Person):
    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        # super() reprezinta clasa parinte in cazul nostru Person
        #cu super apelam instructorul clasei parinte
        super().__init__(nume,varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descriere(self):# fac suprascriere la metoda "descriere" din clasa parintelui
        super().descriere()
        print(self.facultate, self.an_studiu)

class Angajat(Person):
    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu
    def descriere(self):
        super().descriere()
        print(self.companie, self.salariu)

    def salariu_anual(self):
        return self.salariu* 12

class Profesor (Angajat):
    def __init__(self, nume, varsta, adresa, companie, salariu, curs, nr_ore):
        super().__init__(nume, varsta, adresa, companie, salariu)
        self.curs = curs
        self.nr_ore = nr_ore

profesor = Profesor("vlad",33,"Adresa1","IT Factory", 1000, "Testare Automata", 160)
profesor.descriere()
print(str(profesor.salariu_anual()) + " Euro")
student = Student("vlad", 22, "adresa", "UTCM", 3)
print(student.nume)
print(student.facultate)
student.descriere()

#Abstractizare - Polimorfism

'''
Polimorfism = poli (mai multe) morfism (forma/forme) => ceva care poate lua mai multe forme
In cazul OOP, o meroda poate sa aibe acelasi nume in lcase diferite dar implementari/logica diferita in interior

Abstractizarea este un proces prin care putem sa ascundem o anumita functionalitate specifica fata de utilizator
De asemenea putem forta un anumit comportament in clasele copil.

Utilizatorul stie ce face functionalitatea, dar nu si cum.

Clasa parinte care este o clasa abstracta, nu putem sa cream obiecte din ea, ci doar sa o folosim ca un template pentru clasele copil

In abstractizare avem 2 concepte:
- Interfata -> contine doar metode abstracte, in java exista inerfete propriu-zise(interface...)
- Clasa Abstracta -> contine atat metode abstracte cat si metode proprii, cu logica, in java exista abstract class numeclasa

Clasa abstracta trebuie sa mosteneasca clasa ABC (Abstract Class Method)
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplementedError sau pass
Clasa abstracta NU are constructor pentru ca nu cream obiecte din ea

O metoda abstracta e o metoda care nu are corp (fara logica)
'''

from abc import ABC, abstractmethod

class Vehicul(ABC):

    @abstractmethod     #decorator ca sa marcam acesta metoda ca abstracta
    def nr_roti(self):
        raise NotImplementedError

    @abstractmethod
    def nr_locuri(self):
        pass                     # metode abstracte neavand logica si pentru a preveni anumite erori,
                                 # scriem in corpul metodelor pass sau NotImplementedError

    @classmethod
    def metoda_logica_proprie(self):
        print("Aici este o metoda cu logica proprie, nu trebuie implementata in clasa copil")
class Masina(Vehicul):

    def init(self,culoare):
        self.culoare= culoare

    def nr_roti(self):
        return 4

    def nr_locuri(self):
        return 5
class Bicicleta(Vehicul):
    def init(self,culoare,roti_ajutatoare = False):
        self.culoare = culoare
        self.roti_ajutatoare = roti_ajutatoare

    def nr_roti(self):
        if self.roti_ajutatoare: # echivalentul lui: self.roti_ajutatoare == True
            return 4
        else:
            return 2

    def nr_locuri(self):
        return 1
masina = Masina("verde")
print(masina.nr_roti())
print(masina.nr_locuri())
masina.metoda_logica_proprie()

bicicleta = Bicicleta("rosu")
print(bicicleta.nr_roti())
print(bicicleta.nr_locuri())
bicicleta.metoda_logica_proprie()

# vehicul = Vehicul() # NU putem crea un obiect de tipul clasei abstracte.

### INcapsulare
'''
Incapsulare = posbilitatea de a PROTEJA atrbutele/metodele unei clase, folosind meodificatorii de vizibilitate

- private (privat, adica atributul/metoda poate fi accesata doar din interiorul clasei in care a fost definit)
          -- se defineste cu underscore in fata (variabila sau metoda(): )
- protected (protejat, atributul/metoda poate fi accesata din calasa in care a fost defnita,
            dar si din clasele copil ale acesteia, INSA NU din exterior)

Atunci cand avem un atribut ascuns putem folosi metode speciale pentru a interactiona cu el:
Numite getter, setter si delter
getter -> pe a-l vedea/ a avea acces la atribut
setter -> pentru a-i schimba valoarea
delter -> pentru a sterge valoarea

Conventie: aceste metode trebuie denumite cu set,delete si get_ + numele variabilei
'''
class Car:

    variabila_privata = "privat"
    _variabila_protected = "protected"

    def init(self,var_protected):
        self._variabila_protected = var_protected
    #getter
    def get_variabila_privata(self):
        return self.variabila_privata
    #setter
    def set_variabila_privata(self,var):
       self.variabila_privata = var

    #deleter
    def delete_variabila_privata(self):
        self.variabila_privata = None


masina = Car('Update Protected')
# print(masina._variabila_protected)   # convetie ca aceasta variabila sa nu fie accesata.

# print(masina.__variabila_privata)   #-> eroare, variabilele private nu avem acces

print(masina.get_variabila_privata())
masina.set_variabila_privata("Update Private")

print(masina.get_variabila_privata())
masina.delete_variabila_privata()

print(masina.get_variabila_privata())

# "------------------------------------------------------------------"
# Getter, setter, delete intr-un mod pythonic

class CarPy:

    def init(self,color):
        self.color = color
        self.nr_roti = 0
    @property
    def color(self):
        return self.color

    @property
    def nr_roti(self):
        return self.nr_roti

    @color.getter
    def color(self):
        print(f"Getter: Culoare {self.color}")
        return self.color

    @color.setter
    def color(self,color):
        print(f"setter: Setam culoarea in {color}")
        self.color = color

    @color.deleter
    def color(self):
        self.color =None


car_py = CarPy("negru")
car_py.color
car_py.color = "Albastru"
car_py.color
del car_py.color
car_py.color
