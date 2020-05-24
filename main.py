
import sys 
import time 
from functools import partial 

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit, QComboBox, QLabel, QLineEdit 
from PyQt5.QtGui     import QPixmap, QPainter, QBrush, QPen, QFont
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import Qt 
import pyqtgraph as pg
import random 

from Transformer import Transformer 
class Window(QWidget):

    def __init__(self):
        super().__init__() 

        self.plots = [] 
        self.core_material = 'silicon iron' 
        self.transformer = Transformer(self.core_material)  

        self.buttons = dict() 
        self.labels = dict() 

        self.transformer_probabilities_widgets = dict() 
        self.efficiency_widgets = dict() 
        self.short_circuit_widgets = dict() 
        self.main_tab_widgets = dict()
        

        self.setfont() 
        self.init_UI()

    def setfont(self ):
        font = QFont() 
        font.setFamily("Microsoft YaHei") 
        font.setPointSize(11)
        self.setFont(font) 

    def init_UI(self):
        self.setGeometry(300,300, 1400,600)

        self.init_tabs() 
        self.create_widgets_and_hide() 
        self.init_main_tab() 

        self.show()

    def create_widgets_and_hide(self):

        #main tab 
        self.main_tab_widgets['logo'] = self.create_image('Nile_University_logo.png', (700,26), resize = True)
        self.main_tab_widgets['nile_university'] = self.create_label('Nile University', (870, 25, 10,10), font = True) 
        self.main_tab_widgets['school'] = self.create_label("school of engineering and applied science", (870, 55, 10, 10), font = True)
        self.main_tab_widgets['dep'] = self.create_label("Electronics and Computer Engineering (ECE)", (870, 85, 10, 10), font = True)
        self.main_tab_widgets['course'] = self.create_label("Electric Machines (ECEN 403)", (870, 115, 10, 15), font = True)
        self.main_tab_widgets['project'] = self.create_label("Transformer design & modeling", (800, 300, 10, 15), font = 25)

        self.main_tab_widgets['by'] = self.create_label("By - Gad Mohamed Gad", (750, 500, 10, 15))
        self.main_tab_widgets['to'] = self.create_label("To - Dr. Heba Ahmed Hassan & Eng. Shadwa Mohsen", (750, 525, 10, 15))
        

        #tranformer probabilites tab
        self.transformer_probabilities_widgets['materials_window'] = self.create_drop_menu(['silicon iron', 'powdered iron'], (100,270,100,100), self.material_choice)
        self.transformer_probabilities_widgets['hysterisis_loss_label'] = self.create_label('Hysterisis Loss= B_max^β  k_c  V f^α', (100, 90, 100, 100))
        self.transformer_probabilities_widgets['B_peak'] = self.create_label('B_peak', (100, 120, 10,10))
        self.transformer_probabilities_widgets['frequency'] = self.create_label('frequency', (100, 140, 10,10))
        self.transformer_probabilities_widgets['frequency_edit'] = self.create_line_edit((230, 140))
        self.transformer_probabilities_widgets['steimetz_constant'] = self.create_label('steimetz constant', (100, 160, 10,10))
        self.transformer_probabilities_widgets['volume'] = self.create_label('volume', (100, 180, 10,10))
        self.transformer_probabilities_widgets['volume_edit'] = self.create_line_edit((230, 180))

        self.transformer_probabilities_widgets['eddy_Loss'] = self.create_label('Eddy Loss= B_max^2  k_c  V f^2 t^2', (500, 90, 10,10))
        self.transformer_probabilities_widgets['lamination_thickness'] = self.create_label('lamination thickness', (500, 120, 10,10))
        self.transformer_probabilities_widgets['lamination_thickness_edit'] = self.create_line_edit( (660, 120, 10,10))

        self.transformer_probabilities_widgets['eddy_loss_result'] = self.create_label("Eddy Loss = ", (880, 200, 10,10))
        self.transformer_probabilities_widgets['eddy_loss_result_edit'] = self.create_line_edit((1000, 200))
        self.transformer_probabilities_widgets['hysterisis_loss_result'] = self.create_label("Hysterisis Loss = ", (880, 230, 10,10))
        self.transformer_probabilities_widgets['hysterisis_loss_result_edit'] = self.create_line_edit((1000, 230))
        self.transformer_probabilities_widgets['core_loss_result'] = self.create_label("Core Losses = ", (880, 260, 10,10))
        self.transformer_probabilities_widgets['core_loss_result_edit'] = self.create_line_edit((1000, 260))

        self.transformer_probabilities_widgets['calculate_button'] = self.create_button('calculate', (250,270,70,35), self.calculate_iron_losses)
        self.transformer_probabilities_widgets['materials_table'] = self.create_image('materials_table.jpg', (50, 310))

        self.transformer_probabilities_widgets['N1'] = self.create_label('N1:', (865, 110,10,10))
        self.transformer_probabilities_widgets['N1_edit'] = self.create_line_edit((890, 110))
        self.transformer_probabilities_widgets['N2'] = self.create_label('N2:', (865, 140,10,10))
        self.transformer_probabilities_widgets['N2_edit'] = self.create_line_edit((890, 140))


        #efficiency tab
        self.efficiency_widgets['V1'] = self.create_label('V1:', (100,100,10,10))
        self.efficiency_widgets['V1_edit'] = self.create_line_edit((130, 100))
        self.efficiency_widgets['Load'] = self.create_label('Load (z,p.f.):', (310,100,10,10))
        self.efficiency_widgets['Load_edit'] = self.create_line_edit((405, 100))

        self.efficiency_widgets['plot'] = self.create_button('plot', (610, 100,80, 25), self.plot)
        self.efficiency_widgets['undo'] = self.create_button('undo', (710, 100, 80, 25), self.undo_plot) 
        self.efficiency_widgets['clear'] = self.create_button('clear', (810, 100, 80, 25), self.clear_plots)
        
        self.efficiency_widgets['efficiency'] = self.create_label('Efficiency:', (100, 150, 10, 10))    
        self.efficiency_widgets['efficiency_edit'] = self.create_line_edit((190, 150))
        self.efficiency_widgets['calculate_efficiency'] = self.create_button('calculate efficiency', (430, 150, 170, 30), self.calculate_efficiency) 



        #short-citcuit test tab 
        self.short_circuit_widgets['source_voltage'] = self.create_label('source voltage', (100, 90, 10,10))
        self.short_circuit_widgets['source_voltage_edit'] = self.create_line_edit((220, 90))
        self.short_circuit_widgets['record_measurements_button'] = self.create_button('record measurements', (440, 90,220,25), self.record_measurements)

        self.short_circuit_widgets['power'] = self.create_label('power = ', (100, 140, 10,10))
        self.short_circuit_widgets['power_edit'] = self.create_line_edit((170, 140))

        self.short_circuit_widgets['current'] = self.create_label('current = ', (480, 140, 10,10))
        self.short_circuit_widgets['current_edit'] = self.create_line_edit((560, 140))

        self.short_circuit_widgets['R_eq'] = self.create_label('R_eq = ', (780, 140, 10,10))
        self.short_circuit_widgets['R_eq_edit'] = self.create_line_edit((830, 140))

        self.short_circuit_widgets['short_circuit_test_figure'] = self.create_image('short_circuit_test.jpg', (50, 320)) 
        


        self.hide_all_tabs() 



    def init_tabs(self):
        self.create_button('Transformer Properties', (25, 25, 200, 40), self.init_transformer_probability_tab)
        self.create_button('Effeciency', (350, 25, 100, 40), self.init_efficiency_tab)
        self.create_button('Short-Circuit Test', (460, 25, 200, 40), self.init_short_circuit_tab) 
        

    def init_transformer_probability_tab(self) :
        self.hide_all_tabs()
        for key, value in self.transformer_probabilities_widgets.items() :
            value.setVisible(True) 
    
    def init_short_circuit_tab(self):
        self.hide_all_tabs() 
        for key, value in self.short_circuit_widgets.items():
            value.setVisible(True)

    def init_efficiency_tab(self):
        self.hide_all_tabs() 
        for key, value in self.efficiency_widgets.items():
            value.setVisible(True) 
        

    def init_main_tab(self):
        self.hide_all_tabs()
        for key, value in self.main_tab_widgets.items():
            value.setVisible(True) 
        


    def hide_all_tabs(self):
        for key, value in self.transformer_probabilities_widgets.items() :
            value.setVisible(False) 
        for key, value in self.efficiency_widgets.items():
            value.setVisible(False) 
        for key, value in self.short_circuit_widgets.items():
            value.setVisible(False) 
        for key, value in self.main_tab_widgets.items():
            value.setVisible(False) 


    def calculate_iron_losses(self):
        frequency = int(self.transformer_probabilities_widgets['frequency_edit'].text())
        lamination_thickness = float(self.transformer_probabilities_widgets['lamination_thickness_edit'].text()) 
        volume = float(self.transformer_probabilities_widgets['volume_edit'].text()) 
        N1 = int(self.transformer_probabilities_widgets['N1_edit'].text())
        N2 = int(self.transformer_probabilities_widgets['N2_edit'].text())
        
        self.transformer = Transformer(self.core_material) 
        self.transformer.set_value('frequency', frequency) 
        self.transformer.set_value('volume', volume)
        self.transformer.set_value('lamination_thickness', lamination_thickness) 
        self.transformer.set_value('N1', N1) 
        self.transformer.set_value('N2', N2) 

        hysterisis_loss = self.transformer.get_hysterisis_loss() 
        eddy_loss = self.transformer.get_eddy_loss() 
        total_loss = hysterisis_loss + eddy_loss 
        hysterisis_loss = '{:10.3f}'.format(hysterisis_loss) 
        eddy_loss = '{:10.3f}'.format(eddy_loss) 
        total_loss = '{:10.3f}'.format(total_loss) 

        self.transformer_probabilities_widgets['hysterisis_loss_result_edit'].setText(hysterisis_loss + ' W') 
        self.transformer_probabilities_widgets['eddy_loss_result_edit'].setText(eddy_loss + ' W') 
        self.transformer_probabilities_widgets['core_loss_result_edit'].setText(total_loss + ' W') 

        print("total_loss:", total_loss) 

    def material_choice(self, choice) :
        print("chose:", choice) 
        self.core_material = choice 

    def record_measurements(self):
        voltage = float(self.short_circuit_widgets['source_voltage_edit'].text()) 
        p, i = self.transformer.get_short_circuit_test(voltage) 
        p = '{:10.3f}'.format(p) 
        i = '{:10.3f}'.format(i) 
        R_eq = self.transformer.values['R_eq']
        R_eq = '{:10.3f}'.format(R_eq) 
        
        self.short_circuit_widgets['power_edit'].setText(p + " W")
        self.short_circuit_widgets['current_edit'].setText(i + " A")
        self.short_circuit_widgets['R_eq_edit'].setText(R_eq + " ohm")

    def calculate_efficiency(self):
        v1 = self.efficiency_widgets['V1_edit'].text()
        load = self.efficiency_widgets['Load_edit'].text() 
        if ':' in v1 or ':' in load : return 

        _, efficiency, _ = self.transformer.get_efficiency(v1, load)      
        efficiency = '{:.1f}'.format(efficiency)    
        self.efficiency_widgets['efficiency_edit'].setText(str(efficiency ) + ' %')

    def plot(self):
        v1 = self.efficiency_widgets['V1_edit'].text()
        load = self.efficiency_widgets['Load_edit'].text() 
        if ':' not in v1 and ':' not in load : return 
        else : self.efficiency_widgets['efficiency_edit'].setText('')
    
        output_va, efficiency, pf = self.transformer.get_efficiency(v1, load) 
        pf = '{:.2f}'.format(pf) 

        self.plots.append((output_va, efficiency, pf))
        
        self.graph = pg.PlotWidget() 
        self.graph.setTitle('Load vs Efficiency')
        self.graph.setLabel('left', 'Efficiency (%)', color='red', size=30)
        self.graph.setLabel('bottom', 'Load (VA)', color='red', size=30)
        self.graph.setBackground('w')

        colors = [(255,0,0), (255,255,0), (0,255,0), (0,0,255),(0,255,255), (255,0,255)]
        for i, plott in enumerate(self.plots) :
            x, y, pf = plott 
            pen = pg.mkPen(color=colors[i%len(colors)] , name= pf+' p.f.', width=3, style=QtCore.Qt.DashLine)
            self.graph.plot(x, y, pen=pen)   
            self.graph.addLegend() 
            self.graph.setVisible(True) 


    def clear_plots(self):
        self.plots = [] 

    def undo_plot(self):
        if len(self.plots) : self.plots.pop()

    

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
 
        painter.drawRect(20, 20, 650,50)

    def create_button(self, name, coords, on_clicked = None):
        push_button = QPushButton(name, self) 
        push_button.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))
        if on_clicked : push_button.clicked.connect(on_clicked)  
        return push_button 

    def create_label(self, name, coords, font = None ):
        label = QLabel(name, self) 
        label.setGeometry(QtCore.QRect(coords[0], coords[1], coords[2], coords[3]))  
        if font : 
            if isinstance(font, int) and font == 25: label.setFont(QtGui.QFont("Times", 25, QtGui.QFont.Bold) )
            else :label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold) )
        label.adjustSize() 
        label.setMinimumSize(QtCore.QSize(60, 0))
        return label 

    def create_image(self, image_name, coords, resize = None):
        image = QPixmap(image_name)
        if resize : image = image.scaledToWidth(150) 
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

    def create_graph(self):
        return pg.PlotWidget() 














if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = Window() 
    sys.exit(app.exec_()) 