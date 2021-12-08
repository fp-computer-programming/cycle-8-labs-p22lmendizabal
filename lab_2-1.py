# author: LM (AMDG) 1/1/21
number = int(input("Enter the number: "))

def adding(number_input):
    total = 0
    for value in range((number_input) + 1):
        total += value
    return total

print(adding(number))
