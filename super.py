# Super Keyword is a built-in function in Python that allows you to call methods from a parent class in a child class.
# It is commonly used in inheritance to access methods and properties of the parent class.
# The super() function returns a temporary object of the superclass that allows you to call its methods.


#multiple inheritance
# class A:
#     varA = "Welcome to the Class A"

# class B:
#     varB = "Welcome to the Class B"    

# class C(A, B):
#     varc = "Welcome to the Class C"

# c1= C()

# print(c1.varA)  # This will print "Welcome to the Class A" due to method resolution order (MRO)
# print(c1.varB)  # This will print "Welcome to the Class B" due to method resolution order (MRO)
# print(c1.varc)  # This will print "Welcome to the Class C"  


class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")    


class ToyotaCar(Car):     
    def __init__(self, name,type):
        super().__init__(type)
        self.name = name  
        super().start()
        super().stop()

        

c1= ToyotaCar("Prius", "Toyota Camry")  
print(c1.type)  # Output: Toyota Camry
