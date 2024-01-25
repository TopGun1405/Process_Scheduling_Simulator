import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

from simulator import Simulator


class SimulatorView(QMainWindow):
    def __init__(self):
        super().__init__()

        newSimulator = Simulator()

        mainLayout = QVBoxLayout()
        centralWidget = QWidget()

        pane = QHBoxLayout()

        self.setWindowTitle("Process Scheduling Simulator")
        self.show()

    def changeConfig(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimulatorView()
    sys.exit(app.exec())
