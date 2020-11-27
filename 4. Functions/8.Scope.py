value = "Sayan"

def greet(name):
    message = f"Welcome {name}" #Local Variable
    return message


def sentEmail(name):
    global value # Declaration for update Global Variable Value 
    value = "Chowdhury"
    message = f"Hi {name} {value}" #Local Vartiable
    return message


print(greet("Toaha"))
print(sentEmail("Sayan"))
print(value)