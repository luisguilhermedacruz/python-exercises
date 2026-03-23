## QUestion 5: 

notas = [7, 8, 5, 10, 6]

def avalia_aluno(notas):
    media = sum(notas)/len(notas)

    if media >= 7:
        return f'Aluno aprovado!'
    else:
        return f'Aluno reprovado!'
    
print(avalia_aluno(notas))
    