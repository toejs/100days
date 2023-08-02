weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))
bmi_ratio = round(weight / height ** 2, 2)
print(f"BMI Ratio : {bmi_ratio}")
if bmi_ratio < 18.5:
    print("you are underweight")
elif bmi_ratio < 25:
    print("you are normal weight")
elif bmi_ratio < 30:
    print("you are over weight")
elif bmi_ratio < 35:
    print("you are obese")
else:
    print("you are clinically obese")