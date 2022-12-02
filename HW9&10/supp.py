def supportAnswer(user_id, user_req, user_answer):
        print(user_id, user_req, user_answer)


with open('supp.txt', 'r', encoding='utf-8', newline=str) as f:
    data = f.readlines()
    
req_List = []
for row in data:
    req_List.append(row[:-1].split('/'))
for req in req_List:
    print(req)

answerNum = int(input('Введите номер ответа: '))
if answerNum > len(req_List):
    print("такого вопроса не существует")
else:
    print(f'вы будете отвечать на {req_List[answerNum]}')
    answer = (input('Ваш ответ: '))
    req_List[answerNum].append(answer)
    print(f'ваш ответ сохранен в {req_List[answerNum]}')

unansweredList = list(filter(lambda row: len(row) == 4, req_List))
print(unansweredList)
remainingReqs =""
for row in unansweredList:
        remainingReqs = remainingReqs  + "/".join(row) + '\n'
print(remainingReqs)

with open("support.txt", "w", encoding="utf-8") as f:
    f.write(remainingReqs)

#  отвеченный вопрос:
answersList = list(filter(lambda row: len(row) > 4, req_List))
user_id = answersList[0][0]
user_req = answersList[0][3]
user_answer = answersList[0][4]

supportAnswer(user_id, user_req, user_answer)