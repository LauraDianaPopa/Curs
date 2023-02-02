# #Functia simpla(fara parametri si return)
def hello_world():
    print('Hello world!')
#hello_world()
#
# #fara () functia nu va fi executata
# # daca o functie nu este apelat, codul din interiorul ei, nu va fi execuatat
#
# x = hello_world() # codul din functie va fi executat
# print(x) #x va luat valoare none(fuctia nu returneaza nimic)

# def say_hi_name(name):# name este un parametru
#     print(f'Hi my name is {name} ')
# say_hi_name('Cosmin')# cosmin este un argument
# lista_nume = ['Iuliana', 'Cosmin', 'Andrei']
# say_hi_name(lista_nume)
# for nume in lista_nume:
#     say_hi_name(nume)

#definim o functie care sa ne zica daca un numar de la tastatura este par sau impar

# def is_even():
#     numar= int(input('Introduceti un numar: '))
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
# is_even()
#
# def is_even_2(numar):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
# argument_numar= int(input('Introduceti un numar: '))
# y = is_even_2(argument_numar)
# print(y)

# if is_even_2(2) == True:
#     print

# functie ce returneaza suma elementelor dintr-o lista

def suma_numere(lista_numere):
    suma = 0
    for numar in lista_numere:
        suma += numar
    return suma
#print(suma) # nu o recunoaste fara return decat in functie
# lista_1 = [1, 2, 3, 4]
# print(suma_numere(lista_1))
# lista_2 = [7, 10, 3, 4]
# print(suma_numere(lista_2))

#  # cream o functie care returneaza valoarea maxima dintr-o lista

# def nr_maxim(lista):
#     maxim = 0
#     for numere in lista:
#          if maxim < numere:
#              maxim = numere
#     return maxim
# lista_2 = [7, 10, 3, 4]
# print(f'Numarul maxim este {nr_maxim(lista_2)}')

#definim o alta functie maxima
def numar_maxim_2(*numere):
    maxim = 0
    for numar in numere:
        if numar > maxim:
              maxim = numar
    return maxim, 'numar maxim'
# n,string = numar_maxim_2(1,2,3,4,5)
# numar_maxim_2(7, 10, 3, 4)
# print(numar_maxim_2(1,2,3,4,5,20,30))
# print(n)
# print(string)

# varialbila globala = variabila care poate fi folosita in interiorul oricarei functii
var_globala = 30
# print(str(var_globala),'din afara functiei')

def dumy():
    # var_globala = 60
    # print(str(var_globala),'din interiorul functiei')
# valoarea variabilei globale ramane nemodificata in afara functiei
# pentru a modifica valoarea variabilei globale in interiorul unei functii, folosim keywordul global
    global var_globala
    print(var_globala)
# dumy()
# print(var_globala)

def say_my_age(age = 10):
    print(age)
say_my_age()
say_my_age(30)

'''
def - keyword care anunta inceputul unei functii
say_my_age - numele functiei(este dat de catre user si poate fi orice nume)
            - in general numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care putem sa specificam parametri(parametri sunt optionali)
 :  - repr. inceputul corpului functiei 
 corpul functiei (asemanator structurilo if, while, for)
           
'''