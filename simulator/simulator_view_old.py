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
        processName_LineEdit.clearFocus()
        processName_LineEdit.deselect()
        processName_LineEdit.setPlaceholderText("process name")

        processorName_LineEdit = QLineEdit()
        processorName_LineEdit.close()
        processorName_LineEdit.setPlaceholderText("processor name")

        timeQuantum_LineEdit = QLineEdit()
        timeQuantum_LineEdit.setPlaceholderText("timeQuantum")

        pane.addWidget(processName_LineEdit)
        pane.addWidget(processorName_LineEdit)
        pane.addWidget(timeQuantum_LineEdit)

        mainLayout.addLayout(pane)
        centralWidget.setLayout(mainLayout)

        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Process Scheduling Simulator")
        self.show()

    def changeConfig(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OldSimulatorView()
    sys.exit(app.exec())
