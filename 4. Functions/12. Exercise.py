def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 != 0): return "fizz"
    elif(input % 5 ==0 and input % 3 != 0): return "buzz"
    elif(input % 3 == 0 and input % 5 == 0): return "fizz-buzz"
    else: return input


print(fizz_buzz(17))

# Fizz-Buzz Problem