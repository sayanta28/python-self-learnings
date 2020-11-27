# Suppose we can to catch n arguments in one sotrage variable.
# In that time this approach is used for.
# So for catch multi argument we have to use estarik
# It is called tuple ; which much similiar as list
# Tuple = ( 2, 3, 4, 5) and List = [2, 3, 4, 5]
# Tuple and List both are iterable 
# But Tuple can't add new member object. this is it's limitation

def multiply(*numbers): # So for catch multi argument we have to use estarik
    print(type(numbers)) # Show tuple class
    total = 1
    for value in numbers:
        total *= value
    return total


print(multiply(2,3,4,5))