# author: LM (AMDG) 1/2/21
def sum_to(n):
    total = 0
    num = 0
    while num <= int(n):
        print(num)
        total += num
        num += 1

n = input("enter a number: ")
sum_to(n)
