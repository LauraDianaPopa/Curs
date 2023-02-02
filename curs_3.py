lista1 = ["Maria", 32, True, 12.5 ]

#printeza numarul de elemente din lista de mai sus
0#1print(len(lista1))
# #afiseaza primul si ultimul element
# print(lista1[0])
# print(lista1[-1])

#stergem primul element din lista
#lista1.remove(lista1[0])
#print(lista1)
# lista1.pop(0)
# print(lista1)
# first_element = lista1.pop(0)
# print(first_element)
# first_element = lista1.remove(lista1[0])
# print(first_element)

#adaugam un nou eelement la finalul listei

# lista1 = lista1 + ['Ion']
# print(lista1)
# lista1.append(21)
# print(lista1)
# lista1.extend([1,2,3,4])
# print(lista1)

# #adaugam un element pe pozitia cu indexul 2
# lista1.insert(2, '32')
# print(lista1)

# #verificam daca nr.32 apare de mai mutl de o singura data
# assert lista1.count (32) >1, 'numarul 32 nu apare mai mult decat o singura data'
#
# if lista1.count(32)>1:
#     print('Numarul 32 apare mai mult de o singura data')
# else:
#     print('Numarul 32 nu apare mai mult de o singura data')
#
# lista1.reverse()
# print (lista1)

# Dictionar
#cream un dictionar cu doua elemente, cheile sunt nr. intregi iar valorile zile ale saptamanii
# dictionar1 = {'ziua1':'luni','ziua2':'marti'}
# print(dictionar1)
# print(dictionar1.keys())
# print(dictionar1.values())
#adaugam cheia cu valoarea miercuri

# dictionar1 = dictionar1+ {2:'miercuri'} = arunca o eroare
# print(dictionar1)

# dictionar1.update({2:'miercuri'}) = arunca o eroare
# print(dictionar1.update({2:'miercuri'})) #= nu returneaza nimic(mai clar la cursul de functii)
# dictionar1.update({2:'miercuri'})
# print(dictionar1)

#eliminarea unui element(avem nevie sa cunoastem cheia
# dictionar1.pop(0)
# print(dictionar1)
# print(dictionar1.popitem())#returneaza elem ultimul si il elimina ultima valoare
# print(dictionar1)

#verificam dacacheia 0 se afla in dictionar
# print(dictionar1['ziua1'])
# if 0 in dictionar1.keys() :
#     print(f'Cheia 0 exista si vrem sa afisam valoarea {dictionar1.get(0)}')
# else:
#     print('Cheia nu exista')

#verificam daca valoarea luni se afla in dictionar
# if 'luni' in dictionar1.values():
#     print('Valoarea luni exista in dictionar')
# else:
#     print('Valoarea luni nu exista')

#Seturi

new_set = set()# metoda de a declara un set gol
#
# #adaugam elemente in set
new_set.update([1,2,3,4,5,6,1])
print(new_set) # seturile nu accepta duplicate
new_set.add(7)
print(new_set)
# new_set.add(0)
# print(new_set)
new_set2 = {'martie', 'aprilie'}
print(new_set2)
# #new_set.update(new_set2)
# #print(new_set)
# print('new_set2 - new_set '+ str(new_set2.difference(new_set))) #returnaza un al treile set ce contine new_set2-new_set
# print('new_set - new_set2 ' + str( new_set.difference(new_set2)))
#
# #intersectia a doua seturi
# intersection_set = new_set.intersection(new_set2)
# # print(new_set.intersection(new_set2))
# print(intersection_set)
# #verificam daca elementul cu valoarea 3 este in new_set
# if 3 in new_set:
#     print('este')
# else:
#     print('nu este')
#
#tuple
#cream tuple
# tupla = tuple()
# tupla2 = ()
# print(type(tupla))
# print(type(tupla2))
#
# tupla = (10,20,30,40)
# print(tupla)
# print(tupla.count(30))
# #accesam ultimul element
# print(tupla.index(40)) # returneaza indexul valorii respective
# print(tupla[-1])
# tupla_nested = (10,20,30,40,(1,2,('ianuarie', 'februarie'),3,4))
# print(tupla_nested)
#
# #accesam elementul 3
# print(tupla_nested[4][3])
# print(tupla_nested[4][2][1])
#
# #verificam daca elementul 40 este in tupla noastra
#
# if  40 in tupla_nested:
#     print('40 este')
# else:
#     print('40 nu este')
#
# if (1,2,('ianuarie', 'februarie'),3,4) in tupla_nested:
#     print('yes')