class Persoana():
 #atribute
    nume = ''
    prenume = ''
    varsta = 0

    def __init__(self,nume,prenume,varsta):
        self.nume = nume  # self.nume este atributul obiectului instantiat,
                          # iar nume este parametrul functiei init,
                          #prin acest parametru atribuim o valoare atribtului self.nume
        self.prenume = prenume
        self.varsta = varsta

    def __str__ (self):
        return f"Numele meu este {self.nume}. Prenume: {self.prenume}. Varsta: {self.varsta}"
    def varsta_peste_10_ani(self):
        return self.varsta + 10


andrei = Persoana("Slavescu","Andrei",24)
print(andrei.nume,andrei.prenume,andrei.varsta)
andrei.nume = 'Slavescu_modificat'
print(andrei.nume,andrei.prenume,andrei.varsta)

# florica = Persoana('Vladimiresc', 'Florica', 55)
# print(florica.nume, florica.prenume, florica.varsta)
# print(andrei)
# andrei.varsta_peste_10_ani()