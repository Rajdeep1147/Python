class Student:
    collage_name = "ABC Name"
    #parameter Constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Enter New Student in Database")

    def welcome(self):
        print("Welcome student,", self.name)

    def getMarks(self):
       return self.marks        

s1 = Student("Karan",97)
s2 = Student("Arjun",88)


# print(s1.name,s1.marks,s1.collage_name)
# print(s2.name,s2.marks)

s1.welcome()
print(s1.getMarks())

 