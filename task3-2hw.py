# Даны две строки. Посчитайте сколько раз каждый 
# символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

print("Введите строку в которой ищем совпадения: ")
string_1 = input()
print("Введите строку, чьи эелемнты мы ищем в 1й строке: ")
string_2 = input()

count = 0

if len(string_1) > len(string_2):
    print(string_1)
    for i in range (len(string_1)):
        count=0
        for j in range (len(string_2)):
            if string_2[j] == string_1[i]:
                count+=1
        print(str(string_2[j]), '= ', str(count))

else:
    print(string_2)
    for i in range (len(string_2)):
        count = 0
        for j in range (len(string_1)):
            if string_1[i] == string_2[j]:
                count+=1
        print(str(string_1[j]), '= ', str(count))

