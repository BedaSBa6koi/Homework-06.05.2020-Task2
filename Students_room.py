class Student:
    def __init__(self, fullname, age, faculty):
        self.fullname = fullname
        self.age = age
        self.faculty = faculty

    def __str__(self):
        return f'<name: {self.fullname}, age: {self.age}, major: {self.faculty}>'    
    
Steve = Student('Steven Shultz', 23, 'English')
Jhonny = Student('Jonathan Rosenberg', 24, 'Biology')
Penny = Student('Penelope Meramveliotakis', 21, 'Physics')

print(Steve)
print(Jhonny)
print(Penny)


