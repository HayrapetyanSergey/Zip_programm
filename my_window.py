from  PyQt5 import QtWidgets,QtCore
from  PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog,QMessageBox
import zip
import rezip  
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.filename = None

        self.setWindowTitle("Compression and Decompression Window")
        self.setFixedSize(320, 300)
        self.setGeometry(500, 350, 350, 200)

        # Creating MenuBar
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        fileMenu = QMenu("File", self)
        self.menuBar.addMenu(fileMenu)
        fileMenu.addAction("Open", self.menu_action_clicked)

        self.compress_btn = QtWidgets.QPushButton(self)
        self.compress_btn.move(60, 150)
        self.compress_btn.setText("Compress")
        self.compress_btn.setFixedWidth(200)

        self.decompress_btn = QtWidgets.QPushButton(self)
        self.decompress_btn.move(60, 180)
        self.decompress_btn.setText("DeCompress")
        self.decompress_btn.setFixedWidth(200)

        self.compress_btn.clicked.connect(self.compress_clicked)
        self.decompress_btn.clicked.connect(self.decompress_clicked)

        # Error box
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setIcon(QMessageBox.Warning)

    def compress_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            zip.create(self.filename)


    def decompress_clicked(self):
        if self.filename == "" or self.filename == None:
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("Give me a file!")
            self.error.exec_()
        else:
            rezip.restore(self.filename)


    @QtCore.pyqtSlot()
    def menu_action_clicked(self):
        self.filename = QFileDialog.getOpenFileName(self)[0]
        if self.filename == '':
            pass
        elif not self.filename.endswith(".txt"):
            self.error.setText("Not valid file               ")
            self.error.setInformativeText("File must have .txt extentions")
            self.error.exec_()
        else:
            pass

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()