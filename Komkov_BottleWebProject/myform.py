import pdb
from datetime import date
from bottle import post, request

@post('/home', method='post')
def my_form():
    # �������� �������
    questions = {}
    # ��������� ������ �� �����
    mail = request.forms.get('ADRESS')
    # ��������� ����� �� �����
    username = request.forms.get('USERNAME')
    # ��������� ������� �� �����
    question = request.forms.get('QUEST')
    # �������� �������
    questions = {mail : question}
    # ������ ���������
    pdb.set_trace()
    # ����������� ���������
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())