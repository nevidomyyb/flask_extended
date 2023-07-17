class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Representação do objeto em formato de string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"
    
    #Representação do objeto para ser não ambíguo
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)
print(bob)
print(bob.__repr__())
