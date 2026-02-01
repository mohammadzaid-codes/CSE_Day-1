names = ["Zaid", "Ali", "Zaid","Ali","Sara"]
print(set(names))


marks = [35,67,12,89,40,55]

for mark in marks:
 if mark >= 40:
    print(mark,"PASS")
 else:
    print(mark,"FAIL")


emails = ["a@gmail.com","b@gmail.com","a@gmail.com","c@gmail.com"]

print(emails)
unique_emails = set(emails)
print(len(unique_emails))


students = [("Ali",78),("Zaid",35),("Sara",90),("Aman",42)]

for student in students:
   name = student[0]
   marks = student[1]

if marks >= 40:
 print(name,"ELIGIBLE")
else:
 print(name,"NOT ELIGIBLE")


registered_users = {"ali","zaid","sara"}
username = input("Enter a Username").lower()

if username in registered_users:
 print("Login Succesfully")
else:
 print("User Not Found")
 print("Total_registered users", len(registered_users))
