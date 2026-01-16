marks = int(input("Enter  your marks:"))
if marks >= 90:
    print("Grade A ")
elif marks >= 75:
    print("Grade B ")
elif marks >=60:
    print("Grade C ")
else:
    print("FAIL")




    username = input("enter Username:")
    password = input("enter password:")
    if username == "admin" and password == "1234":
        print("Login Sucesfully")
    else:
        print("Invalid Ceredentials")
        