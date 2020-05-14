
import sys 
import time 
from functools import partial 

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit, QComboBox, QLabel, QLineEdit 
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

        self.show()

    def create_widgets_and_hide(self):
        #tranformer probabilites tab
        self.transformer_probabilities_widgets['materials_window'] = self.create_drop_menu(['silicon iron', 'powder iron'], (250,300,100,100), self.material_choice)
        self.transformer_probabilities_widgets['hysterisis_loss_label'] = self.create_label('Hysterisis Loss= B_max^β  k_c  V f^α', (100, 90, 100, 100))
        self.transformer_probabilities_widgets['B_peak'] = self.create_label('B_peak', (120, 120, 10,10))
        self.transformer_probabilities_widgets['frequency'] = self.create_label('frequency', (120, 140, 10,10))
        self.transformer_probabilities_widgets['frequency_edit'] = self.create_line_edit((250, 140))
        self.transformer_probabilities_widgets['steimetz_constant'] = self.create_label('steimetz constant', (120, 160, 10,10))
        self.transformer_probabilities_widgets['volume'] = self.create_label('volume', (120, 180, 10,10))
        self.transformer_probabilities_widgets['volume_edit'] = self.create_line_edit((250, 180))

        self.transformer_probabilities_widgets['eddy_Loss'] = self.create_label('Eddy Loss= B_max^2  k_c  V f^2 t^2', (500, 90, 10,10))
        self.transformer_probabilities_widgets['lamination_thickness'] = self.create_label('lamination thickness', (520, 120, 10,10))
        self.transformer_probabilities_widgets['lamination_thickness_edit'] = self.create_line_edit( (600, 120, 10,10))

        self.transformer_probabilities_widgets['materials_table'] = self.create_image('materials_table.jpg', (50, 320))


        self.efficiency_widgets['efficiency_button'] = self.create_button('efficiency', [100, 100, 50, 50], self.init_open_circuit_test)
        self.efficiency_widgets['efficiency_button'].setVisible(False) 


    def init_tabs(self):
        self.create_button('Transformer Probabilities', (25, 25, 200, 40), self.init_transformer_probability_tab)
        self.create_button('Effeciency', (250, 25, 100, 40), self.init_efficiency_tab)
        self.create_button('Short-Circuit Test', (360, 25, 200, 40), self.init_short_circuit_tab) 
        self.create_button('Open-Circuit Test', (570, 25, 200, 40), self.init_open_circuit_test)

    def init_transformer_probability_tab(self) :
        self.hide_all_tabs()
        print("all tabs hidded")
        for key, value in self.transformer_probabilities_widgets.items() :
            print("showing :", key) 
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


    


    



    def init_open_circuit_test(self):
        
        pass

    def paintEvent(self, e):
        '''
        global_painter = QPainter(self) 
        global_painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
        global_painter.drawRect(0, 0, self.width(), self.height()) 
        '''
        painter = QPainter(self)
        #painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        #painter.setBrush(QBrush(QtGui.QColor('#fcfcfc')))
        painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
 
        painter.drawRect(20, 20, 800,50)

    def create_button(self, name, coords, on_clicked = None):
        push_button = QPushButton(name, self) 
        push_button.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))
        if on_clicked : push_button.clicked.connect(on_clicked)  
        return push_button 

    def create_label(self, name, coords):
        label = QLabel(name, self) 
        label.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))  
        label.adjustSize() 
        label.setMinimumSize(QtCore.QSize(60, 0))
        return label 

    def create_image(self, image_name, coords):
        image = QPixmap(image_name) 
        label = QLabel(self) 
        label.setPixmap(image) 
        label.setGeometry(QtCore.QRect(coords[0], coords[1], image.width(), image.height()))
        return label 

    def create_line_edit(self, coords):
        line = QLineEdit(self) 
        line.move(coords[0], coords[1]) 
        return line 

    def create_drop_menu(self, options, coords, on_clicked) :
        menu = QComboBox(self) 
        for option in options :
            menu.addItem(option)
        menu.move(coords[0], coords[1])
        #menu.move(coords[0], coords[1])
        menu.activated[str].connect(on_clicked)
        return menu 















if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = Window() 
    sys.exit(app.exec_()) 