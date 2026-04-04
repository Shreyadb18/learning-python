print("hello world!!")#this is my code

print("I am a good girl\nand I am studing")#next line

"""
python is a simple language
i am shreya
don't remove my code
"""
print("I am a \"good girl\"\nand I am studing")

print("hey",6,7,sep="~",end="009\n")
print("shreya")

a=12
print(a)
harry=9
b=harry
print(b)
b="harry"
print(b)

a=1
b=2.1
c=True
d="shreya"
e=None
print(a+b)
print("The type of a is ",type(a))
print("The type of a is ",type(b))
print("The type of a is ",type(c))
print("The type of a is ",type(d))
print("The type of a is ",type(e))

list=["apple",6,3.2,"elephant"]
print(list)#collection of ordered data,it is mutable
 
tuple=("apple",6,3.2,"elephant")
print(tuple)#same as list but it is immutable

dict={"name":"shreya","age":20}
print(dict)#key:value pair

#typecasting:conversion of one data type into other
a="1"
b="2" 
print(a+b)
print(int(a)+int(b))

#implicit typecasting:one datatype is converted to other by python interpreter itself
c=1.2
d=2
print(c+d)

#taking user input
a=input("Enter the name: ")
print("My name is",a)

x=input("Enter first number: ")
y=input("Enter the second number: ")
print(x+y)
print(int(x)+int(y))

#strings
name = "shreya"
friend = "chethan"
anotherfriend = "pramod"
apple = '''he said,
hii shreya
hey I am good
"I want to eat an apple'''

print("hello, "+name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("I like coding\n")

for characters in apple:
    print(characters)
for characters in name:
    print(characters)

#slicing
fruit = "mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[:5])
print(fruit[0:-3])
print(fruit[-1:len(fruit)-3])
print(fruit[:len(fruit)-3])
print(fruit[-3:-1])

a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a^b)
print(a**b)

a=50
b=2
print("The value of",a,"+",3,"is: ",a+b)
print("The value of",a,"+",3,"is: ",a-b)
print("The value of",a,"+",3,"is: ",a*b)
print("The value of",a,"+",3,"is: ",a/b)



