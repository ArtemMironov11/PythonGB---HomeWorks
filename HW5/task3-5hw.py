# Задайте список случайных чисел 
# от 1 до 10. Посчитайте, сколько 
# всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента 
# совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random
print('Введите количество элементов списка, N = ')
N = int(input())
rand_list = [random.randint(1, 10) for i in range(N)]
print(rand_list, " - изначальный рандом список")

unique_list = set(rand_list)
print(list(unique_list), " - уникальный рандом список")

repeat_items = dict ((x, rand_list.count(x)) for x in unique_list if rand_list.count(x) > 1)
print(repeat_items, " - словарь повторов больше 1 раза")

print(len(repeat_items), "элементов совпадают")
