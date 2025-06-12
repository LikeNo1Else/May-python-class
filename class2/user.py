# Task 1

your_age = int(input("Enter your age: "))

if your_age>0 and your_age<13:
    print("You are a child")
elif your_age>=13 and your_age<18:
    print("You are a teenager")
elif your_age>18 and your_age<65:
    print("You are an adult")
elif your_age>=65:
    print("You are an elder")
else:
    print("Incorrect age")


