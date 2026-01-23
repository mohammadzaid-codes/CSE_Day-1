student = {
    "name": "Zaid",
    "age": 18,
    "course": "CSE"
}


print(student)
# Accessing values

print(student["name"])
print(student["age"])

student ["college"] = "Rama University"
print(student)

student["age"] = 19
print(student)

del student["course"]
print(student)

for key, value in student.items():
    print(key, ":",value)





# Mini project: Student marks 

student_marks ={}

name = input("Enter student name")
marks = int(input("Enter marks"))

student_marks[name] = marks

print("Result")
for name, marks in student_marks.items():
     if marks >= 40:
        print(name,"PASS")
     else:
        print(name,"FAIL")

