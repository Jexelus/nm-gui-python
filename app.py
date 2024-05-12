import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QStyleFactory, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import QFile, QTextStream, Qt
# print(QStyleFactory.keys())
from components.mainLayout import MainLayout


class NmGuiPython(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName('nm-gui-python-window')
        #todo: INFO WIDGET
        #todo: left side list networks
        #todo: right side buttons

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        center_x = (screen_geometry.width() - self.width()) // 2
        center_y = (screen_geometry.height() - self.height()) // 2

        self.setStyleSheet(open('./static/window.css').read())

        layout = QVBoxLayout()
        layout.setObjectName("body")
        layout.addWidget(MainLayout())

        self.setLayout(layout)
        self.setFixedSize(int(screen_geometry.width() / 2), int(screen_geometry.height() / 2))
        self.move(center_x, center_y)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint, )
        self.setWindowTitle('nm-gui-python')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = NmGuiPython()
    widgets = app.allWidgets()
    for widget in widgets:
        print(widget.objectName())
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
