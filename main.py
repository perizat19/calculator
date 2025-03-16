from PyQt6.QtWidgets import QApplication
import sys
from calculator import CalculatorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    app.exec()



