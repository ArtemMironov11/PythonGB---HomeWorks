# Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.

N = int(input())

temp = str(N)
temp1 = temp + temp
temp2 = temp1 + temp

sum = N + int(temp1) + int(temp2)

print(sum)
