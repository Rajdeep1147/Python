# This code creates a dictionary with various key-value pairs and prints it.
#This is Unorder 
info = {
    "name":"Rajdeep",
    "age": 25,
    "city":"Hamirpur",
    "hobbies": ["reading", "coding", "gaming"],
    "is_student": False,
}

info["name"] = "Tanu Singh"  # Ovrright the name
# print(info)

nullDict = {}  # Create an empty dictionary
nullDict["name"] = "Apna College"  # Add a key-value pair to the empty dictionary
# print(nullDict)

student = {     
    "name": "Arjun",
    "age": 20,
    "subjects": {
        "math": 85,
        "science": 90,
        "english": 88
    },
    "is_enrolled": True,
}

# print(student)
# print(student['subjects']['math'])  # Access the 'subjects' dictionary

# print(len(student))
# print(student.keys())  # Get all keys in the dictionary
print(student.values())  # Get all values in the dictionary

print(student.get("name"))  # Get the value associated with the key 'name'
print("After")  # Get the value for 'address', return "Not Found" if key doesn't exist
new_dict = {"status": "active", "state": "Himachal Pradesh"}
student.update(new_dict)  # Update the student dictionary with new key-value pairs
print(student)

practice = {
   "cate":"a small cat",
   "table":["a piece of furniture","List of Facts and Figures"],
}
print(practice)

practice2 = {}
addValue = input("Enter the First Value: ")  # Get input from the user
practice2.update({"Math":addValue})  # Add a new key-value pair to the empty dictionary
print(practice2)  # Print the empty dictionary
addValue2 = input("Enter the Second Value: ")
practice2.update({"English":addValue2})  # Add a new key-value pair to the empty dictionary
print(practice2)  # Print the empty dictionary
addValue3 = input("Enter the Third Value: ")
practice2.update({"Science":addValue3})  # Add a new key-value pair to the empty dictionary
print(practice2)  # Print the empty dictionary
