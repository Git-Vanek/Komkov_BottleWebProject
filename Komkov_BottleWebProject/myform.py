from datetime import date
from bottle import post, request

@post('/home', method='post')
def my_form():
    # получение адреса из формы
    mail = request.forms.get('ADRESS')
    # получение имени из формы
    username = request.forms.get('USERNAME')
    # возвращение сообщения
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())