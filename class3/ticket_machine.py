def ticket_machine():
    while True:
        your_age=int(input("Enter your age: "))
        if your_age<13 and your_age>0:
            print("Sorry your not allow to pass")
        elif your_age>=13 and your_age<18:
            print("Please call your legal guardian")
        elif your_age>=18:
            print("Welcome")
        else: print("Something went wrong")


ticket_machine()
