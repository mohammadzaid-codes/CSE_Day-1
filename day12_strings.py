text = "Hello World"
name = "Zaid"

print(text)
print(name)
print(type(text))


# indexing
print(text[0])
print(text[-1])


word = "Programming"

print(word[0:6])
print(word[3:])
print(word[:4])

# useful string methods
msg = " hello python world"

print(msg.upper())
print(msg.lower())
print(msg.strip())
print(msg.replace("python " ,"coding"))
print(msg.split())

# string condition logic 
email = input("Enter email")

if "@" in email and "." in email :
    print("Valid email")
else:
    print("Invalid email")

# looping through string
name = "zaid"

for ch in name:
    print(ch)

#Mini project 1 - Word Counter
sentence = input("Enter a sentence")

words = sentence.split()
print("Total words",len (words))

# Mini project 2 - password checker
password = input("Enter password")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")

#Mini project 3 - Name Formatter
name = input("Enter full name")

print("Upper", name.upper())
print("Lower", name.lower())
print("Title", name.title())


