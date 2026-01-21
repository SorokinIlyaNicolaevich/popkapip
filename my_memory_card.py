#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QPushButton ,QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import randint
from random import shuffle

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2

        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какой из перечисленных косметических продуктов самый востребованный', 'Консилер', 'Тональный крем', 'Румяна', 'Пудра'))
question_list.append(Question('Какой предмет в школе чаще всего ученики выбирают на ОГЭ', 'Обществознание', 'Физика', 'Английский', 'Информатика'))
question_list.append(Question('Какой мультфильм выпустила компания Дисней', 'Суперсемейка','Смешарики','Лунтик','Медведи соседи'))



app = QApplication([])

win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(400, 100)
#создание виджетов главного окна
winner = QLabel('Какой национальности не существует')
rgb = QGroupBox('Варианты ответов')
answer = QPushButton('Ответить')
button = QRadioButton('Энцы')
button2 = QRadioButton('Чулымцы')
button3 = QRadioButton('Смурфы')
button4 = QRadioButton('Алеуты')

rgbalet = QButtonGroup()
rgbalet.addButton(button)
rgbalet.addButton(button2)
rgbalet.addButton(button3)
rgbalet.addButton(button4)

ans = QGroupBox('Результат теста')
resl = QLabel('Правильно/Неправильно')
dosh = QLabel('Правильный ответ')
ansLayout = QVBoxLayout()
ansLayout.addWidget(resl, alignment = Qt.AlignLeft)
ansLayout.addWidget(dosh, alignment = Qt.AlignCenter)
ans.setLayout(ansLayout)


#расположение виджетов по лэйаутам
v_line = QVBoxLayout()
h_line = QHBoxLayout()
h_line2 = QHBoxLayout()
v_line3 = QVBoxLayout()
v_line.addWidget(winner, alignment = Qt.AlignCenter)
h_line.addWidget(button, alignment = Qt.AlignCenter)
h_line.addWidget(button2, alignment = Qt.AlignCenter)
h_line2.addWidget(button3, alignment = Qt.AlignCenter)
h_line2.addWidget(button4, alignment = Qt.AlignCenter)


v_line3.addLayout(h_line)
v_line.setSpacing(5)
v_line3.addLayout(h_line2)
rgb.setLayout(v_line3)

v_line.addWidget(winner)
v_line.addWidget(rgb)
v_line.addWidget(ans)

v_line.addWidget(answer)
ans.hide()
win.setLayout(v_line)

#обработка нажатий на переключатели
def show_resalt():
    rgb.hide()
    ans.show()
    answer.setText('Следующий вопрос')

def show_question():
    ans.hide()
    rgb.show()
    answer.setText('Ответить')
    rgbalet.setExclusive(False)
    button.setChecked(False)
    button2.setChecked(False)    
    button3.setChecked(False)
    button4.setChecked(False)
    rgbalet.setExclusive(True)
def start_test():
    if answer.text() == 'Ответить':
        show_resalt()
    else:
        next_question()
answers = [button, button2, button3, button4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    winner.setText(q.question)
    dosh.setText(q.right_answer)
    show_question()
#def show_correct()



def check_answer():
    global score
    if answers[0].isChecked():
        resl.setText('Правильно')
        score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            resl.setText('Неправильно')
    start_test()

def next_question():
    global total
    global score
    total += 1
    print('Статистика')
    print('Всего вопросов:', total)
    print('Правильный ответов:', score)
    print('Рейтинг:', score / total * 100)
    num_q = randint(0,len(question_list)-1)
    
    q = question_list[num_q]
    ask(q)

def clickok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

'''cur_question = randint(0, len(questions_list) - 1)
q = questions_list[cur_question]'''


score = 0
total = 0

next_question()
#обработка событий
answer.clicked.connect(clickok)




#запуск приложения



win.show()
app.exec_()
































































































































































































































































































































































































































































