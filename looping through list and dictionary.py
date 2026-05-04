#looping through list
l = [1,23,24,34,56]
total = 0
for num in l:
    print(total)
    total = total+num
    print(total)
    
l = [1,23,24,34,56]
dl = []
for num in l:
    dl.append(num*2)
    print(dl)

#looping through dictionary
student_marks = {"Anand":85,"Geetha":90,"kumar":78}
for student, marks in student_marks.items():
    print(f"{student}---{marks}")

student_marks = {"Anand":85,"Geetha":90,"kumar":78}
for student in student_marks.items():
    print(student)

student_marks = {"Anand":85,"Geetha":90,"kumar":78}
for  marks in student_marks.items():
    print(marks)

#for loop with range
student = ["Shreya","Modi","Gandhi"]
marks = [32,90,60]

for index,student in enumerate(student):
    student_marks[student] = marks[index]
    print(student_marks)

student = ["Shreya","Modi","Gandhi"]
marks = [32,90,60]

student_marks = {}

for i in range(3):
    student_marks[student[i]] = marks[0]
    print(student_marks)

student = ["Shreya","Modi","Gandhi"]
marks = [32,90,60]

student_marks = {}

for i in range(len(student)):
    student_marks[student[i]] = marks[i]
    print(student_marks)
    
student = ["Shreya","Modi","Gandhi"]
marks = [32,90,60]

student_marks = {}

for i in range(1,len(student),2):
    student_marks[student[i]] = marks[i]
    print(student_marks)
    
