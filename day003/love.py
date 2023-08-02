print("Welcome to the love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combining_name = name1 + name2
lcase_name = combining_name.lower()
t = lcase_name.count("t")
r = lcase_name.count("r")
u = lcase_name.count("u")
e = lcase_name.count("e")
true = t + r + u + e

l = lcase_name.count("l")
o = lcase_name.count("o")
v = lcase_name.count("v")
e = lcase_name.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
print(love_score)
love_score_int = int(love_score)
if (love_score_int < 10) or (love_score_int > 90):
    print(f"Your score is {love_score_int}, you go together like coke and mentos")
elif (love_score_int >= 40) and (love_score_int <= 50):
    print(f"your score is {love_score_int}, you are alright together.")
else:
    print(f"your score is {love_score_int}")