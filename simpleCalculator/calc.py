
"""
Input of the operands and the operator
"""
Val1 = input("Value one: ")
Val2 = input("Value two: ")
Op = input("Enter the operator: ")

"""
try-except block to solve the problem that might occur if someone
un-intentional entered string value instead of numerical value...
"""
try:
    fVal1 = float(Val1)
    fVal2 = float(Val2)
except:
    print("Enter a Numerical Value!!!")
    exit

"""
if-elif statements for the calculations....
"""
if Op == "+": # if the Op variable is equal to +
    print(fVal1 + fVal2) # then perform summision
elif Op == "-": # if the Op variable is equal to -
    print(fVal1 - fVal2) # then perform subtraction
elif Op == "/": # if the Op variable is equal to /
    print(fVal1 / fVal2) # then perform division
elif Op == "*": # if the Op variable is equal to *
    print(fVal1 * fVal2) # then perform multiplication
