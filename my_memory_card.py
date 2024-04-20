from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QButtonGroup, QPushButton, QGroupBox, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from random import shuffle, randint

class Question():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
quest_list=[]
quest_list.append(Question('как дела','хорошо','норм','отлино','плохо'))
quest_list.append(Question('какое время года','осень','зима','лето','весна'))
quest_list.append(Question('В каком году было крешение руси','988','1111','667','244'))
quest_list.append(Question('что делаешь','лежу','сижу','стою','летаю'))
quest_list.append(Question('как тебя зовут','по имени','как мама назвала','меня не зовут','вчера звали'))
quest_list.append(Question('сколько тебе лет','13','29','47','76'))
quest_list.append(Question('сколько ты убил птиц','98','106','24','1'))
quest_list.append(Question('что вчера ел','кашу','еду','морковку','капусту'))
quest_list.append(Question('сколько часов ты спал','-9','7','2','22'))
quest_list.append(Question('кто такие цукаты','мангустины','танго','журавль','цифра'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('zxc')
main_win.resize(800, 600)

btn_OK = QPushButton('Ответить')
quest = QLabel('Когда я родился арбуз')

RadioGroupBox = QGroupBox('Ну подумай')
rbtn1 = QRadioButton('Завтра')
rbtn2 = QRadioButton('Cегодня')
rbtn3 = QRadioButton('Вчера')
rbtn4 = QRadioButton('Послезавтра')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('результат')
lb_result = QLabel('прав да нет')
lb_correct = QLabel('ответ')

layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lb_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ans4.addWidget(lb_correct, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layout_ans4)

layout_line = QVBoxLayout()
layout_line.addWidget(quest, alignment = (Qt.AlignCenter | Qt.AlignCenter))
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line.addWidget(btn_OK, stretch=2)
main_win.setLayout(layout_line)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Продолжить')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quest.setText(q.quest)
    lb_correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Угадал')
        main_win.score +=1
        print('Статистика\nВсего вопросов - ', main_win.total, "\nКоличество правельных ответов -", main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Не угадал')
            print('Рейтинг:', main_win.score/main_win.total*100,'%')
def next_quest():
    main_win.total +=1
    print('Статистика\nВсего вопросов - ', main_win.total, "\nКоличество правельных ответов -", main_win.score)
    print('Рейтинг:', main_win.score/main_win.total*100,'%')
    cur_quest = randint(1, len(quest_list)-1)
    q = quest_list[cur_quest]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_quest()

main_win.total = 0 
main_win.score = 0
btn_OK.clicked.connect(click_OK)
next_quest()

main_win.show()
app.exec_()