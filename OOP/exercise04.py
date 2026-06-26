class Animal():
    def __init__(self, nome):
        self.nome = nome
    
    def fazerSom(self):
        print("...")
    

class Cachorro(Animal):
    def fazerSom(self):
        print(f"Meu cachorro {self.nome} faz AU AU AU AU")

class Gato(Animal):
    def fazerSom(self):
        print(f"Meu gato {self.nome} faz MIAU MIAU")

rex = Cachorro("REX")
abusado = Gato("ABUSADINHO")

rex.fazerSom()
abusado.fazerSom()




