# Task 1
summ=0
for i in range(101):
    summ+=i
print("Resault summ =", summ)


#Task 2
for i in range(100,0,-1):
    print(i)


#Task 3
def mult_table(number):
    for i in range(11):
        print(f"{number}*{i} = {i*number}")

input_number=int(input("Enter number: "))
mult_table(input_number)
