from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import os
from ui import*
from PIL import Image
from PyQt5.QtGui import QPixmap

app=QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ShowFileNameList)

    def Filter(self, files, extensions):
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result 
    
    def ChoosenWorkdir(self):
        global workdir 
        workdir=QFileDialog.getExistingDirectory()
    
    def ShowFileNameList(self):
        extensions=['.png','.jpg','.jpeg','.bmp','.gif']
        self.ChoosenWorkdir()
        self.filenames=self.Filter(os.listdir(workdir),extensions)
        for filename in self.filenames:
            self.ui.listWidget.addItem(filename)
    
    
ex=MainWindow()
ex.show()
app.exec_()