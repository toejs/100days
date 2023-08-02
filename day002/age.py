age = int(input("What is your current age?"))

remain_year = 94 - age
remaining_days = remain_year * 365
remaining_weeks = int(remaining_days / 7)
print("your remaining age in day : " + str(remaining_days))
print("your remaining age in week : " + str(remaining_weeks))
print("your remaining age in year : " + str(remain_year))
print("week per year : ", 365 / 7)

