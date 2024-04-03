import pdb
from datetime import date
from bottle import post, request

@post('/home', method='post')
def my_form():
    # создание словаря
    questions = {}
    # получение адреса из формы
    mail = request.forms.get('ADRESS')
    # получение имени из формы
    username = request.forms.get('USERNAME')
    # получение вопроса из формы
    question = request.forms.get('QUEST')
    # создание словаря
    questions = {mail : question}
    # запуск отладчика
    pdb.set_trace()
    # возвращение сообщения
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())