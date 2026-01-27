marks = [45,67,23,89,90]

for mark in marks:
    if mark >= 40:
       print(mark,"PASS")
    else:
        print(mark,"FAIL")


students = []

for i in range(3):
    name = input("Enter a Student name")
    students.append(name)

    print("Students lists")
    for student in students:
        print(student)


 # Mini Project 
marks = []

for i in range(5):
    m = int(input("Enter mark"))
    marks.append(m)

total = sum(marks)
average = total / len(marks)

print("Total",total)
print("Average", average)

if average >= 40:
    print("Result : PASS")
else:
    print("Result : FAIL")
    
       
