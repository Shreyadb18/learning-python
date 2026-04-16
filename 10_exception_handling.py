#Exception handling:process of responding to unwanted or unexpected events when computer program runs
#try:
    # risky code
#except:
    # handle error
#finally:
    # always executes

try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This block always runs")

a = input("Enter the number: ")
print("Multiplication table of {a} is: ")
for i in range(1,11):
    print(f"{int(a)} * {i} = {int(a)*i}")

print("Some lines of code")
print("end of program")
# try and except are used to handle to handle the error
a = input("Enter the number: ")
print("Multiplication table of {a} is: ")
try: 
 for i in range(1,11):
    print(f"{int(a)} * {i} = {int(a)*i}")
except:
    print("Invalid Input")

print("Some lines of code")
print("end of program")

try:
    num = int(input("Enter an intrger: "))
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")

#final clause:part of the expection handling
try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")
    
finally:
    print("I am always executed")


try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")
    
finally:
    print("I am always executed")

#def func1():
 #    try:
  #    l = [1,5,6,7]
  #   i = int(input("Enter the index: "))
   #  print(l[i])
    # return 1
#except:
 #     print("Some error occurred")
  #  return 0
    
#finally:
 #   print("I am always executed")

#x = func1()
#print(x)

#raise custom error
age = int(input("Enter age: "))

if age < 18:
    raise Exception("You must be at least 18 years old")
#using own custom error
class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise InvalidAgeError("Age is below 18")

#using try and except
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Not eligible")
    print("You can proceed")
except InvalidAgeError as e:
    print("Error:", e)

#using real world logic
class BalanceError(Exception):
    pass

balance = 1000
withdraw = int(input("Enter amount: "))

if withdraw > balance:
    raise BalanceError("Insufficient balance")