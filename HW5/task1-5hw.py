# Задача 1. Задайте список случайных 
# чисел от 1 до 10, выведите все 
# элементы больше 5. Используйте для 
# решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


import random

random_List = [random.randint(1, 10) for i in range(9)]
print(random_List, " - весь список")

filteredList = list(filter(lambda x: x > 5, random_List))
print(filteredList, " - список из элементов >5")