# Property Method we use @property decorator to create a property method to decorate in any method of the class
# This allows us to access the method like an attribute without needing to call it with parentheses
# This is useful for encapsulation and controlling access to class attributes
# Example of a property method in a class
class Student:
    def __init__(self, phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math

    @property
    def percentage(self):
        return (self.phy + self.che + self.math) / 3 

s1 = Student(85, 90, 95)
print(s1.percentage)  # Output: 90.0 

s1.phy = 40
print(s1.percentage)  # Output: 88.33333333333333