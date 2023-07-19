from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QDir
import os

class Ui:
    def __init__(self):
        self.app = QApplication([])

    def test(self):
        print("Test")

    def startWindow(self):
        self.window = QWidget()

        self.layout = QFormLayout()
        self.width = QLineEdit('500')
        self.height = QLineEdit('200')
        self.btnExit = QPushButton('Record Image')
        self.btnExit.clicked.connect(self.app.quit)

        self.layout.addRow('Width', self.width)
        self.layout.addRow('Height', self.height)
        self.layout.addRow(self.btnExit)

        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()

        return int(self.width.text()), int(self.height.text())

    def recordWindow(self):
        self.window = QWidget()

        self.layout = QGridLayout()
        self.progressBar = QProgressBar()
        self.label = QLabel("Progress")

        self.layout.addWidget(self.label, 0, 1)
        self.layout.addWidget(self.progressBar, 1, 0, 1, 3)

        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()
        
    def showImage(self, width, height, values):
        self.window = QWidget()

        self.layout = QGridLayout()
        self.image = QPixmap(width, height)

        # Convert grayscale values to bytes
        bytes_data = bytes(values)

        # Create a QImage from the grayscale values
        image = QImage(bytes_data, width, height, QImage.Format.Format_Grayscale8)

        self.image.convertFromImage(image)
        self.label = QLabel()
        self.label.setPixmap(self.image)

        self.layout.addWidget(self.label, 0, 0)

        # Add a "Save Image" button
        self.btnSave = QPushButton("Save Image")
        self.btnSave.clicked.connect(self.saveImage)
        self.layout.addWidget(self.btnSave, 1, 0)

        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()
        
    def saveImage(self):
        # Get the path of the current Python file
        current_path = os.path.dirname(os.path.abspath(__file__))

        # Set a default save path relative to the current file location
        default_path = os.path.join(current_path, "save.jpg")


        # Open a file dialog with the default save path selected
        file_dialog = QFileDialog()
        save_path, _ = file_dialog.getSaveFileName(None, "Save Image", default_path, "JPEG Files (*.jpg);;PNG Files (*.png)")

        # Save the image if a save path is selected
        if save_path:
            self.image.save(save_path)

if __name__ == "__main__":
    ui = Ui()
    ui.startWindow()