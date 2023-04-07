'''
Easy:
Question:
Write a program which will find all such numbers which are divisible by 7 
but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method


'''
def div7(a,b):
    list_1 = []
    for i in range(a,b+1):
        if i % 7 == 0 and i % 5 != 0:
            list_1.append(str(i))
    return list_1

number1 = int(input("Enter th number1:"))
number2 = int(input("Enter th number1:"))
result = div7(number1,number2)
print("The Numbers obtained are:",",".join(result))
