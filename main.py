from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPixmap,  Qt.KeepAspectRatio, QInputDialog, QWidget, QFileDialog,  QLineEdit, QListWidget,QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QTextEdit
import os 
app = QApplication([])


'''Интерфейс приложения'''
main_win = QWidget()
workdir = QFileDialog.getExitstingDirectory()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700, 400)

list_noted = QListWidget()
list_noted_label = QPushButton('Папка')
field_text = QLabel('Картинка')
button_noted_lev = QPushButton('Лево')
button_noted_right = QPushButton('Право')
button_noted_sharpness = QPushButton('Зеркало')
button_noted_flip = QPushButton('Резкость')
button_noted_gray = QPushButton('Ч/Б')
col_1 = QVBoxLayout()
col_1.addWidget(list_noted_label)
col_1.addWidget(list_noted)
row_1 = QHBoxLayout()
col_2 = QVBoxLayout()
row_1.addWidget(button_noted_lev)
row_1.addWidget(button_noted_right)
row_1.addWidget(button_noted_sharpness)
row_1.addWidget(button_noted_flip)
row_1.addWidget(button_noted_gray)
row_2 = QHBoxLayout()
col_2.addWidget(field_text)
col_2.addLayout(row_1)
row_2.addLayout(col_1)
row_2.addLayout(col_2)

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExitstingDirectory()
def filter(files, extensions):
    result = []
    for file_name in files:
        for extension in extensions:
            if file_name.endwith(extension):
                result.append(file_name)
    return result
def showFilenameList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    files = os.listdir(workdir)
    file_names = filter(files, extensions)
    lw_files.clear()
    for file_name in file_names:
        iw_files.addItems(file_name)


class ImageProcessor():
    def __init__(self):
        self.image = None 
        self.dir = None
        self.file_name = None
        self.save = 'save/'
    def loadImage(self, file_name):
        self.file_name = file_name
        image_path = os.path.join(workdir, file_name)
        self.image = Image.open(image_path)
    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
    def do_bw(self):
        self.image = self.image_conver('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.file_name)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join()
        os.mkdir(path)
        path = os.path.join(path, self.file_name)
        self.image.save(image_path)


def showChosenImage():
    if list_noted.currentRow() >= 0:
        file_name = list_noted.currentItem().text()
        workimage.loadImage(file_name)
        image_path = os.path.join(workdir, workimage, file_name)
        workimage.showImage(image_path)


iw_files.currentRowChanged.connect(showChosenImage)

list_noted_label.clicked.connect(showChosenImage)




    





main_win.show()
app.exec_()








