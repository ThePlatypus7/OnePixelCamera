from PyQt6.QtWidgets import *

class ui:
    def test(self):
        print("Test")
        
    def startWindow(self):
        self.app = QApplication([])
        self.window = QWidget()
        
        self.layout = QFormLayout()
        self.width = QLineEdit('500')
        self.height = QLineEdit('200')
        self.btnExit = QPushButton('Exit')
        self.btnExit.clicked.connect(self.app.quit)
        
        self.layout.addRow('Width', self.width)
        self.layout.addRow('Height', self.height)
        self.layout.addRow(self.btnExit)
        
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec()
        
        return int(self.width.text()), int(self.height.text())