from PyQt5.QtWidgets import * # QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton

# makes the app
app = QApplication([])

# sets the style
app.setStyle('Windows') #The available styles depend on your platform but are usually 'Fusion', 'Windows', 'WindowsVista' (Windows only) and 'Macintosh' (Mac only).

# creates a palatte and sets the app
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)

window = QWidget()
layout = QVBoxLayout()
label = QLabel('Sup World')
layout.addWidget(label)
Top = QPushButton('Top')
def on_Top_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the Top button!')
    alert.exec_()

Top.clicked.connect(on_Top_button_clicked)
layout.addWidget(Top)
layout.addWidget(QPushButton('Middle'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()