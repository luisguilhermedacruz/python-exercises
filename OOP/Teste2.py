class Score():
    def __init__(self, time_a, time_b):
        self.time_a = time_a
        self.time_b = time_b
        self.gols_a = 0
        self.gols_b = 0

    def gol_a(self, gol):
        self.gols_a += gol
    
    def gol_b(self, gol):
        self.gols_b += gol

    def vencedor(self):
        
        if self.gols_a == self.gols_b:
            return f"O time {self.time_a} tem {self.gols_a} e o time {self.time_b} também tem {self.gols_b}. Desta forma o jogo está empatado!"
        elif self.gols_a > self.gols_b:
            return f"Com {self.gols_a} o time {self.time_a} é o vencedor"
        else:
            return f"Com {self.gols_b} o time {self.time_b} é o vencedor"
        
    def __str__(self):
        return f"PLACAR ATUAL: {self.time_a}:{self.gols_a} X {self.time_b}:{self.gols_b}"  


jogo1 = Score("SPFC", "CORINTHIANS")
print(jogo1)
jogo1.gol_a(4)
jogo1.gol_b(1)
print(jogo1.vencedor()) 
print(jogo1) 
