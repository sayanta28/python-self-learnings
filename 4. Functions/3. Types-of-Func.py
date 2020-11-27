#Function that Perform a task
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Abraod")


greet("Sayanta","Chowdhury")
print(greet("Mosh", "Chy")) # Return 'None' because the Function return nothing
#Function that Return a value
def get_greet(first_name, last_name):
    return f"Hi {first_name} {last_name}"


print(get_greet("Sayanta", "Chy"))
message = get_greet("Mosh", "Chy")
