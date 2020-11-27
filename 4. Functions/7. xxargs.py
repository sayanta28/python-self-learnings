#  Suppose we want to pass multiple key-value pair in function
# Then we have to use ** or double astarik
# And it helps us make pakage our arguments in one variable
# And that variable storage is known as Dictionary

def save_user(**users):
    print(users) # So user makes a key value pairs which act as dictionary
    print(type(users)) # class = 'dict'
    # print(users["id"])
    return users


save_user(id=1 , name="mosh", age=22)
db = save_user(val = 3, number = 4)
print(db, type(db)) #db also 'dict' type