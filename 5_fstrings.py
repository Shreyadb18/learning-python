#f-strings
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Shreya"
print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this:Hey my name is {{name}} and I am from {{country}}")
price = 49.0999
txt = f"For only {price:2f} dollars!"
print(txt)
print(txt.format())
print(type(f"{2 * 30}"))

#docstrings:strings that are appear right after defination of a function,method,class
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#Recursion: it is a technique where a function call itself to solve the problem
#it commonly used when a problem can be broken into smaller version of the same problem
#factorial(n) = n * factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
#how the prgm will work means n*factorial(n-1)
#factorial(5)
#5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# 120
#fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
# retuen 5 + 4
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# f(n) = f(n-1) + f(n-2)

# recursive countdown
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n-1)

countdown(5)

#using loop
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

#using dynamic programming
def fibonacci(n):
    fib = [0, 1]

    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]

print(fibonacci(10))