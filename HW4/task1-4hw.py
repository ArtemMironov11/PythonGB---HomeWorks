# Задача 1. Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def factorial(x):
    result = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            result.append(d)
            x = x // d
        else:
            d += 1
    if x > 1:
        result.append(x)
    return result
print(factorial(409))
