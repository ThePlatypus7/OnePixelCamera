from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QImage, QColor
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
        
    def showImage(self, width, height, red_values, green_values, blue_values):
        self.window = QWidget()

        self.layout = QGridLayout()
        self.image = QImage(width, height, QImage.Format.Format_RGB888)

        # Combine red, green, and blue channels to create a colored image
        for y in range(height):
            for x in range(width):
                color = QColor(red_values[y * width + x], green_values[y * width + x], blue_values[y * width + x])
                self.image.setPixelColor(x, y, color)

        self.label = QLabel()
        self.label.setPixmap(QPixmap.fromImage(self.image))

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