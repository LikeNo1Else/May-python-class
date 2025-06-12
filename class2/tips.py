# Task 2

tips_size=int(input("Your tips size: "))

if tips_size>0 and tips_size<=15:
    print("Standart")
elif tips_size>15 and tips_size<=18:
    print("Good")
elif tips_size>18 and tips_size<=20:
    print("Great")
elif tips_size>20:
    print("My hero")
else:
    print("You are cheap")

