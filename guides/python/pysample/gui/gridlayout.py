# Example PyQt5 GUI Program on GRID LAYOUT

# Standard Imports
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget,\
                            QLabel, QPushButton,\
                            QVBoxLayout, QGridLayout
# All Qt app must have one instance of this
app = QApplication([])

# fonts
large_font = QFont("Arial", 20, QFont.Bold)

# callback for exit buttons
def exit_gui_prog():
    exit(0)

# create label
label1 = QLabel('Hello World')
label1.setFont(large_font)
label2 = QLabel('by ToraNova')
label2.setFont(QFont("Arila", 12, QFont.Light, True))
exit_button = QPushButton('Exit')
exit_button.clicked.connect( exit_gui_prog )

# create a widget
window = QWidget()
# layout define
layout = QGridLayout()
# populate layout
# Hello World spans across 4 rows and 1 col
layout.addWidget( label1, 0, 0, 3, 1)
# the rest just normal, on col 2
layout.addWidget( label2, 0, 1 )
layout.addWidget( exit_button, 1, 1 )
# set stretch
layout.setColumnStretch( 0, 20 ) # col 0 is 20 rel size
layout.setColumnStretch( 1, 10 ) # col 1 is 10 rel size

# set layout
window.setLayout( layout )

# display window
window.setGeometry(100,100,200,100)
window.setWindowTitle('GridLayout')
window.show()
app.setStyle('Fusion')

# hand over control
app.exec_()

