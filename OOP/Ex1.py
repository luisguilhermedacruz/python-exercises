class Person:
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

   
    def show_info(self):
        return f'I am a person, my name is {self.name}, I am {self.age} years old and I am {self.status}!'
    
    def change_status(self):
        status_for_use = input("Have you changed your marital status? If so, please type: MARRIED / SINGLE or OTHER? ").lower()

        if status_for_use == 'married':
            self.status = 'married'
        elif status_for_use == 'single':
            self.status = 'single'
        else:
            self.status = 'another type of relationship'


person1 = Person("LUIS", 31, "Single")
print(person1.show_info())
person1.change_status()
print(person1.show_info())
        

    

