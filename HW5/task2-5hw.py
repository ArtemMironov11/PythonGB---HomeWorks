# Дан список случайных чисел. 
# Создайте список, в который попадают числа,
#  описывающие возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] 
# или [5, 6, 7] или [4, 6, 7] и т.д.


import random
print('Введите количество элементов списка, N = ')
N = int(input())
rand_list = [random.randint(1, 10) for i in range(N)]
print(rand_list, " - изначальный рандом список")

def grow_filter():
    for i in range(len(rand_list)):
        result = [0]
        for elem in rand_list[i:]:
            if elem > result[-1]:
                result.append(elem)
        result.remove(0)
        if len(result)>1:
            print(result)

print("Вывожу все возрастающие: ")
grow_filter()