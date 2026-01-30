numbers = [10,20,30,40]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(len(numbers))

#Modifying Lists
numbers.append(50)
print(numbers)

numbers.remove(20)
print(numbers)

numbers[0] = 99
print(numbers) 

#Loop and list
marks = [45,67,23,89,90]

for mark in marks:
    if mark >= 40:
        print("PASS")
    else:
        print("FAIL")


#Mini Project
students = [] 

for i in range(10):
     name = input("Enter Student Name")
    
     students.append(name)

     print("Student lists")
     for student in students:
        print(student)