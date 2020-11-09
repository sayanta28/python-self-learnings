age = 12
"""
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

"""

#Clean Code
"""
age = 12
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

print(message)
"""

#Most Clean Code
#Ternary Operator
message = "Eligible" if age>=12 else "Not Eligible"
print(message)
