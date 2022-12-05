# Задача 1. Постройте график функции f(𝑥)=5𝑥^2+10𝑥−30 
# По графику определите, при каких значения x значение функции отрицательно.


import matplotlib.pyplot as plt

xList, yList = [], []
for i in range(-10, 10):
    xList.append(i)
    yList.append(5*pow(i,2) + 10*i-30)
    
        
plt.axhline(y = 0, color = 'g', linestyle = '-.')
plt.plot(yList)
plt.show()