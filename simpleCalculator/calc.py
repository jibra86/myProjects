
"""
Input of the operands and the operator
"""
Val1 = input("Value one: ")
Val2 = input("Value two: ")
Op = input("Enter the operator: ")

try:
    fVal1 = float(Val1)
    fVal2 = float(Val2)
except:
    print("Enter a Numerical Value!!!")
    exit

if Op == "+":
    print(fVal1 + fVal2)
elif Op == "-":
    print(fVal1 - fVal2)
elif Op == "/":
    print(fVal1 / fVal2)
elif Op == "*":
    print(fVal1 * fVal2)
