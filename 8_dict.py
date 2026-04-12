#dictionary:orderd collection of data item
dic = {
    "shreya":"Human being",
    "spoon" :"object"
}
print(dic["shreya"])

dic = {
    123:"chethu",
    345:"pramu",
    567:"shreya"
}
print(dic[123])

info = {'name':'shreya','age':20,'eligible':True}
print(info)
print(info.keys())
print(info.values())
for key in info.keys():
    print(info[key])
print(f"The value corresponding to the key {key} is {info[key]}")
print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {info[key]}")
print(info.items())

#dictionary methods
ep1 = {122:45,123:89,124:69,125:69}
ep2 = {222:67,566:90}
ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)
ep1.pop(122)
print(ep1)
ep1.popitem()
print(ep1)
del ep1[122]
print(ep1)