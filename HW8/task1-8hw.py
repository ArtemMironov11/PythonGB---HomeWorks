# Задача 1. В каждой группе учится 
# от 20 до 30 студентов. По итогам экзамена все оценки з
# аносятся в таблицу. Каждой группе отведена своя строка. 
# Определите группу с наилучшим средним баллом.



from random import randint 
groups = randint(5, 10)

grades = [0]*groups

for i in range(len(grades)):
    grades[i] = list(randint(2, 5) for j in range(20, 30))


grades_2 = []

for grades_in_group in grades:
    mean = 0
    for grade in grades_in_group:
        mean += grade
    grades_2.append(round(mean/len(grades_in_group), 2))


for grades_in_group in grades:
    print(grades_in_group)
    
print(grades_2)

max_grade = max(grades_2)
num_group = grades_2.index(max_grade)
print(f'лучший средний балл {max_grade}. У группы {num_group+1}')
