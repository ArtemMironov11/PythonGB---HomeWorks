# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

fruits_List = []
clear_Fruits_List = []

with open("Task2-3hw.txt", "r", encoding="utf-8") as file:
    fruits_List = file.read().splitlines()

# в массиве есть пустые элементы, не тяну их в новый массив
for elem in fruits_List:
    if len(elem) > 0:
        clear_Fruits_List.append(elem)

search_1st_symbol = input("Введите букву: ")

for clear_elem in clear_Fruits_List:
    if clear_elem[0].lower() == search_1st_symbol.lower():
        print(clear_elem, end=", ")