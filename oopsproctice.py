# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod  # this will make the function static
#     def hello():
#         print("THis is Hello Method")
            

#     def getAvarage(self):
#         sum = 0
#         for value in self.marks:
#             sum +=value    
#         print("Hii",self.name,"Your Avrage Score is ",sum/4 )    

# s1 = Student("Rajdeep Rangra",[98,78,60,94])

# s1.getAvarage()
# s1.hello()


# class Car:
#     def __init__(self):
#         self.acc = False  #Example of Abraction
#         self.brk = False  #Example of Abraction
#         self.cluch = False  #Example of Abraction

#     def start(self):
#         self.acc =True   #Example of Abraction
#         self.brk =True   #Example of Abraction
#         print("Car Start")

# c1 =Car()
# c1.start()


# class Account:
#     def __init__(self,balance,acc_num, acc_pass):
#         self.balance = balance
#         self.acc_num = acc_num
#         self.__acc_pass = acc_pass   #private variable  

#         print("This is Bank Account")

#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs",amount ,"was debited from",self.acc_num , "account")
#         print("Total Balance =",self.getBalance())


#     def credit(self,amount):
#         self.balance += amount
#         print("Rs",amount ,"was credited from",self.acc_num,  "account")
#         print("Total Balance =",self.getBalance())

#     def getBalance(self):
#         return self.balance
    
#     def resetPassword(self):
#        print(self.__acc_pass)
   

# acc1 = Account(10000,12345,"abc123")



# acc1.debit(1000)
# acc1.credit(500)
# print(acc1.getBalance())


class Person:
    __name = "Rajdeep Rangra"  # private variable

    def __hello(self):
        return f"Hello, this is a private method. My name is {self.__name}"

    def welcome(self):
        return self.__hello()

p1 = Person()
print(p1.welcome())                  # Accessing via method
print(p1._Person__name)              # Accessing directly (not recommended outside debugging/testing)

