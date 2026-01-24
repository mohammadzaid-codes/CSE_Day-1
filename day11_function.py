def greet():
    print("Hello , welcome")

    greet()

def greet_user(name):
     print("Hello", name)

     greet_user("Zaid")


def add(a, b):
         return a + b
     
result = add(5,3)
print(result)

def calculator(a,b):
       return a+b,a-b,a*b
    
sum_, sub_, mul_ = calculator(10,5)
print(sum_,sub_,mul_)


def even_odd(num):
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
      
print(even_odd(7))




def check_result(marks):
        if marks >= 40:
            return "PASS"
        else:
            return "FAIL"
        
print(check_result(35))
    



    # Mini project: fumction nased calculator

def calculator(a,b,operation):
        if operation == "add":
            return a+b
        elif operation == "sub":
            return a-b
        elif operation == "mul":
            return a*b
        elif operation == "div":
            return a/b
        else:
            return  "Invalid Operation"
        
print(calculator(10,5,"sub"))
     