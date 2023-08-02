print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("you can ride")
    age = int(input("What is you age? "))
    bill = 0
    if age < 12:
        bill += 5
        print(f"Charges to pay {bill}$")
    elif age <= 18:
        bill += 7
        print(f"Charges to pay {bill}$")
    elif age <= 22:
        bill += 10
        print(f"Charges to pay {bill}$")
    elif age >= 40 and age <= 60:
        bill += 14
        print(f"Charges to pay {bill}$")
    else:
        bill += 12
        print(f"Charges to pay {bill}$")
    wants_photo = input("Do you want to take photo ? Y or N ")
    if wants_photo == "Y":
        bill += 3
        print(f"Please pay {bill}$")
    else:
        print(f"please pay {bill}$")
else:
    print("You can not ride")