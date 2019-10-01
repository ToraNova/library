# Example PyQt5 GUI Program
# Thanks to https://build-system.fman.io/pyqt5-tutorial

# Standard Imports
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QApplication, QLabel,\
                            QWidget, QPushButton, QVBoxLayout
# All Qt app must have one instance of this
app = QApplication([])

# theme define
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)

# callback for exit buttons
def exit_gui_prog():
    exit(0)

# create label
label1 = QLabel('Hello World')
label2 = QLabel('by ToraNova')
exit_button = QPushButton('Exit')
exit_button.clicked.connect( exit_gui_prog )

# create a widget
window = QWidget()
# layout define
layout = QVBoxLayout()
# populate layout
layout.addWidget( label1 )
layout.addWidget( label2 )
layout.addWidget( exit_button )
# set layout
window.setLayout( layout )
window.setWindowTitle('PYQT')

# display window
# window.show()
window.showFullScreen()

app.setPalette( dark_palette ) #dark theme, comment to disable
app.setStyle('Fusion')
app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

# hand over control
app.exec_()

