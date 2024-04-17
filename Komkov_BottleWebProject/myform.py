import json
from datetime import date
from bottle import post, request

@post('/home', method='post')
def my_form():
    # ��������� ������ �� �����
    mail = request.forms.get('ADRESS')
    # ��������� ����� �� �����
    username = request.forms.get('USERNAME')
    # ��������� ������� �� �����
    question = request.forms.get('QUEST')
    # �������� ������������ �������
    if len(question)<=3 or question[len(question)-1] != "?" or question.isdigit():
        return "Question should be longer that 3 chars, end with the symbol ? and not consist only of digits."
    # �������� ������ �� �����
    try:
        with open('questions.json', 'r') as read_json:
            questions = json.load(read_json)
    except FileNotFoundError:
        questions = {}
    except:
        return "Unknown error"
    # ���� ��������� ����� ���� � �������
    if mail in questions:
        # ���� ��� � ������� ���������� �� ����������
        if username != questions[mail][0]:
            # ����� ��������� �� ������
            return "The username for this email is incorrect."
        # ���� ������� �� ���������
        if question not in questions[mail][1:]:
            # ���������� ������ ������� � ������
            questions[mail].append(question)          
        else:
            return "The question has alredy been send."
    # ���� ��������� ����� ��� � �������
    else:
        # �������� ����� ������ � �������
        questions[mail] = [username, question]
    # ������ ������ � ����
    with open('questions.json', 'w') as file:
            json.dump(questions, file, indent=4) # 4 ������� ��� ������������
    # ����������� ���������
    return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (username, mail, date.today())