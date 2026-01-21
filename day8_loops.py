# Multiplication Table
num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Sum of numbers
total_sum = 0
for i in range(1, 11):
    total_sum = total_sum + i

print("The sum is", total_sum)

# While loop
i = 1
while i <= 10:
    print(i)
    i = i + 1
 