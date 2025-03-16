import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        self.expression += char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except ZeroDivisionError:
            self.expression = ""
            return "Error: Division by zero"
        except Exception:
            self.expression = ""
            return "Error"

    def get_expression(self):
        return self.expression


class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.calculator = Calculator()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.input = QLineEdit(self)
        layout.addWidget(self.input)

        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            grid_layout.addWidget(button, row, col)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self, char):
        if char == '=':
            result = self.calculator.calculate()
            self.input.setText(str(result))
        elif char == 'C':
            self.calculator.clear_expression()
            self.input.setText("")
        else:
            self.calculator.add_to_expression(char)
            self.input.setText(self.calculator.get_expression())


