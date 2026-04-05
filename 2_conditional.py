a = int(input("Enter your age: "))
print("Your age is:",a) 

if a >= 18:
    print("You an drive")
else:
    print("You cannot drive")

applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("alexa, add 1 kg apples to the cart.")
else:
    print("alexa, do not add apples to the cart.")

num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

num = 18
if(num < 0):
    print("Number is negative.")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

