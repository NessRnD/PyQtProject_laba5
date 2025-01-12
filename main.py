import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit, QLabel, QLineEdit, QMessageBox
import random

class MyArray:
    def __init__(self, array=None):
        if array is None:
            self.array = []
        else:
            self.array = array

    def manual_fill(self, array):
        self.array = array

    def auto_fill(self, rows, cols, min_val, max_val):
        self.array = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    def __len__(self):
        return len(self.array)

    def show(self, separator=' '):
        return '\n'.join([separator.join(f"{elem:.0f}" if elem.is_integer() else f"{elem:.1f}" for elem in row) for row in self.array])

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem + other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Arrays must have the same dimensions for addition")
            return MyArray([[self.array[i][j] + other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem - other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Arrays must have the same dimensions for subtraction")
            return MyArray([[self.array[i][j] - other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem * other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Arrays must have the same dimensions for multiplication")
            return MyArray([[self.array[i][j] * other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem / other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Arrays must have the same dimensions for division")
            return MyArray([[self.array[i][j] / other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return MyArray([[elem > other for elem in row] for row in self.array])
        elif isinstance(other, MyArray):
            if len(self.array) != len(other.array) or len(self.array[0]) != len(other.array[0]):
                raise ValueError("Arrays must have the same dimensions for comparison")
            return MyArray([[self.array[i][j] > other.array[i][j] for j in range(len(self.array[i]))] for i in range(len(self.array))])
        else:
            raise TypeError("Unsupported operand type")

    def sort_even(self):
        self.array = [sorted([elem for elem in row if elem % 2 == 0]) for row in self.array]

    def add_element_to_start(self, element):
        self.array.insert(0, element)

    def remove_element_from_start(self):
        if self.array:
            self.array.pop(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.array = MyArray()

        self.setWindowTitle("MyArray Application")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Manual Fill Section
        self.input_label = QLabel("Enter array elements (comma separated, rows separated by semicolon):")
        self.input_field = QLineEdit(self)
        self.fill_button = QPushButton("Manual Fill", self)
        self.fill_button.clicked.connect(self.manual_fill)

        # Auto Fill Section
        auto_fill_layout = QHBoxLayout()

        self.rows_label = QLabel("Rows:")
        self.rows_input = QLineEdit(self)

        self.cols_label = QLabel("Columns:")
        self.cols_input = QLineEdit(self)

        self.min_val_label = QLabel("Min Value:")
        self.min_val_input = QLineEdit(self)

        self.max_val_label = QLabel("Max Value:")
        self.max_val_input = QLineEdit(self)

        auto_fill_layout.addWidget(self.rows_label)
        auto_fill_layout.addWidget(self.rows_input)
        auto_fill_layout.addWidget(self.cols_label)
        auto_fill_layout.addWidget(self.cols_input)
        auto_fill_layout.addWidget(self.min_val_label)
        auto_fill_layout.addWidget(self.min_val_input)
        auto_fill_layout.addWidget(self.max_val_label)
        auto_fill_layout.addWidget(self.max_val_input)

        self.auto_fill_button = QPushButton("Auto Fill", self)
        self.auto_fill_button.clicked.connect(self.auto_fill)

        # Show Array Section
        self.show_button = QPushButton("Show Array", self)
        self.show_button.clicked.connect(self.show_array)

        # Add Element to Start Section
        self.add_element_label = QLabel("Element to add at start:")
        self.add_element_input = QLineEdit(self)
        self.add_element_button = QPushButton("Add Element to Start", self)
        self.add_element_button.clicked.connect(self.add_element_to_start)

        # Remove Element from Start Section
        self.remove_element_button = QPushButton("Remove Element from Start", self)
        self.remove_element_button.clicked.connect(self.remove_element_from_start)

        # Sort Even Elements Section
        self.sort_even_button = QPushButton("Sort Even Elements", self)
        self.sort_even_button.clicked.connect(self.sort_even)

        # Arithmetic Operations Section
        self.arithmetic_label = QLabel("Arithmetic Operation (value or array):")
        self.arithmetic_input = QLineEdit(self)
        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.add_operation)
        self.sub_button = QPushButton("Subtract", self)
        self.sub_button.clicked.connect(self.sub_operation)
        self.mul_button = QPushButton("Multiply", self)
        self.mul_button.clicked.connect(self.mul_operation)
        self.div_button = QPushButton("Divide", self)
        self.div_button.clicked.connect(self.div_operation)

        # Output Field
        self.output_field = QTextEdit(self)
        self.output_field.setReadOnly(True)

        # Adding widgets to layout
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.fill_button)
        layout.addLayout(auto_fill_layout)
        layout.addWidget(self.auto_fill_button)
        layout.addWidget(self.show_button)
        layout.addWidget(self.add_element_label)
        layout.addWidget(self.add_element_input)
        layout.addWidget(self.add_element_button)
        layout.addWidget(self.remove_element_button)
        layout.addWidget(self.sort_even_button)
        layout.addWidget(self.arithmetic_label)
        layout.addWidget(self.arithmetic_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.sub_button)
        layout.addWidget(self.mul_button)
        layout.addWidget(self.div_button)
        layout.addWidget(self.output_field)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Manual Fill Function
    def manual_fill(self):
        try:
            input_text = self.input_field.text()
            rows = input_text.split(';')
            array = [list(map(int, row.split(','))) for row in rows]
            self.array.manual_fill(array)
            self.output_field.append("Array manually filled.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid integers separated by commas and rows separated by semicolons.")

    # Auto Fill Function
    def auto_fill(self):
        rows = self.rows_input.text()
        cols = self.cols_input.text()
        min_val = self.min_val_input.text()
        max_val = self.max_val_input.text()

        if not rows or not cols or not min_val or not max_val:
            QMessageBox.warning(self, "Error", "All fields are required for Auto Fill.")
            return

        try:
            rows = int(rows)
            cols = int(cols)
            min_val = int(min_val)
            max_val = int(max_val)

            self.array.auto_fill(rows, cols, min_val, max_val)
            self.output_field.append("Array auto filled.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid integers for Rows, Columns, Min Value, and Max Value.")

    # Show Array Function
    def show_array(self):
        self.output_field.append(self.array.show())

    # Add Element to Start Function
    def add_element_to_start(self):
        element = self.add_element_input.text()
        if not element:
            QMessageBox.warning(self, "Error", "Please enter a valid element.")
            return

        try:
            element = int(element)
            self.array.add_element_to_start(element)
            self.output_field.append("Element added to start.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid integer.")

    # Remove Element from Start Function
    def remove_element_from_start(self):
        self.array.remove_element_from_start()
        self.output_field.append("Element removed from start.")

    # Sort Even Elements Function
    def sort_even(self):
        self.array.sort_even()
        self.output_field.append("Even elements sorted.")

    # Add Operation Function
    def add_operation(self):
        value = self.arithmetic_input.text()
        if not value:
            QMessageBox.warning(self, "Error", "Please enter a valid value.")
            return

        try:
            if ';' in value:
                rows = value.split(';')
                array = [list(map(int, row.split(','))) for row in rows]
                second_array = MyArray(array)
                self.array = self.array + second_array
                self.output_field.append("Array after addition of second array.")
            else:
                value = int(value)
                self.array = self.array + value
                self.output_field.append("Array after addition operation.")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    # Subtract Operation Function
    def sub_operation(self):
        value = self.arithmetic_input.text()
        if not value:
            QMessageBox.warning(self, "Error", "Please enter a valid value.")
            return

        try:
            if ';' in value:
                rows = value.split(';')
                array = [list(map(int, row.split(','))) for row in rows]
                second_array = MyArray(array)
                self.array = self.array - second_array
                self.output_field.append("Array after subtraction of second array.")
            else:
                value = int(value)
                self.array = self.array - value
                self.output_field.append("Array after subtraction operation.")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    # Multiply Operation Function
    def mul_operation(self):
        value = self.arithmetic_input.text()
        if not value:
            QMessageBox.warning(self, "Error", "Please enter a valid value.")
            return

        try:
            if ';' in value:
                rows = value.split(';')
                array = [list(map(int, row.split(','))) for row in rows]
                second_array = MyArray(array)
                self.array = self.array * second_array
                self.output_field.append("Array after multiplication of second array.")
            else:
                value = int(value)
                self.array = self.array * value
                self.output_field.append("Array after multiplication operation.")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    # Divide Operation Function
    def div_operation(self):
        value = self.arithmetic_input.text()
        if not value:
            QMessageBox.warning(self, "Error", "Please enter a valid value.")
            return

        try:
            if ';' in value:
                rows = value.split(';')
                array = [list(map(int, row.split(','))) for row in rows]
                second_array = MyArray(array)
                self.array = self.array / second_array
                self.output_field.append("Array after division of second array.")
            else:
                value = int(value)
                self.array = self.array / value
                self.output_field.append("Array after division operation.")
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
