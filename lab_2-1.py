# author: LM (AMDG) 1/1/21
def adding(number_input):
    total = 0
    for value in range(int(number_input + 1)):
        total += value
    return total


number = (input("Enter the numbers: "))
print(adding(number))
