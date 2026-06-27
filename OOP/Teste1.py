class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Hello, my name is {self.name} e I have {self.age} years old!")


person_one = Person("LUIS", 31)
person_one.show_info()

