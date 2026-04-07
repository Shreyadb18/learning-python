str1 = "Welcome to the console"
print(str1.endswith("!!!"))
str1 = "Welcome to the console !!!"
print(str1.endswith("to",8,10))
print(str1[8:10])
a="i am"
print(a+" chethan")

#strings are immutable
a = "Harry!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!!!!"))# remove the trailing character
print(a.replace("Harry","John"))
print(a.split(" "))# string at the specified instance returns the separated strings as list items
blogHeading = "introduction to js"
print(blogHeading.capitalize())# capitalize:first letter capital others are small

str1 = "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))# indicates how many times the letter repeated

str1 = "Welcome to the console"
print(str1.endswith("!!!"))
str1 = "Welcome to the console !!!"
print(str1.endswith("to",4,10))

str1 = "He's name is Dan.He is an honest man."
print(str1)
print(str1.find("is"))#bsearches for the occourance of the given value and returns the index when it is present,if the value is absent the string returns -1
print(str1.find("ishh"))
print(str1.index("is"))#same as find but if the value is absent from the string then raise an exception
str1 = "WelcomeToTheConsole"
print(str1.isalnum())#a-z,A-Z,0-9
str1 = "Welcome"
print(str1.isalpha())#A-Z,a-z

str1 = "Hello World"
print(str1.islower())

str1 = "we wish you a Merry christmas\n"
print(str1)
print(str1.isprintable())#print as it is but \n newline character is printable
str1 = "     "  #using spacebar
print(str1.isspace())

str1 = "World Health organization"
print(str1.istitle)# title: 1st letter capital

str1 = "Python is a Interpreted language"
print(str1.startswith("Python"))

str1 = "He's name is Dan.He is an honest man."
print(str1.swapcase())
str1 = "He's name is Dan.He is an honest man."
print(str1.title())




