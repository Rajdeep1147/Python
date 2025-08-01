# List in Python
# Lists are mutable, It can be changed.
marks = [94.3,89,56,43,78]
# print(marks)
# print(type(marks))
# print(len(marks))

student=["Arjun",86,"Delhi"]
# print(student[0])

# print(marks[1:3])

list = [1,2,4]
list.append(3)
print(list)
list.sort()
list.sort(reverse=True)

print(list)

list.insert(1, 5) # Insert 5 at index 1
# print(list)

list.remove(5) # Remove first 5 from the list
# print(list)

# list.pop(5) # Remove all 5 from the list
# print(list)

# movies = []  # Initialize an empty list to store movie names
# movie1 = input("Enter 1st Movies")
# movie2 = input("Enter 2nd Movies")
# movie3 = input("Enter 3rd Movies")

# movies.append(movie1)  # Add the first movie to the list
# movies.append(movie2)  # Add the second movie to the list
# movies.append(movie3)  # Add the third movie to the list
# print("Your favorite movies are:", movies)  # Print the list of favorite movies

a = [1, 2, 1]
list.copy()  # Create a shallow copy of the list
b = a.copy()  # Copy the list 'a' to 'b'
b.reverse()

if(a == b):
    print("Palindrome")
else:
    print("Not Palindrome")