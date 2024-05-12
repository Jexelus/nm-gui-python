from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QTextBrowser, QLabel
from PyQt6.QtGui import QPixmap


class ImageRadioButton(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.selected = False
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(image_path))
        self.image_label.mousePressEvent = self.on_click
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.image_label)

    def on_click(self, event):
        self.selected = not self.selected
        self.update_style()

    def update_style(self):
        if self.selected:
            self.setStyleSheet("""
                ImageRadioButton {
                    border: 2px solid blue;
                }
            """)
        else:
            self.setStyleSheet("""
                ImageRadioButton {
                    border: none;
                }
            """)

class NetworkInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(60)
        self.network_name = "None"
        self.ip_address = "None"
        self.vpn_name = "None"
        self.initUI()

    def initUI(self):
        network_info = QHBoxLayout()
        network_info.setObjectName("network-info")

        r_btn = ImageRadioButton("./static/wifi.svg")
        r_btn.setObjectName("network-info-rbn")
        r_btn.setFixedHeight(60)
        r_btn.setFixedWidth(60)
        network_info.addWidget(r_btn)
        text_block = QVBoxLayout()

        network_name_text = QLabel()
        network_name_text.setObjectName("network-info-network-name-text")
        network_name_text.setText("Network: " + self.network_name)
        network_name_text.setFixedHeight(10)
        text_block.addWidget(network_name_text)

        ip_address_text = QLabel()
        ip_address_text.setObjectName("network-info-ip-address-text")
        ip_address_text.setText("IP: " + self.ip_address)
        ip_address_text.setFixedHeight(10)
        text_block.addWidget(ip_address_text)

        vpn_name_text = QLabel()
        vpn_name_text.setObjectName("network-info-vpn-name-text")
        vpn_name_text.setText("VPN: " + self.vpn_name)
        vpn_name_text.setFixedHeight(10)
        text_block.addWidget(vpn_name_text)
        self.setLayout(network_info)

        text_block.setObjectName("network-info-text-block")
        network_info.addLayout(text_block)




class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        view = QVBoxLayout()
        view.setObjectName("nm-gui-python-main-layout")
        view.addWidget(NetworkInfo())
        self.setLayout(view)


