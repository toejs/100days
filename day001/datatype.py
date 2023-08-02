#Data Types

#string
print("hello"[0])
print("23434" + "2345")

#integer
print(23434+2345)

#float
pi = 22/7
print(pi)

#boolean
isTrue = True
print(isTrue)

num_char = len(input("what is your name")) #int
print(type(num_char))
print("Your name has " + str(num_char) + " length.") #convert to string

#multiply two digits
num = input("enter digit : ")
first_digit = num[0]
print(type(first_digit))
second_digit = num[1]
print(type(second_digit))
result = int(first_digit) * int(second_digit)
print("The result is : " + str(result))

