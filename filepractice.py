# file = open("practice.txt","w")
# data = file.write("Hi Everyone \n we are learning File I/O \n using Java \n I like Programing in Java")
# print(data)

# with open("practice1.txt","w") as f:

#     f.write("Hi Everyone \nwe are learning File I/O \n using Java\n I like Programing in Java") 


#Change the Text in File
# with open("practice1.txt","r") as f:
#     data = f.read()

# datanew = data.replace("Java","Python");   
# print(datanew)

# with open("practice1.txt","w") as f:
#     data = f.write(datanew)

# def check_for_word():
#     word = "learning1"
#     with open("practice1.txt","r") as f:
#         data = f.read()
        
#         if(word in data):
#             print("found")
#         else:
#             print("not found")    

# def check_for_word()


#Check the which line where word Exist
# def check_for_word():
#     word = "learning"
#     data = True
#     with open("practice1.txt","r") as f:
#         while data:
#             data = f.readline() 
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1        

# check_for_word()

#Find the Text in which Line

def check_for_word():
    word = "Programing"
    line_no = 1  # Initialize line number
    with open("practice1.txt", "r") as f:
        while True:
            data = f.readline()
            if not data:  # End of file
                break
            if word in data:
                print(f"Found on line: {line_no}")
                return
            line_no += 1

    return -1  # Word not found

check_for_word()


