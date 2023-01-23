import random
import sys
import string
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
                             QPushButton, QWidget, QMessageBox, QSpinBox)

__name__ = '__main__'


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.numbers_checkbox = None
        self.copy_password_button = None
        self.special_characters_checkbox = None
        self.generate_password_button = None
        self.length_spin_box = None
        self.uppercase_checkbox = None
        self.length_label = None
        self.password_line_edit = None
        self.password_label = None
        self.password = ""
        self.use_uppercase = False
        self.use_numbers = False
        self.use_special_characters = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Generator")

        self.password_label = QLabel("Password:", self)
        self.password_label.move(20, 20)

        self.password_line_edit = QLineEdit(self)
        self.password_line_edit.move(80, 20)
        self.password_line_edit.setReadOnly(True)

        self.length_label = QLabel("Length:", self)
        self.length_label.move(20, 50)

        self.length_spin_box = QSpinBox(self)
        self.length_spin_box.move(80, 50)
        self.length_spin_box.setMinimum(8)
        self.length_spin_box.setMaximum(32)
        self.length_spin_box.setValue(16)

        self.uppercase_checkbox = QCheckBox("Use Uppercase Letters", self)
        self.uppercase_checkbox.move(20, 80)
        self.uppercase_checkbox.stateChanged.connect(self.use_uppercase_changed)

        self.numbers_checkbox = QCheckBox("Use Numbers", self)
        self.numbers_checkbox.move(20, 110)
        self.numbers_checkbox.stateChanged.connect(self.use_numbers_changed)

        self.special_characters_checkbox = QCheckBox("Use Special Characters", self)
        self.special_characters_checkbox.move(20, 140)
        self.special_characters_checkbox.stateChanged.connect(self.use_special_characters_changed)

        self.generate_password_button = QPushButton("Generate Password", self)
        self.generate_password_button.move(20, 170)
        self.generate_password_button.clicked.connect(self.generate_password)

        self.copy_password_button = QPushButton("Copy to clipboard", self)
        self.copy_password_button.move(20, 200)
        self.copy_password_button.clicked.connect(self.copy_password)

        self.setGeometry(300, 300, 300, 250)
        self.show()

        self.length_spin_box.valueChanged.connect(self.generate_password)
        self.generate_password()

    def generate_password(self):
        possible_characters = string.ascii_lowercase
        if self.use_uppercase:
            possible_characters += string.ascii_uppercase
        if self.use_numbers:
            possible_characters += string.digits
        if self.use_special_characters:
            possible_characters += "!@#$%^&*()_+-=[]{};:,.<>/?\""
        self.password = ''.join(random.choice(possible_characters) for _ in range(self.length_spin_box.value()))
        self.password_line_edit.setText(self.password)

    def use_uppercase_changed(self, state):
        self.use_uppercase = state == Qt.Checked

    def use_numbers_changed(self, state):
        self.use_numbers = state == Qt.Checked

    def use_special_characters_changed(self, state):
        self.use_special_characters = state == Qt.Checked

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password)
        QMessageBox.information(self, "Password Copied", "The password has been copied to your clipboard.")


if __name__ == '__main__':
    app = QApplication([])
password_generator = PasswordGenerator()
sys.exit(app.exec_())
