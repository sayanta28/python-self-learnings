high_income = True
good_credit = True

#Ques: If a human has high income and good credit then ok otherwise not okay.
if high_income and good_credit:
    print("Eligible")

else: 
    print("Not")

student = True

#Ques: If a human is a student then ok otherwise not okay.

if not student:
    print("Eligible")
else:
    print("Not Eligible")

#Ques: If a human has high income or good credit and is a student then ok otherwise not okay.

high_income = True
good_credit = False
student = True

if(high_income or good_credit) and student:
    print("eligible")
else:
    print("Not Eligible")
