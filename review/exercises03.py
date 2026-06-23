name= "Luis"
age = 31
height = 1.78
like_python = True

print(type(name))
print(type(age))
print(type(height))
print(type(like_python))


temp = 15

if temp < 15:
    print("COLD")
elif temp <= 25:
    print("OK")
else:
    print("HOT")





def tabuada(n: int) -> None:
    for i in range (1,10):
        print(f"{n} x {i} = {n * i}")
    
tabuada(7)

