# for loop
name = 'shreya'
for i in name:
    print(i)
    if(i == "b"):
        print("This is something special")

colors = ["red,white,blue,pink"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(5):
    print(k)
    print(k+1)

for k in range(1,5):
    print(k)
for k in range(1,12,2):
    print(k)


#while loop
i = 0
while(i<=3):
    print(i)
i=i+1
print("Done with the loop")

count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")

#do while loop
#while True:
    # statements
    
    #if condition:
       # break
i = 1

while True:
    print(i)
    i = i + 1
    
    if i > 5:
        break
    
 #break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

for i in range(12):
    if(i == 10):
        break
    print("5 X",i+1,"=",5 * (i+1))


#continue
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X",i,"=",5 * i)


