#for else loop
successful = True
for number in range(3):
    print("Attempt")
    successful = False
    if successful:
        print('Successful')
        break
    else:
        successful = True
else:
    print("Tried but failed")