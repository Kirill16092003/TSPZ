import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,\
    QGridLayout, QStyleFactory, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()

    def keypad(self):
        container = QWidget()
        container.setLayout(QGridLayout())
        # button
        self.result_field = QLineEdit()
        button_clear = QPushButton('C', clicked = self.clear_result_field)
        button_result = QPushButton('=', clicked = self.make_result)
        button_0 = QPushButton('0', clicked = lambda: self.num_press('0'))
        button_1 = QPushButton('1', clicked = lambda: self.num_press('1'))
        button_2 = QPushButton('2', clicked = lambda: self.num_press('2'))
        button_3 = QPushButton('3', clicked = lambda: self.num_press('3'))
        button_4 = QPushButton('4', clicked = lambda: self.num_press('4'))
        button_5 = QPushButton('5', clicked = lambda: self.num_press('5'))
        button_6 = QPushButton('6', clicked = lambda: self.num_press('6'))
        button_7 = QPushButton('7', clicked = lambda: self.num_press('7'))
        button_8 = QPushButton('8', clicked = lambda: self.num_press('8'))
        button_9 = QPushButton('9', clicked = lambda: self.num_press('9'))
        button_add = QPushButton('+', clicked = lambda: self.oper_press('+'))
        button_sub = QPushButton('-', clicked = lambda: self.oper_press('-'))
        button_mul = QPushButton('*', clicked = lambda: self.oper_press('*'))
        button_divd = QPushButton('/', clicked = lambda: self.oper_press('/'))
        button_none = QPushButton('^', clicked = lambda: self.oper_press('**'))
        button_pop_in2 = QPushButton(':-D')
        # container
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(button_pop_in2,1,0)
        container.layout().addWidget(button_none,1,1)
        container.layout().addWidget(button_clear,1,2)
        container.layout().addWidget(button_result,1,3)
        container.layout().addWidget(button_9,2,0)
        container.layout().addWidget(button_8,2,1)
        container.layout().addWidget(button_7,2,2)
        container.layout().addWidget(button_add,2,3)
        container.layout().addWidget(button_6,3,0)
        container.layout().addWidget(button_5,3,1)
        container.layout().addWidget(button_4,3,2)
        container.layout().addWidget(button_sub,3,3)
        container.layout().addWidget(button_3,4,0)
        container.layout().addWidget(button_2,4,1)
        container.layout().addWidget(button_1,4,2)
        container.layout().addWidget(button_mul,4,3)
        container.layout().addWidget(button_0,5,0,1,3)
        container.layout().addWidget(button_divd,5,3)
        self.layout().addWidget(container)

    def num_press(self, num_id):
        self.temp_nums.append(num_id)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText((''.join(self.fin_nums) + temp_string).replace("**", "^"))
        else:
            self.result_field.setText(temp_string.replace("**", "^"))

    def oper_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))
        self.result_field.setText(''.join(self.fin_nums).replace("**", "^"))

    def make_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        try:
            result_string = eval(fin_string)
        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('ZeroDivisionError')
            msg.setIcon(msg.Warning)
            msg.exec()
            self.result_field.clear()
            self.temp_nums = []
            self.fin_nums = []
        except OverflowError:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('OverflowError')
            msg.setIcon(msg.Warning)
            msg.exec()
            self.result_field.clear()
            self.temp_nums = []
            self.fin_nums = []
        else:
            fin_string += '='
            fin_string += str(result_string)
            self.result_field.setText(fin_string.replace("**", "^"))

    def clear_result_field(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


app = QApplication([])
mw = MainWindow()
app.setStyle(QStyleFactory.create('Fusion'))
app.exec_()
