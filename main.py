from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QFormLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QListWidget, QListWidgetItem, QPushButton,
                             QRadioButton, QSpinBox, QTableWidget, QVBoxLayout,
                             QWidget)

app = QApplication([])
win_card = QWidget()
win_card.setWindowTitle('MemoryCard')
one = QRadioButton('apple')
two = QRadioButton('appl')
three = QRadioButton('ayppl')
four = QRadioButton('piapl')
box_min = QSpinBox()
#створ таймер, який можна зупинити
box_min.setValue(30)
#
q1 = QLabel('Яблуко?')
one1 = QPushButton("Меню")
two1 = QPushButton("Відпочити")
three1 = QPushButton("Відповісти")

layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()
layoutV4 = QHBoxLayout()
#4 кнопки в групу, для прописування для всіх програм
radiogroup = QButtonGroup()
radiogroup.addButton(one)
radiogroup.addButton(two)
radiogroup.addButton(three)
radiogroup.addButton(four)
RadioGroupBox = QGroupBox("")
AnsGroupBox = QGroupBox("Результат теста")
#приєднання до ліній
layoutH1 = QHBoxLayout()
layoutV1 = QHBoxLayout()
layoutV2 = QHBoxLayout()
layoutV1.addWidget(one)
layoutV1.addWidget(three)
layoutV2.addWidget(two)
layoutV2.addWidget(four)
layoutH1.addLayout(layoutV1)
layoutH1.addLayout(layoutV2 )
ansG = QGroupBox('Результат тексту')
Ans_res = QLabel("")#правильно чи ні
Ans_cor = QLabel("apple")
layoutV3 = QHBoxLayout()
layoutV3.addWidget(Ans_res, alignment = (Qt.AlignLeft | Qt.AlignTop))
layoutV3.addWidget(Ans_cor, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layoutV3)
RadioGroupBox.setLayout(layoutH1)
AnsGroupBox.hide()

layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QVBoxLayout()

layoutH2.addWidget(one1)
layoutH2.addWidget(two1)
layoutH2.addWidget(box_min)
layoutH2.addWidget(QLabel('хвилин'))
layoutH2.addStretch(1)

layoutH3.addWidget(q1, alignment = Qt.AlignHCenter | Qt.AlignVCenter )
layoutH4.addWidget(AnsGroupBox)
layoutH4.addWidget(RadioGroupBox)
layoutH5.addStretch(1)
layoutH5.addWidget(three1)
layoutH5.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layoutH2, stretch = 1)
layout_card.addLayout(layoutH3, stretch = 2)
layout_card.addLayout(layoutH4, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layoutH5, stretch  = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
win_card.setLayout(layout_card)
def show_result():
       RadioGroupBox.hide()
       AnsGroupBox.show()
       three1.setText('наступний')
def show_question():   
   RadioGroupBox.show()
   AnsGroupBox.hide()
   three1.setText('Відповісти')
 
   radiogroup.setExclusive(False) 
   one.setChecked(False)
   two.setChecked(False)
   three.setChecked(False)
   four.setChecked(False)
   radiogroup.setExclusive(True)
from random import shuffle

frm_question = 'Яблоко'
frm_right = 'apple'
frm_wrong1 = 'appl'
frm_wrong2 = 'ayppl'
frm_wrong3 = 'piapl'
text_wrong = 'False'
text_correct = 'True'
radio_list = [one, two, three, four]
shuffle(radio_list)
answer = radio_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]
def show_data(): 
   q1.setText(frm_question)
   Ans_cor.setText(frm_right)
   answer.setText(frm_right)
   wrong_answer1.setText(frm_wrong1)
   wrong_answer2.setText(frm_wrong2)
   wrong_answer3.setText(frm_wrong3)
def check_result():
       correct = answer.isChecked()
       if correct:
              Ans_res.setText(text_correct)
              show_result()
       else:
              incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
              if incorrect:
                     Ans_res.setText(text_correct)
                     show_result()
def click_ok():
       if three1.text() != 'наступний':
              check_result()
show_data()
show_question()
three1.clicked.connect(click_ok)
win_card.show()
app.exec_()
      
