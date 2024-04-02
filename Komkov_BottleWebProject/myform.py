from datetime import date
from bottle import post, request

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    username = request.forms.get('USERNAME')
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())