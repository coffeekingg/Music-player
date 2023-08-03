from PyQt5 import QtCore,  QtWidgets, QtMultimedia
import interface
import os


class Player(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.play)
        self.pushButton_2.clicked.connect(self.stop)
        self.listWidget.itemDoubleClicked.connect(self.play)
        self.pushButton_3.clicked.connect(self.load)

        self.dir = ""

        self.setFixedSize(self.size())

    def play(self):
        item = self.listWidget.currentItem()

        if item:
            file_name = os.path.join(self.dir, item.text())
            content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))

            self.mediaPlayer = QtMultimedia.QMediaPlayer()
            self.mediaPlayer.setMedia(content)
            self.mediaPlayer.play()
        else:
            self.listWidget.setCurrentRow(0)
            self.play()

    def stop(self):
        self.mediaPlayer.stop()

    def load(self):
        self.listWidget.clear()

        dir1 = QtWidgets.QFileDialog.getExistingDirectory(self)

        if dir1:
            for file_name in os.listdir(dir1):
                if file_name.endswith(".mp3"):
                    self.listWidget.addItem(os.path.join(file_name))
            self.dir = dir1


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()