from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
app = QApplication([])
my_win = QWidget()
a = QLabel("В каком году канал получил золотую кнопку от You Тube?")
c = QRadioButton('2005')
d = QRadioButton('2010')
e = QRadioButton('2015')
x = QRadioButton('2020')
h = QHBoxLayout()
h.addWidget(a, alignment = Qt.AlignCenter)
m = QHBoxLayout()
m.addWidget(c, alignment = Qt.AlignCenter)
m.addWidget(d, alignment = Qt.AlignCenter)
v = QHBoxLayout()
v.addWidget(e, alignment = Qt.AlignCenter)
v.addWidget(x, alignment = Qt.AlignCenter)
q = QVBoxLayout()
q.addLayout(h)
q.addLayout(m)
q.addLayout(v)
def showwin():
    g = QMessageBox()
    g.setText("Вы выиграли")
    g.exec_()
def joc():
    wow = QMessageBox()
    wow.setText("Вы проиграли")
    wow.exec_()
c.clicked.connect(joc)
d.clicked.connect(joc)
e.clicked.connect(showwin)
x.clicked.connect(joc)
my_win.setLayout(q)

my_win.show()
app.exec_()

