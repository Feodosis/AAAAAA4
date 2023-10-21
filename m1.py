from PyQt5.QtWidgets import QApplication

from random import choice, shuffle
from time import sleep

app = QApplication([])

from m2 import*
from m3 import*

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wroung(self):
        self.count_ask += 1
q1 = Question("Квантова теорія полягає в тому, що.. ", "Елементарна частка знаходить певний стан лише в момент спостереження", "У квантів своє життя", "Часток не існує", "Квантів не існує")
q2 = Question("Сингулярність чорних дір..", "Точка в їхньому центрі де сила гравітації стає нескінченною і об'єм об'єкта стискається до нескінченно малого розміру", "Де сила гравітації стає нескінченною", "Їхній дотик", "Точка в їхньому центрі, де гравітація обнуляється і об'єкт зникає")
q3 = Question("Що являють собою квантові всесвіти ?", "Всесвіт, в якому частка може перебувати в декількох місцях одночасно", "Паралельний всесвіт", "Всесвіт із квантів", "Нічого")
q4 = Question("Суперпозиція це..", "Коли результуючий ефект кількох незалежних впливів є сумою ефектів, що викликаються кожним впливом окремо", "Немає конкретного визначення", "Дуже крута позиція", "Знаходження об'єкта у різних вимірах")
q5 = Question("Квантова заплутаність це..", "Квантовомеханічне явище, при якому квантові стани двох або більшої кількості об'єктів виявляються взаємозалежними", "Коли об'єкти плутаються", "Знищення всіх об'єктів", "Такого не існує")
q6 = Question("Реакція перетворення частинки та античастинки при їх зіткненні на будь-які інші частинки, відмінні від вихідних..", "Анігіляція", "Ентропія", "Ефект Снука", "Диполь")
q7 = Question("Кіт Шредінгера..", "Герой уявного експерименту, в якому кіт перебуває рівночасно у двох станах - живий і мертвий", "Ім'я вченого", "Ім'я мого кота", "Одиниця виміру")
q8 = Question("Ядерний фотоефект це..", "Реакції що відбуваються під час поглинання гамма-квантів ядрами атомів", "Реакція при якій гамма-кванти поглинають ядра атомів", "Реакція при якій гамма-кванти стають невидимими", "Не існуючий фотоефект")
q9 = Question("При зіткненні білої і чорної діри утворюється..", "Вони не зіткнуться, при цьому матерія перетікатиме з однієї діри в другу", "Анігіляція", "Мутація", "Нічого не відбудеться")
q10 = Question("При злитті двох чорних дір відбудеться..", "Утворення ще більшої та масивної чорної діри", "Передача енергії або зміна траєкторії руху", "Анігіляція", "Злиття не відбудеться")
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText("Правильно!")
                answer.setChecked(False)
                break
    else:
        lb_result.setText("Неправильно!")
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.text() == "Відповісти":
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText("Наступне запитання")
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText("Відповісти")
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)
def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()