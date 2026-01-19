def greet():
    print("Hello")

def greet_name(name):
        print("Hello", name)

def add(a,b):
            return a + b

greet()
greet_name("Zaid")
        
result1 = add(10, 20)
print("sum is", result1)
result2 = add(5, 7)
print("sum is ", result2)




def substract(a, b):
        return a-b


def multiply(a, b):
           return a*b

def square(n):
        return n*n

a= int(input("enter first number"))
b= int(input("enter second umber"))
n= int(input("enter a number to square"))

print("substraction is",substract(a,b))
print("multiplication is",multiply(a,b))
print("square of number is", square(n))

