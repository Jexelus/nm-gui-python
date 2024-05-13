from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QTextBrowser, QLabel, QApplication, \
    QSpacerItem, QSizePolicy, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap


class ImageRadioButton(QWidget):
    def __init__(self):
        super().__init__()
        self.is_selected = False
        self.image = QSvgWidget('./assets/wifi.svg')
        self.initUI()
        self.setFixedHeight(60)
        self.setFixedWidth(60)

    def initUI(self):
        layout = QHBoxLayout()
        layout.addWidget(self.image)
        self.setLayout(layout)


class NetworkInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(60)
        self.network_name = "None"
        self.ip_address = "None"
        self.vpn_name = "None"
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addWidget(ImageRadioButton())
        text_container = QVBoxLayout()
        network_name_label = QLabel(f"NETWORK: {self.network_name}")
        ip_address_label = QLabel(f"IP: {self.ip_address}")
        vpn_name_label = QLabel(f"VPN: {self.vpn_name}")
        text_container.addWidget(network_name_label)
        text_container.addWidget(ip_address_label)
        text_container.addWidget(vpn_name_label)
        layout.addLayout(text_container)
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.setStyleSheet("background-color: #E5F7FF; color: black;")
        self.setLayout(layout)
