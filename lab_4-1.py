# author: LM (AMDG) 12/3/21
total = 0
while True:
    inputnumber = input("Enter a number: ")
    if inputnumber == "-1":
        break
    else:
        total += int(inputnumber) 

print("The sum of all numbers enter is {0}.".format(total))