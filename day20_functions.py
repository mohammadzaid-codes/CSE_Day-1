def say_hello():
    print("Hello , welcome to python")

say_hello()
say_hello()


def check_pass(marks):
    if marks >= 40:
        print("PASS")
    else:
        print("FAIL")

check_pass(35)
check_pass(78)


def login_user(username):
    registered_users = {"ali","zaid","sara"}

    if username in registered_users:
        print("Login Succesfully")
    else:
        print("User Not Found")

users = input("Enter Username").lower()
login_user(users)

def check_even_odd(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
              
check_even_odd(10)
check_even_odd(7)

