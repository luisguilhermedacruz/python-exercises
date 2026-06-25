texto1 = input("")
texto2 = input("")
texto3 = input("")
texto4 = input("")



def write_files(texto1, texto2: str) -> str:
    with open("text.txt", "w", encoding="utf-8") as file:
        file.write(texto1 + "\n")
        file.write(texto2 + "\n")
        

write_files(texto1, texto2)

def write_stay(texto3, texto4: str) -> str:
    with open("text.txt", "a", encoding="utf-8") as file:
        file.write(texto3 + "\n")
        file.write(texto4 + "\n")

write_stay(texto3, texto4)

with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)