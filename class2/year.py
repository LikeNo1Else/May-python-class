year = int(input("Enter number of years: "))
unit = input("""Make a choice: 
1-Day, 
2-Week, 
3-Hours 
What is your choice? """)

if unit == "1":
    print(f"in {year} years there are {year*365} days")
elif unit == "2":
    print(f"in {year} years there are {year*52} weeks")
elif unit == "3":
    print(f"in {year} years there are {year*24*365} hours") 
else:
    print("Wrong choice")




