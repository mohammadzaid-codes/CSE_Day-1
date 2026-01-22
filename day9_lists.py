numbers = [10,20,30,40,50]
print(numbers)

# Access elements
print(numbers[0])
print(numbers[-1])


# Modify lists
numbers.append(60)
numbers.remove(20)
print(numbers)

#loop through lists
for num in numbers:
    print(num)

#sum of list elements
total = 0
for num in numbers:
    total += num
    print("Total", total)

# Mini project: Student Marks
marks = [78,85,90,66,88]

total = sum(marks)
average = total / len(marks)

print("Total Marks", total)
print("Average Marks", average)

# Mini project 2 : Find the largest number 
numbers = [12,45,2,89,34]
print("Maximum", max(numbers))


days = ("Mon", "Tue", "Wed")
print(days)