names = ["Zaid","Bread","Kallu","Deba"]

print(names)
print(names[0])
print(len(names))

students = []

for i in range(3):
     name = input("Enter a student name")

     students.append(name)

     print(students)


for student in students:
     print("Students name is ", students)



#Mini project - Student Marks System
marks = []

for i in range(5):
   m = int(input("Enter Marks"))
   marks.append(m)

print("All marks" , marks)

total =  sum(marks)
average = total / len(marks)

print("Total " , total)
print("Average ", average)

if average >= 40:
    print("PASS")
else:
    print("FAIL")



#String practice
sentence =  input("Enter a senence")

words = sentence.split()
print("Words", words)
print("Number of Words", len(words))



