import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow


class SimulatorView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Process Scheduling Simulator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimulatorView()
    sys.exit(app.exec())
