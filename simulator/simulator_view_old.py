import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

from simulator import Simulator


class OldSimulatorView(QWidget):
    def __init__(self):
        super().__init__()

        newSimulator = Simulator()

        self.setWindowTitle("Process Scheduling Simulator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OldSimulatorView()
    sys.exit(app.exec())
