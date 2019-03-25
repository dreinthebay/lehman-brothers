#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox)


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        #self.createBottomLeftTabWidget()
        #self.createBottomRightGroupBox()
        self.createBottomGroupBox()
        self.createProgressBar()

        styleComboBox.activated[str].connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        #disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        #mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        mainLayout.addWidget(self.bottomGroupBox, 4, 0, 1, 2)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")
        self.changeStyle('Windows')
        

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def createBottomGroupBox(self):
        self.bottomGroupBox = QGroupBox('Everyday')
        label_intro = QLabel('Here are the things you need to do everyday:')
        prepare = QLabel('prepare to be productive')
        to_do = QLabel('write your to-do list the night before')
        sleep = QLabel('get a good night sleep')
        early = QLabel('get up early')
        read = QLabel('read')
        exercise = QLabel('exercise')
        eat = QLabel('have breakfast')
        worst_first = QLabel('start with the worst job')
        consistent = QLabel('be consistent')
        layout = QVBoxLayout()
        layout.addWidget(label_intro)
        layout.addWidget(to_do)
        layout.addWidget(sleep)
        layout.addWidget(early)
        layout.addWidget(read)
        layout.addWidget(exercise)
        layout.addWidget(eat)
        layout.addWidget(worst_first)
        layout.addWidget(consistent)
        self.bottomGroupBox.setLayout(layout)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Data Collection")

        label_intro = QLabel('Welcome to the ISS Tracker Program')
        label_data_file = QLabel('Please enter the name of the data file to write to:')
        self.data_csv_name_line = QLineEdit('data.csv')
        print(self.data_csv_name_line.text())
        #label_data_file.setBuddy(data_csv_name)

        label_steps = QLabel('Please enter the number of 5 second steps to run:')

        self.step_count = QSpinBox(self.topLeftGroupBox)
        self.step_count.setValue(1)
        #self.step_count.valueChanged.connect(self.value_change)
        

        run_data_collection_button = QPushButton('Collect Data')
        run_data_collection_button.clicked.connect(self.run_data)


        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(label_intro)
        layout.addWidget(label_data_file)
        layout.addWidget(self.data_csv_name_line)
        layout.addWidget(label_steps)
        layout.addWidget(self.step_count)
        layout.addWidget(run_data_collection_button)
        #layout.addWidget(radioButton1)
        #layout.addWidget(radioButton2)
        #layout.addWidget(radioButton3)
        #layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Mapping")
        label_intro = QLabel('Mapping time')

        label_map_file = QLabel('Enter the file name for the map')
        self.map_file_name = QLineEdit('map')

        run_map_maker = QPushButton('Run Mapper')
        open_map_button = QPushButton('Open Map')
        open_map_button.clicked.connect(self.open_map)


        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(label_intro)
        layout.addWidget(label_map_file)
        layout.addWidget(self.map_file_name)
        layout.addWidget(run_map_maker)
        layout.addWidget(open_map_button)
        #layout.addWidget(defaultPushButton)
        #layout.addWidget(togglePushButton)
        #layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    
    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)

    def run_data(self):
        self.run_data_collection('this is a test')

    def run_data_collection(self, meep): #csv_file_name, steps):
        import os
        import sys
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(os.path.dirname(path))
        sys.path.append(dir_path)
        
        alert = QMessageBox()
        meep = dir_path
        alert.setText('You clicked the Top button! {}'.format(meep))
        alert.exec_()
        file_path = os.path.join(dir_path,'ISS_Tracker','ISS_location_grabber')
        print(file_path)
        print(os.getcwd())
        from ISS_Tracker.ISS_location_grabber.iss_location_grabber import ISS_Tracker
        t = ISS_Tracker(self.data_csv_name_line.text())
        t.collect_5_second_interval_data(self.step_count.value())

    def open_map(self):
        import os
        import sys
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(os.path.dirname(path))
        sys.path.append(dir_path)
        file_path = os.path.join(dir_path,'ISS_Tracker','ISS_location_grabber')
        print(file_path)
        from ISS_Tracker.ISS_map_maker.ISS_map_maker import Mapper

        mapper = Mapper(self.data_csv_name_line.text(), self.map_file_name.text())
        mapper.map_points()
        print('opening map...')
        mapper.open_map()

    
    #def value_change(self):
    #    self.steps = self.step_count.value()
    #def update_file_name(self):
    #    self.data_csv_name ='hi' 


     



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 
