course = "Python Course"

#For pritning a message

message = """
Hi,Mosh ... Bla bla bla
"""
#print(message)

#Function is reuseable a piece of code that carries out a task. Exam: Remote of a TV
#Some functions are input and that is called argument
print(len(message))
print(course[0])
print(course[-1]) #That take us to the back of the string
#Slice a string
print(course[0:3]) #It is return a new string containing n charaters which is start from x index and end with y index; that means course[start_index:end_index].
print(course[2:]) #course[start_index:]
print(course[:4]) #course[:end_index]
print(course[:]) #course[:]

#Escape Sequence
name = "Sayan \\\'\"Chy\"" #Backslace is a escape charecter here
print(name)
#\n for new line

#Format the strings
first = "sayanta"
last = "Chowdhury"
#full = first + " " + last
full = f"{len(first)} {last}" #Here we can use any kind od expresion in between curly braces
print(full)

#String Methods
print(course.upper())
#everything In python is object and object has function
#which is known as object and it can be excessible by (Dot) Notation.

print(course.lower().title()) #Tile() make Uppercase the first char
print(course.strip()) #Trim whitespace in end and begining
print(course.find("th"))
print(course.replace("P","j"))
print("yth" in course) #Find substr in Python
print("is" not in course)

