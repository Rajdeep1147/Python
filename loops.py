#Break Statement
# i = 1
# while i<=10:
#     print("Rajdeep Rangra",i)
#     if i == 5:
#         break
#     i += 1  # Increment i by 1 to avoid an infinite loop 

# k = 1
# while k <= 100:
#     print("This is an infinite loop",k)  # This will run indefinitely
#     k += 1 

# i= 1
# n= int(input("Enter the Number You want to Print the Table: "))
# while i<=10:
#     print(i,"X",n ,"=",i*int(n))
#     i += 1  # Increment i by 1 to avoid an infinite loop

# k = 1
# while k<=10:
#     j = k*k
#     k += 1  # Increment k by 1 to avoid an infinite loop
#     print([j])  
  



# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# n = int(input("Enter the number you want to find: "))

# i = 0  # Start index
# found = False  # Flag to track if number is found

# while i < len(num):
#     if num[i] == n:
#         print(f"The number is present in the tuple at index {i}.")
#         break
#     i += 1

# if not found:
#     print("The number is not present in the tuple.")


# #Countinue Statement
# a = 1
# while a<=5:
#     if(a%2==0):
#         a+=1
#         continue
#     print(a)
#     a+=1


# For Loop
tup = (1,2,3,4,5)
x= 1
idx = 0
for val in tup:
    if(val==x):
        print("value found at index",idx)
        break
    idx += 1
else:
    print("Number not found")    

 

n = int(input("Enter the number: "))
i = 1
s = 0

while i <= n:
    s += i
    i += 1

print("Sum of numbers from 1 to", n, "is:", s)


h = 5
fact = 1

for  z in range(1,h+1):
    fact *= z
print("Factorial =",fact)    