#use source ./bin/activate to enable venv

#test video link: https://www.youtube.com/watch?v=C0DPdy98e4c


# from YoutubeDownload import *

# link = input("Enter the YouTube video URL: ")
# Download(link)
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox, QLabel, QHBoxLayout, QLineEdit
from SupportedFileTypes import *
from VideoConversion import Convert

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Converter")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()

        # -----FromBox-----------
        self.label = QLabel('From')
        layout.addWidget(self.label)


        fromBox = self.create_from_box()
        layout.addLayout(fromBox)


        #---------To Box--------------
        self.label = QLabel('To')
        layout.addWidget(self.label)


        toBox = self.create_to_box()
        layout.addLayout(toBox)

        ToBox = QHBoxLayout()

         # Add Convert Button
        self.convertButton = QPushButton("Convert")
        self.convertButton.clicked.connect(self.convert_file)
        layout.addWidget(self.convertButton)        

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_from_box(self):
        fromBox = QHBoxLayout()

        # Button to open file dialog
        self.FromFileButton = QPushButton("Select File")
        self.FromFileButton.clicked.connect(self.open_file_dialog)
        self.FromFileButton.setFixedSize(64, 64)
        fromBox.addWidget(self.FromFileButton)

        #Textbox for file path selection
        self.fromFilePath = QLineEdit()
        fromBox.addWidget(self.fromFilePath)

        return fromBox
    
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

        #dropdown of available conversion types
        self.dropdown = QComboBox()
        self.dropdown.addItems(SupportedFileTypes)
        toBox.addWidget(self.dropdown)

        

        return toBox

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;Python Files (*.py)", options=options)
        if file_name:
            print("Selected file:", file_name)
            # Set the file path to the respective QLineEdit
            sender = self.sender()
            if sender == self.FromFileButton:
                self.fromFilePath.setText(file_name)
                self.toFilePath.setText(file_name)
            elif sender == self.ToFileButton:
                self.toFilePath.setText(file_name)
    
    def convert_file(self):
        input_file = self.fromFilePath.text()
        output_file = self.toFilePath.text()
        Convert(input_file, output_file)
        print(f"Converted {input_file} to {output_file} as {conversion_type}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())