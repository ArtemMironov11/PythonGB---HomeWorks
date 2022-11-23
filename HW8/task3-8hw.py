# Задача 3. В двумерном массиве хранятся средние 
# дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 
# 7-дневный промежуток этого периода. Выведите его даты.



from random import uniform

D_List = [31, 30, 31, 30, 31]
Nm_D_List = ["Март", "Апрель", "Май", "Июнь", "Июль"]


term_List = [None]*(len(D_List))
for i in range(len(term_List)):
    term_List[i] = list(round(uniform(5.00, 30.00), 2)
                        for _ in range(D_List[i]))

print("Средние дневные температуры:")
for row in term_List:
    print(f'{Nm_D_List[term_List.index(row)]} : {row} \n')

flatterm_List = sum(term_List, [])
print(
    f' Одномерный массив температур с {Nm_D_List[0]} по {Nm_D_List[-1]} : {flatterm_List}')

daysStep = 7
Week_term_List = []
for i in range(len(flatterm_List) - daysStep):
    week_term = 0
    for j in range(daysStep):
        daysNum = i+j
        week_term = week_term + flatterm_List[daysNum]
    Week_term_List.append(week_term)
print(f"\n Семидневные промежутки температуры:")
print(Week_term_List)

maxSevenDays, minSevenDays = max(Week_term_List), min(Week_term_List)
print(
    f'\n Максимальный промежуток 7дневной температуры: {maxSevenDays}, минимальный промежуток 7дневной температуры {minSevenDays}')

maxIndex, minIndex = Week_term_List.index(
    maxSevenDays), Week_term_List.index(minSevenDays)
print(
    f'\n Индекс максимального промежутка 7дневной температуры: {maxIndex} (день), Индекс минимального промежутка 7дневной температуры {minIndex} (день)')


def printIntervals(index, type):
    S_D_List = []
    daysSum = 0
    for i in range(len(D_List)):
        daysSum = daysSum + D_List[i]
        S_D_List.append(daysSum)

    print()
    print(S_D_List)

    monthIn = 0
    for row in S_D_List:
        if (index <= row):
            monthIn = S_D_List.index(row)
            break

    print(f'({monthIn+1}) - месяц входа {type} индекса')

    if index < S_D_List[0] and ((index + daysStep) <= S_D_List[0]):
        print("случай 1 = все в мае")
        print(
            f'Промежуток {type} темп = с {index} {Nm_D_List[0]} по {index + daysStep} {Nm_D_List[0]}')


    elif index <= S_D_List[0] and ((index + daysStep) >= S_D_List[0]):
        print("случай 1.1 = конец мая переход в июнь")
        print(
            f'Промежуток {type} темп = с {index} {Nm_D_List[0]} по {(index + daysStep - S_D_List[0])} {Nm_D_List[1]}')


    elif ((index-S_D_List[(monthIn-1)]) < S_D_List[monthIn]) and ((index + daysStep)-S_D_List[(monthIn-1)]) < D_List[(monthIn-1)]:
        print("случай 2 = все в рамках месяца")
        print(
            f'Промежуток {type} темп = с {index-S_D_List[monthIn-1]} {Nm_D_List[monthIn]} по {((index+daysStep)-S_D_List[(monthIn-1)])} {Nm_D_List[monthIn]}')

    else:
        print("переход с месяца на месяц")
        startDay = index - S_D_List[monthIn-1]
        startMonth = Nm_D_List[monthIn-1]

        endDay = index + daysStep - S_D_List[monthIn] + 1
        endMonth = Nm_D_List[monthIn]

        print(
            f'Промежуток {type} темп = с {startDay} {startMonth} по {endDay} {endMonth}')


printIntervals(maxIndex, "max")
printIntervals(minIndex, "min")