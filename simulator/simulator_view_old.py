import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

from simulator import Simulator


class OldSimulatorView(QMainWindow):
    def __init__(self):
        super().__init__()

        newSimulator = Simulator()

        mainLayout = QVBoxLayout()
        centralWidget = QWidget()

        pane = QHBoxLayout()
        processName_LineEdit = QLineEdit()
        processorName_LineEdit = QLineEdit()
        timeQuantum_LineEdit = QLineEdit()
        
        pane.addWidget(processName_LineEdit)

        mainLayout.addLayout(pane)
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

        self.setWindowTitle("Process Scheduling Simulator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OldSimulatorView()
    sys.exit(app.exec())
