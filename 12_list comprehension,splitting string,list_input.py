l = [1,2,3,4]
dl = [item**2 for item in l]
print(dl)

l = [x for x in range(1,11)]
print(l)
edl = [x**2 for x in l]
print(edl)

#dictionary comprehension
names = ["shreya","chethan","shrishant","pramu"]
d = {name:len(name) for name in names}
print(d)

cp = {
    "Bengaluru":84,
    "Mysuru":70,
    "Davanagere":20
}
lc = {key:value for key,value in cp.items() if value>60}
print(cp)

#splitting strings
s = "this is a computer"
l = s.split()
print(l)

s = "this-is-a-computer"
l = s.split("-")
print(l)

#list input
print("list input practice")
x = input("Enter list of integers: ")
print(x.split())

print("list input practice")
x = input("Enter list of integers: ").split()
l = [int(num) for num in x]
print(l)