"""

structuri repetitive= modalitati prin care putem executa un cod in mod repetat pana cand o anumita conditie nu mai este indeplinita
structuri repetitive
1. while
2. do while(nu este scopul cursului)
3. for
4. for each

Modaitati de control al structurilor repetitive
1. Break(opreste executarea structurii repetitive)
2. Continue (face skip la o iteratie)
"""
"""
while este o sctructura repetitiva in care executam o serie de instructiuni atata timp cat conditia este adevarata
De regula elementul sau variabila de control al whil-lului se declara inainte de acesta sau inafara lui.

"""
# Exercitiul 1: Printeaza pe ecran toate nr. de la 1-10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#Debugging = proces prin care analizam codul pentru a vedea cum circula datele.
#DE fiecare data cand vrem sa facem debugging putem sa punem breakpoint(bulinuta rosie)

#Exercitiul 2: Suma numerelor de la 1-500
# i = 1
# suma = 0
# while i <= 500:
#     suma += i
#     i+=1
# print(suma)

#Ex.3: Facem o lista cu lunile anului si sa o parcurgem si sa printam fiecare valoare din lista
#lista1 = ['ianuarie', 'februarie', 'martie','aprilie', 'mai','iunie', 'iulie']
#index = 0
# while index < len(lista1):
# print(lista1(index)
# # # index +=1
# #parcurgem lista fara a afisa luna martie si luna mai
# while index < len(lista1):
#     if lista1[index] == 'martie' or lista1[index] == 'mai':
#         index+=1
#         continue
#     print(lista1[index])
#     index+=1

#parcurgem lista pana ajungem la luna aprilie
# while index < len(lista1):
#     if lista1[index] == 'aprilie':
#      break
#     print(lista1[index])
#     index+=1

#inlocuim luna mai cu luna noiembrie, Presupunem ca exista numai o singura luna de mai
# while index < len(lista1):
#     if lista1[index] == 'mai':
#         lista1[index] = 'noiembrie'
#         break
#     index += 1
# print(f'Lista finala este {lista1}')


"""
For-ul este o structura repetitiva care este utilizata atunci cand vrem sa parcurgem o structura de date
cu scopul de a prelucra datele din acea structura de date
De asemenea poate fi folosit sa executam un set de instructiuni de un numar finit de ori(range)
Structura unui for 
-Incepututl structurii repetitive for
-Variabila de iteratie
-Incepututl range-ului de parcurs(defoult = 0 - optional)
-Sfarsitul range-ului de parcurs(obligatoriu)
-Capatul superior nu este luat in considerare
-Pasul range-ului care defoult este 1
"""
#Ex 1. Sa parcurgem toate numerele de la 0 la 10 si sa printam separat numerele pare de cele impare
# for i  in range(11):
#     if i%2 == 0:
#         print(f'numarul {i} este par')
#     else:
#         print(f'numarul{i} este impar')

#Ex. 2. Nested list sau embedded list sau lista imbricata sau matrice
# matrice = [
#     [1,"test1"],
#     [2, "test2", 3],
#     [5, 6, 7]
# ]
# for i in range(len(matrice)):
#     for j in range(len(matrice[i])):
#         print(f'Valoarea de pe pozitia [{i}][{j}] este {matrice [i][j]}')

# luni = ['ianuarie', 'februarie', 'martie','aprilie', 'mai','iunie', 'iulie']
# for i in range (len(luni)):
#     print(luni[i])
# for luna in luni:
#    print(luna)

# lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
#                             "orange", "verde", "indigo"]
# liste_culori_de_exclus = ["rosu", "galben", "roz"]
# lista_culori_neexcluse = []
# for culoare in lista_culori_disponibile:
#     if culoare in liste_culori_de_exclus:
#         continue
#     lista_culori_neexcluse.append(culoare)
# print(lista_culori_neexcluse)


#Ex7. Algoritmi de sortare si algoritmi de cautare

#Ex.6 !!!!!!   Sortam o lista de numere!
#bublesort
lista_nesortata = [1, 5, 10, 2, 50, 11, 20, 12]
# lista_nesortata.sort() #suprascrie lista initiala, nu returneaza nimic
# print(lista_nesortata)

#Le sortam manual

for i in range(len(lista_nesortata)-1):
    for j in range (len(lista_nesortata)-1):
        if lista_nesortata[j] > lista_nesortata [j+1]:
            lista_nesortata[j], lista_nesortata[j+1] = lista_nesortata[j+1], lista_nesortata[j]
print(lista_nesortata)


"""
Recapitulare:
Tupla = structura de date care se defineste intre 2 paranteze (2,5), are indexi dar imutabile
Dictionare = structura de date cu cheie si valoare{cheie:valoare} sunt mutabile, cheile sunt unice, sunt ordonate(aplicatie pentru masini)
seturi = structura de date care are elemente unice, nu sunt ordonate sau indexate, nu putem schimba locatia elementelor, se pot adauga sau sterge elemente(lunile anului)
liste =  structura de date care pastreaza mai multe valori intr-o singura variabila, fiecare element are index, este mutabila"""
