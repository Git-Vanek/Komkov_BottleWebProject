import json
from datetime import date
from bottle import post, request

@post('/home', method='post')
def my_form():
    # получение адреса из формы
    mail = request.forms.get('ADRESS')
    # получение имени из формы
    username = request.forms.get('USERNAME')
    # получение вопроса из формы
    question = request.forms.get('QUEST')
    # Проверка правильности вопроса
    if len(question)<=3 or question[len(question)-1] != "?" or question.isdigit():
        return "Question should be longer that 3 chars, end with the symbol ? and not consist only of digits."
    # Загрузка данных из файла
    try:
        with open('questions.json', 'r') as read_json:
            questions = json.load(read_json)
    except FileNotFoundError:
        questions = {}
    except:
        return "Unknown error"
    # если введенная почта есть в словаре
    if mail in questions:
        # если имя в словаре отличается от введенного
        if username != questions[mail][0]:
            # вывод сообщения об ошибке
            return "The username for this email is incorrect."
        # если вопросы не совпадают
        if question not in questions[mail][1:]:
            # добавление нового вопроса в список
            questions[mail].append(question)          
        else:
            return "The question has alredy been send."
    # если введенная почта нет в словаре
    else:
        # создание новой записи в словаре
        questions[mail] = [username, question]
    # запись данных в файл
    with open('questions.json', 'w') as file:
            json.dump(questions, file, indent=4) # 4 отступа для сериализации
    # возвращение сообщения
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())