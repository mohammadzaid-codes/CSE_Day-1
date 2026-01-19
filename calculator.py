def add(a,b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Cannot divided by zero"
    else:
        return a/b
    
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
              

