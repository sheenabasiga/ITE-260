# Initialzing constants
CHILD_DISCOUNT = 0.2
CHARITY_DONATION = 0.12

# use inputs
day_week = str(input())
no_adults = int(input())
no_children = int(input())
no_hours = int(input())
payment = float(input())

if day_week == "Sunday":
    adult_rate = 200.00
elif day_week == "Wednesday" or day_week == "Saturday":
    adult_rate = 150.00
else:
    adult_rate = 120.00
  
child_rate = adult_rate - (adult_rate * CHILD_DISCOUNT)

ticket_adult = adult_rate * no_adults * no_hours
ticket_child = child_rate * no_children * no_hours

total_bill = ticket_adult + ticket_child
charity_bill = total_bill * CHARITY_DONATION

if payment < total_bill:
  print("Not enough money!")
else:
  change =  payment - total_bill
  print("Total Adult Fee:", ticket_adult,
        "\nTotal Child Fee:", ticket_child,
       "\nTotal Entrance Fee:", total_bill,
       "\nCharity Donation:", charity_bill,
       "\nChange:", change)