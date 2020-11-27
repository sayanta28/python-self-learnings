def multiply(*numbers): # So for catch multi argument we have to use estarik
    print(type(numbers)) # Show tuple class
    total = 1
    for value in numbers:
        total *= value
    return total

print("start")
print(multiply(1,2,3))

# Learn how to use debug mode for finding bug.
# and Shortcut keys
# Home Button for go in First oint of line
# End Button for go in Last point of line
# CTRL + Home Button for go in First Line of the file
# CTRL + End Button for go in Last Line of the file
# ALT + UP or Down Key
# SHIFT + ALT + UP/DOWN Key
# Make Comment = Select line and CTRL + '\' 
# For AUTO Completion press enter or sub char