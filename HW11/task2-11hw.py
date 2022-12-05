# Задача 2. Имеются данные о площади и стоимости 15 домов. 
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей. 
# Предоставьте ему графические данные о стоимости квадратного метра 
# каждого дома и список подходящих ему домов, отсортированных по площади. 
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.


import matplotlib.pyplot as plt
import random as rnd
import math
houses = 15
priceChecking = 50000

housesName, housesSquare, housesPrice, avg_Price = [],[],[],[]

for i in range(houses):
  housesName.append(f'Дом {i+1}')
  housesSquare.append(rnd.randint(100,301))
  housesPrice.append(rnd.randint(3000000,21000000)) 
  house_Avg_Price = round((housesPrice[i]/housesSquare[i]),2)
  avg_Price.append(house_Avg_Price)

allData = list(zip(housesName, housesSquare, housesPrice, avg_Price))
print(allData)

house_avg_Price_dict = dict(zip(housesName,avg_Price))

sortedTuple = sorted(house_avg_Price_dict.items(), key=lambda x:x[1])

sortedDict = dict((x, y) for x, y in sortedTuple)
print(sortedDict)

names = list(sortedDict.keys())
values = list(sortedDict.values())
plt.figure(figsize=(12,12))
plt.axhline(y = priceChecking, color = 'g', linestyle = '-.')
plt.plot(names,values)
plt.show()