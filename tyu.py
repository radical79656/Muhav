from PyQt5.QtCore import Qt
from random import shuffle
from random import randint
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)

app = QApplication([]) 
win = QWidget() 
 
pixmap = QPixmap("logo.png") 
lbl = QLabel() 
lbl.setPixmap(pixmap) 
 
win.setWindowIcon(QIcon('logo.png')) 
 
main_layout = QVBoxLayout() 
main_layout.addWidget(lbl) 
win.setLayout(main_layout) 
 
btn_l = QHBoxLayout() 
btn_l2 = QHBoxLayout() 
 
btn_info=QPushButton('Новости') 
btn_reg=QPushButton('Регистрация') 
btn_score=QPushButton('Мой cчет') 
btn_test=QPushButton('Викторина') 
 
btn_l.addWidget(btn_info) 
btn_l.addWidget(btn_reg) 
btn_l2.addWidget(btn_score) 
btn_l2.addWidget(btn_test) 
 
main_layout.addLayout(btn_l) 
main_layout.addLayout(btn_l2) 
 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        

label = QLabel()
pixmap = QPixmap('super car2.png')
label.setPixmap(pixmap)
btn_OK = QPushButton('Ответить')
btn_OK.setStyleSheet(
    'width: 70px;'
    'height: 30px;'
    'front-size: 20px;'
    'background-color: #1cb317;'
    'border: 2px solid white;'
    'color: white;'
    )



lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(label, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # кнопка должна быть большой
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()    
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

question_list = []
question_list.append(Question('Как называется активная оболочка Земли, которая населена живыми организмами?', 'Биосфера', 'Литосфера ', 'Геосфера', 'Гидросфера'))


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг:', (window.score / window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно! Правильный ответ:')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)

    q = question_list[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
#window.setWindowIcon(QtGui.QIcon('лого.png'))

btn_OK.clicked.connect(click_ok)

window.score = 0
window.total = 0

next_question()
window.resize(400, 300)
window.setStyleSheet(
    'background-color:#87CEEB;'
    'color: black;'
    )

 
def change_win_reg(): 
    win.hide() 
    window.show() 
 
win.show() 
btn_test.clicked.connect(change_win_reg) 
app.exec_()
