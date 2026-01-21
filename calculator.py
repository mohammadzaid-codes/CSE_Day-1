def add(c,d):
    return c+d

def substract(c,d):
    return c-d
def multiply(c,d):
    return c*d

def divide(c,d):
    if d == 0:
        return "Cannot divided by zero"
    else:
        return c/d

num1 = float(input("Enter first number"))
num2 =  float(input("Enter second number"))

op = input("Enter operation (+,-,*,/):")
if op == "+":
        print("Result", add(num1,num2))
elif op == "-":
        print("Result", substract(num1,num2))
elif op == "*":
        print("Result", multiply(num1,num2))
elif op == "/":
        print("Result", divide(num1,num2))
else:
        print("Invalid operation")
              

