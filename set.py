#set is the collection of unique elements
# it is mutable and unordered sts is mutable but their elements are immutable
# it is used to perform mathematical set operations like union, intersection, difference, etc.
#set are always unique

nums = {1, 2, 13, 4, "Hello","world"}  # Set Ignore duplicate values
print(nums)  # Output: {1, 2, 3, 4,

print(type(nums))  # Output: <class 'set'>  
print(len(nums))

nums.add(7)  
nums.add("apnacollege")  # Add a new element to the set
print(nums)
collection=set
print(type(collection))  # Output: <class 'dict'> (empty dictionary)

print(nums.pop())  # Remove and return an arbitrary element from the set
print(nums)  # Output: Set after popping an element

set1 = {1,2,3}
set2 = {4,3,5}

print(set1.union(set2)) # Perform union operation on two sets
print(set1.intersection(set2)) # Perform intersection operation on two sets


practice = {"Python", "c++", "javascript","Java","Python","Java","c++","c"}
print(len(practice))