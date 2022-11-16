#Kurt Jonathan L. Gozano , Sheena Mechaela Basiga 

total_payment = float(input("total purchase "))
money = float(input("customer payment "))

if total_payment >= 2000:
    discount = 0.1 * total_payment
    total = total_payment - discount
    print("your total payment is", total)
else: 
    total = total_payment - 0
    print("you have no discount")

change = money - total 
print("change is", change)