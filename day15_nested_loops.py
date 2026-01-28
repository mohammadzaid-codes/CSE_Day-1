for i in range(3):
    for j in range(2):
        print("i =" , i , "j =" , j)


for i in range(4):
    for j in range(4):
        print("*", end="")
    print()



for i in range(1,6):
    for j in range(i):
        print("*" , end="")
    print()


 # Mini Project
for i in range(1,6):
    print("Table of " , i)
    for j in range(1,11):
        print(i, "x" , j , "=", i*j)
    print()   