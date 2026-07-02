class Vehicle:
    def __init__(self, plate, is_motocycle = False):
        self.plate = plate
        self.is_motocycle = is_motocycle
        self.hours_parked = 0

    def calculate_free(self):

        if self.is_motocycle == True:
            value_hour = 3
            return self.hours_parked * value_hour
        else:
            value_hour = 5
            return self.hours_parked * value_hour
        
    def park_hour(self):
        self.hours_parked += 1
        print(f"Veiculo estacionado a {self.hours_parked} horas!")

    def can_leave(self):
        if self.hours_parked > 0:
            return True
        else:
            return False
        
    def checkout(self):
        if self.can_leave():
            print(f"Pode sair! Placa {self.plate} - Total: R${self.calculate_free()}")
        else:
            print("Veículo não estacionado, nada a pagar!")


car1 = Vehicle("RVB6F67", False)
car1.park_hour()       
car1.park_hour()
car1.checkout()       