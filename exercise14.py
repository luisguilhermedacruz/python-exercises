class Carro:
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self):
        return f'O carro do modelo {self.modelo} está acelerando a velocidade de {self.velocidade}'
    

carro1 = Carro("Civic", 400)
print(carro1.acelerar())