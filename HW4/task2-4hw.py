data = open('icecream.txt', encoding = 'utf-8')
icecream = data.readlines()
data.close()

first = set(icecream[0].replace('\n', '').split(', '))
second = set(icecream[1].replace('\n', '').split(', '))

print(first.difference(second))
