#function defination

def calSum(a,b): #parameter
    result = a+b

    return result 


print(calSum(5,4)) #function call; arguments


def calAvg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calAvg(98,94,80)



def calProd(a=4,b=12):
    print(a*b)
    return a*b
calProd()

cities = ["Gurgao","Noida","Delhi","Mumbai"]
def listLength(cities):
    print(len(cities))

def printList(cities):
    for item in cities:
        print(item,end=" ")     #end=" " use to show data in one line   
   


printList(cities)

listLength(cities)

# fact = int(input("Enter the number which you the Factorial"))

# def findFact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# findFact(fact)

money = int(input("Enter the Value You want to convert in USD $"))

def convertMoney(money):
    value =86.08
    amount = money/value
    print(amount)
        
convertMoney(money)


#Recersive Function

def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)

show(5)