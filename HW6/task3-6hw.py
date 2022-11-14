# Найдите все простые 
# несократимые дроби, лежащие между 
# 0 и 1, знаменатель которых 
# не превышает 11.


import math


result =[]
for i in range (2, 12):
    for j in range(1, i):
        if math.gcd(i,j) == 1:
            result.append(f'{j}/{i}')
print(result)