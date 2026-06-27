class Employee():
    def __init__(self, name, salary_base):
        self.name = name
        self.salary_base = salary_base

class Manager(Employee):
    def salary_final (self):
        return self.salary_base * 1.50

    def __str__(self):
        return f"The final salary's Manager {self.name} is R${self.salary_final():.2f}"

class Trainee(Employee):
    def salary_final (self):
        return self.salary_base * 0.80

    def __str__(self):
        return f"The final salary's Trainee {self.name} is R${self.salary_final():.2f}"    



luis_gerente = Manager("LUIS", 2000)
print(luis_gerente)