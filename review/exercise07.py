## old way

quadrados = []

for i in range(5):
    quadrados.append(i*3)


print(quadrados)

quadrados = [i * 2 for i in range(5)]
print(quadrados)


numbers = [1,3,56,8,8,4,3456,3245,234,3,123454]
evens = [e for e in numbers if e % 2 == 0]

print(evens)


