
import sys 
import time 
from functools import partial 

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit

from PyQt5.QtWidgets import QApplication 

class Window(QWidget):

    def __init__(self):
        super().__init__() 

        self.buttons = dict() 
        self.labels = dict() 

        self.init_UI()

    def init_UI(self):
        self.setGeometry(300,300, 1000,500)
        
        self.create_button('button', (100, 100, 50, 20), self.on_clicked)
        self.create_label('label',(160, 100, 50, 20) )
        


        self.show()
        
    def init_open_circuit_test(self):
        
        pass

    def create_button(self, name, coords, on_clicked = None):
        push_button = QtWidgets.QPushButton(name, self) 
        push_button.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))
        self.buttons[name] = push_button 
        
        if on_clicked : push_button.clicked.connect(partial(on_clicked, name))  
        return push_button 

    def create_label(self, name, coords):
        label = QtWidgets.QLabel(name, self) 
        label.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))
        label.setMinimumSize(QtCore.QSize(60, 0))
        self.labels[name] = label 
        
        return label 

    def on_clicked(self, name):
        
        pass 

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = Window() 
    sys.exit(app.exec_()) 