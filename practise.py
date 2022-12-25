student_info = [(10, 55.0), (23, 66.7), (14, 87.0)]

student_info.append((9, 57.0))
print(student_info)

in_class = False
for i in range(len(student_info) - 1):
    class_number, grade = student_info[i]
    if class_number == 10:
        in_class = True    
print(in_class)

in_class = False
for tuple in student_info:
    class_number, grade = tuple
    if class_number == 38:
        in_class = True
print(in_class)

i = 0 
while i < len(student_info):
    class_number, grade = student_info[i]
    if class_number == 38:
        in_class = True
    i+=1
print(in_class)


print(range(len(student_info)))

i = 0
count = 0
while i < len(student_info):
    class_number, grade = student_info[i]
    if grade >= 50.0:
        count+=1
    i+=1
print(count)

for tuple in student_info:
    class_number, grade = tuple
    
        
#Draft
red = 'R'
black = 'B'

draft = [[black] * 8 for i in range(8)]
 
for i in range(8):
    for j in range(8):
        if (i + j) % 2 != 0:
            draft[i][j] = red
for i in range(8):
    for j in range(8):
        print(draft[i][j], end= " ")
    print()
    
print('\n')

i = 0 
while i < 8:
    for j in range(8):
        if (i + j) % 2 != 0:
            draft[i][j] = red
    i+=1
    
for i in range(8):
    for j in range(8):
        print(draft[i][j], end= " ")
    print()
    
    

ecor1051 = [("A", "Bailey"), ("B", "Schrramm"), ("C", "Bailey"), ("H", "Schramm"), ("I", "Bailey")]

ecor1051[-1] = "I", "Martial"
print(ecor1051)
for tuple in ecor1051:
    section, instructor = tuple
    print(section, end=" \n")
    
i = 0 
while i < len(ecor1051):
    section, instructor = ecor1051[i]
    print(section, instructor)
    i+=1
print()