#import the modules that i need
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QLineEdit, QMessageBox

def create_to_box(self):
    toBox = QHBoxLayout()
    # Button to open file dialog
    self.ToFileButton = QPushButton("Select File")
    self.ToFileButton.clicked.connect(self.open_file_dialog)
    self.ToFileButton.setFixedSize(64, 64)
    toBox.addWidget(self.ToFileButton)

    # Textbox to display selected file path
    self.toFilePath = QLineEdit()
    toBox.addWidget(self.toFilePath)

    return toBox
def ErrorMessage(text, parent=None):
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    return msg.exec_()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # Create and show your main window or widget here
    # For example:
    # main_window = QMainWindow()
    # main_window.show()
    sys.exit(app.exec_())