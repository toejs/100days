print("Welcome from Pizza App")
size = input("What kind of Pizza do you want to buy? ")
bill = 0
if size == "S":
    bill += 15
    print(f"Small Pizza : $ {bill}")
elif size == "M":
    bill += 20
    print(f"Medium Pizza : $ {bill}")
else:
    bill += 25
    print(f"Big Pizzia : $ {bill}")

add_perpperoni = input("Do you want to add Perpperoni? ")
if add_perpperoni == "Y":
    if size == "S" or size == "M":
        bill += 2
        print(f"Charge is $ {bill}")
    else:
        bill += 3
        print(f"Charge is $ {bill}")
else:
    print(f"Charges pay $ {bill}")
cheese = input("Do you want to add cheese ? ")
if cheese == "Y":
    bill += 1
    print(f"Final pay $ {bill}")
else:
    print(f"Final pay $ {bill}")