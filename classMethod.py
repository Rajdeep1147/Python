# @classMethod is a Python script that demonstrates the use of class methods.
# Class methods are methods that are bound to the class and not the instance of the class.
# They can be called on the class itself, rather than on an instance of the class.
class Person:
    name = "John Doe"
    
    @classmethod
    def changeName(cls,name):
        # self.name = name
        cls.name = name

p1 = Person()

p1.changeName("Rajdeep Rangra")
print(p1.name)    
print(Person.name)     

       