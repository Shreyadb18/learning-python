#sets:an unorderd collection of data items
s = {2,4,2,6}
print(s)

info = {"Carlo",19,False,5.9,19}#order is not mentioned
print(info)

shreya = {}
print(type(shreya))

shreya = set()
print(type(shreya))

for value in info:
    print(value)

#set methods
s1 = {1,2,4,6}
s2 = {3,5,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

s = {1,2,3,4}
s1 = {5,6,3,4}
s2 = s.difference(s1)
print(s2)

s = {1,2,3,4}
s1 = {1,5,6,7}
print(s.isdisjoint(s1))
print(s.issuperset(s1))
s2 = {1,3,5,7}
print(s.issuperset(s2))
print(s2.issubset(s))

s = {1,2,3,4}
s.add(5)
print(s)
s.remove(2)
print(s)
s = {1,2,3,4,5}
item = s.pop()
print(s)
print(item)
#s = {1,2,3,4,5}
#del s
#print(s)

info = {"Carlo",19,False,5.9,19}
if "Carlo" in info:
    print("Carlo is present")
else:
     print("Carlo is absent")


