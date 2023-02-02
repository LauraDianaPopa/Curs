'''
clasa CursProgramare
atribute = companie, nume_curs, numar_locuri_max, studenti
metoda = inscriere_student, descriere_curs, get_locuri_disponibile
'''
from Persoana import Persoana


class CursProgramare():
    def __init__(self, companie, nume_curs, numar_locuri_max):
        self.companie = companie
        self.nume_curs = nume_curs
        self.numar_locuri_max = numar_locuri_max
        self.studenti = []

    def inscriere_studenti(self, nume_student):
        if self.get_locuri_disponibile() > 0:
            self.studenti.append(nume_student)
        else:
            print(f'Nu mai sunt locuri disponibile')

    def descriere_curs(self):
        print(f'{self.companie} - {self.nume_curs}')
        print(30 * '*')
        if len(self.studenti) >0 :
            print(f' Lista studenti: ')
            for student in self.studenti:
                print(f'{student.nume, student.prenume}')
        else:
            print(f' Nu sunt studenti inscrisi!')

    def get_locuri_disponibile(self):
        return self.numar_locuri_max - len(self.studenti)

student1 = Persoana('Matei', 'Vlad',33)
curs_python = CursProgramare('IT Factory', 'Introducere in Python', 10)
curs_python.descriere_curs()
curs_python.inscriere_studenti(student1)
curs_python.descriere_curs()
curs_python.inscriere_studenti(student1)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
student2 = Persoana('Luiza', 'DIana', 29)
print(curs_python.get_locuri_disponibile())
curs_python.descriere_curs()