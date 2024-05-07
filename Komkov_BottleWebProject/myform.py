import json
import re
from datetime import date
from bottle import post, request

# ћетод проверки почты
def mailcheck(checkmail):
    pattern = re.compile('[a-zA-Z0-9]{1}[a-zA-Z0-9._%+\-]{4,28}[a-zA-Z0-9]{1}@(gmail.com|mail.ru|yandex.ru)')
    return re.fullmatch(pattern, checkmail)

@post('/home', method='post')
def my_form():
    # получение адреса из формы
    mail = request.forms.get('ADRESS')
    # ѕроверка вводимой почты
    if mailcheck(mail) == False:
        return "The email format is incorrect. E-mail should consist only of Latin letters, numbers and special characters, as well as have from 6 to 30 characters at the beginning and either @gmail.com , or @mail.ru, or yandex.ru at the end."
    # получение имени из формы
    username = request.forms.get('USERNAME')
    # получение вопроса из формы
    question = request.forms.get('QUEST')
    # ѕроверка правильности вопроса
    if len(question)<=3 or question[len(question)-1] != "?" or question.isdigit():
        return "Question should be longer that 3 chars, end with the symbol ? and not consist only of digits."
    # «агрузка данных из файла
    try:
        with open('questions.json', 'r') as read_json:
            questions = json.load(read_json)
    except FileNotFoundError:
        questions = {}
    except:
        return "Unknown error"
    # если введенна€ почта есть в словаре
    if mail in questions:
        # если им€ в словаре отличаетс€ от введенного
        if username != questions[mail][0]:
            # вывод сообщени€ об ошибке
            return "The username for this email is incorrect."
        # если вопросы не совпадают
        if question not in questions[mail][1:]:
            # добавление нового вопроса в список
            questions[mail].append(question)          
        else:
            return "The question has alredy been send."
    # если введенна€ почта нет в словаре
    else:
        # создание новой записи в словаре
        questions[mail] = [username, question]
    # запись данных в файл
    with open('questions.json', 'w') as file:
            json.dump(questions, file, indent=4) # 4 отступа дл€ сериализации
    # возвращение сообщени€
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())