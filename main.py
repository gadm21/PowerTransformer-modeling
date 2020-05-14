
import sys 
import time 
from functools import partial 

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit
from PyQt5.QtGui     import QPixmap, QPainter, QBrush, QPen, QFont
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import Qt 
class Window(QWidget):

    def __init__(self):
        super().__init__() 

        self.buttons = dict() 
        self.labels = dict() 

        self.transformer_probabilities_widgets = dict() 
        self.efficiency_widgets = dict() 
        self.short_circuit_widgets = dict() 
        

        self.setfont() 
        self.init_UI()

    def setfont(self ):
        font = QFont() 
        font.setFamily("Microsoft YaHei") 
        font.setPointSize(11)
        self.setFont(font) 

    def init_UI(self):
        self.setGeometry(300,300, 1200,600)

        self.init_tabs() 
        self.create_widgets_and_hide() 

        self.display_image('me.jpg') 

        self.show()

    def create_widgets_and_hide(self):
        self.transformer_probabilities_widgets['materials_window'] = QtGui.QComboBox(self)
        self.transformer_probabilities_widgets['meterials_window'].addItem("silicon iron")
        self.transformer_probabilities_widgets['meterials_window'].addItem("powder iron")
        self.transformer_probabilities_widgets['meterials_window'].move(50, 250)
        self.transformer_probabilities_widgets['meterials_window'].activated[str].connect(self.material_choice) 
        self.transformer_probabilities_widgets['meterials_window'].setVisible(False)  


    def init_tabs(self):
        self.create_button('Transformer Probabilities', (25, 25, 200, 40), self.init_transformer_probability_tab)
        self.create_button('Effeciency', (250, 25, 100, 40), self.init_efficiency_tab)
        self.create_button('Short-Circuit Test', (360, 25, 200, 40), self.init_short_circuit_tab) 
        self.create_button('Open-Circuit Test', (570, 25, 200, 40), self.on_clicked)

    def init_transformer_probability_tab(self) :
        self.hide_all_tabs()
        for key, value in self.transformer_probabilities_widgets.items() :
            value.setVisible(True) 
    
    def init_efficiency_tab(self):
        self.hide_all_tabs() 
        for key, value in self.efficiency_widgets.items():
            value.setVisible(True) 
    
    def init_short_circuit_tab(self):
        self.hide_all_tabs() 
        for key, value in self.short_circuit_widgets.items():
            value.setVisible(True) 


    def hide_all_tabs(self):
        for key, value in self.transformer_probabilities_widgets.items() :
            value.setVisible(False) 
        for key, value in self.efficiency_widgets.items():
            value.setVisible(False) 
        for key, value in self.short_circuit_widgets.items():
            value.setVisible(False) 


    def material_choice(self, choice) :
        print("chose:", choice) 

    def display_image(self, image_name):
        image = QPixmap(image_name) 
        if 'image_label' not in self.labels :
            self.create_label('image_label', ( 820, 100, image.width(), image.height())) 
        
        self.labels['image_label'].setPixmap(image) 





    def init_open_circuit_test(self):
        
        pass

    def paintEvent(self, e):

        global_painter = QPainter(self) 
        global_painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
        global_painter.drawRect(0, 0, self.width(), self.height()) 

        painter = QPainter(self)
        #painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(QtGui.QColor('#fcfcfc')))
 
        painter.drawRect(20, 20, 800,50)

    def create_button(self, name, coords, on_clicked = None):
        push_button = QtWidgets.QPushButton(name, self) 
        push_button.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))
        self.buttons[name] = push_button 
        
        if on_clicked : push_button.clicked.connect(partial(on_clicked, name))  
        return push_button 

    def create_label(self, name, coords, on_clicked):
        label = QtWidgets.QLabel(name, self) 
        label.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))
        label.setMinimumSize(QtCore.QSize(60, 0))
        self.labels[name] = label 
        
        return label 

    def create_drop_menu(self, options, coords) :
        menu = QtGui.QComboBox(self)
        for option in options :
            menu.addItem(option)
        menu.move(coords) 
        menu.activated[str].connect(on_clicked) 
        return menu 


    def on_clicked(self, name):
        if self.labels['image_label'].isVisible() : 
            self.labels['image_label'].setVisible(False) 
        else : 
            self.labels['image_label'].setVisible(True) 

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = Window() 
    sys.exit(app.exec_()) 