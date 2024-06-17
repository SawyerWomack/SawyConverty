#use source ./bin/activate to enable venv

#test video link: https://www.youtube.com/watch?v=C0DPdy98e4c


# from YoutubeDownload import *

# link = input("Enter the YouTube video URL: ")
# Download(link)
import sys
from SupportedFileTypes import *
from VideoConversion import Convert
from YoutubeDownload import Download
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QComboBox, QLabel, QHBoxLayout, QLineEdit, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Converter")
        self.setGeometry(100, 100, 400, 300)
        
        # Create a tab widget
        self.tabs = QTabWidget()
        
        #--------- File Conversion Tab------------------
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "File Converter")
        
        
        
        # Set up the layout for the first tab
        self.tab1_layout = QVBoxLayout()
        self.tab1.setLayout(self.tab1_layout)
        
        # -----FromBox-----------
        self.label = QLabel('From')
        self.tab1_layout.addWidget(self.label)

        fromBox = self.create_from_box()
        self.tab1_layout.addLayout(fromBox)

        #---------To Box--------------
        self.label = QLabel('To')
        self.tab1_layout.addWidget(self.label)

        toBox = self.create_to_box()
        self.tab1_layout.addLayout(toBox)

        # Add Convert Button
        self.convertButton = QPushButton("Convert")
        self.convertButton.clicked.connect(self.convert_file)
        self.tab1_layout.addWidget(self.convertButton)
        

        #------- Youtube Download Tab-----------

        #create the tab
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Youtube Download")



        # Set up the layout for the second tab
        self.tab2_layout = QVBoxLayout()
        self.tab2.setLayout(self.tab2_layout)
        
        # Add widgets to the second tab as needed

        

        
        #add a link input box
        self.linkLabel = QLabel("Type link of video to download:")
        self.tab2_layout.addWidget(self.linkLabel)

        self.linkInput = QLineEdit()
        self.tab2_layout.addWidget(self.linkInput)

        #add a download location input
        self.downloadLabel = QLabel("Where should the file download to:")
        self.tab2_layout.addWidget(self.downloadLabel)

        self.downloadLocation = QLineEdit()
        self.tab2_layout.addWidget(self.downloadLocation)


        # Add a download button to the second tab
        self.downloadButton = QPushButton("Download")
        self.downloadButton.clicked.connect(self.download_video)
        self.tab2_layout.addWidget(self.downloadButton)
        



        #--------Central widget-----------
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.tabs)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def create_from_box(self):
        fromBox = QHBoxLayout()

        # Button to open file dialog
        self.FromFileButton = QPushButton("Select File")
        self.FromFileButton.clicked.connect(self.open_file_dialog)
        self.FromFileButton.setFixedSize(64, 64)
        fromBox.addWidget(self.FromFileButton)

        # Textbox for file path selection
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
    
    def download_video(self):
        link = self.linkInput.text()
        Download(link)



# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())