# spend $100 and more and get 10% discount
# spend $200 and more and get 20% discount
# if we buy for 80$ we pay 80$
# if we buy for $150 - we pay $135
# we pay 10% 

discount = 0
sales_tax = 0.1

def tax_func(price):
    taxes = price*sales_tax
    return (taxes)

def discount_function(price, discount):
    discount = price * (discount / 100)
    return (discount)

price=float(input("Enter price: "))
tax=tax_func(price)

if price > 100 and price <= 200:    # if price 101-200$ discount 10%
    discount = discount_function(price, 10)
elif price > 200:                   # if price more then 200 discount 20%
    discount = discount_function(price, 20)

total_price = price + tax - discount
print(total_price)
