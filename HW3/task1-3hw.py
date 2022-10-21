# Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8 

fib_list = [1,1]
fib1 = fib2 = 1

N = int(input("Введите N: "))

for i in range(2, N):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list.append(fib2)

file = open('Task1-3hw.txt', 'w', encoding='utf-8')
file.write(' '.join(str(x) for x in fib_list))
file.close()