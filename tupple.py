# Tupple are imultiple values in a single variable
# They are immutable, meaning they cannot be changed after creation
# Tuples are defined using parentheses ()

tup = (1, 2, 3, 4, 5,2)
print(tup)
print(type(tup))
#how to create singlw value in tuple
single_value_tuple = (1,)  # Note the comma
print(single_value_tuple)

print(tup.index(4))  # Find the index of the value 4 in the tuple
print(tup.count(2))  # Count how many times the value 2 appears in

marks = ("c","D" ,"A","A","B","B","A")
list = ["c","D" ,"A","A","B","B","A"]

print(marks.count("A"))  # Count how many times "A" appears in the list

print(list.sort())  # Sort the list in ascending order
print(list)  # Print the sorted list