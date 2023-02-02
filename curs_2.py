#bancomat
#verificam username si parola
#user-ul are doua incercari de a-si introduce username-ul si parola
#daca userul isi poate scoate o suma mai mica sau egala cu soldul curent
#daca introducem o suma mai mare poate sa aleaga daca sa mai reincerce sau nu
#la a doua incercare daca user-ul introduce o suma prea mare, se iese din program


# expected_user_name = 'username'
# expected_password = 'password'
# sold = 5000
# username = input('Introduceti username:')
# if username == expected_user_name:
#     print (f'username corect')
# else:
#     print(f'Username incorect')
#     username = input('Introduceti username:')
#     assert username == expected_user_name, 'Username gresit a doua oara'
# password = input('Introduceti parola:')
# if len(password) != len(expected_password):
#     print(f'parola gresita')
#     password = input('Introduceti parola: ')
#     assert password == expected_password, 'Parola gresita a doua oara'
# elif password == expected_password:
#     print(f'Parola corecta')
# else:
#     print(f'parola gresita')
#     password = input('Introduceti parola: ')
#     assert password == expected_password, 'Parola gresita a doua oara'
# suma_extrasa =int(input('Introduceti suma dorita:'))
# if suma_extrasa <= sold:
#     print(f'Tranzactie reusita')
# else:
#     print(f'Suma dorita depaseste soldul curent')
#     incercare = input('Doriti sa reintroduceti suma?')
#     if reincercare == 'Da':
#         suma_extrasa= int(input('Introduceti suma:'))
#         assert suma_extrasa<= sold, 'Suma dorita depaseste soldul curent'
#         print('Tranzactie acceptata')
#     elif reincercare =='Nu':
#         print('Multumesc')
#
#        #simplificarea codului prin aplicarea operatorilor logici
#     if len(password)==len(expected_password) and password==expected_password:
#         print('Parola corecta')
#     else:
#         print('parola gresita')

#import random

dice_number = [1,2,3,4,5,6]
dice_roll = random.choice(dice_number)
number = int(input('Introduceti un numar de la 1 la 6: '))
if number< dice_roll:
    print(f'Ai pierdut, ai ales un numai mic. Ai ales {number}, dar a fost {dice_roll}')
elif number > dice_roll:
    print(f'Ai pierdut, ai ales un numai mmare. Ai ales {number}, dar a fost {dice_roll}')
else:
    print(f'Ai ghicit! Ai ales {number} si a fost {dice_roll}')