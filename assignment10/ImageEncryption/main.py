from functools import partial
import cv2
import numpy as np
import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox
from PySide6.QtGui import QPixmap
from ui import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.encrypted_image = None
        self.key = None
        self.encrypt_image_address = None
        self.ui.pushButton_load_encrypt.clicked.connect(self.load_encrypt)
        self.ui.pushButton_encrypt.clicked.connect(partial(self.encryption))
        self.ui.pushButton_decrypt.clicked.connect(partial(self.decryption))

    def load_encrypt(self):
        file_name = QFileDialog.getOpenFileName(self,
                    "Open Image", "./", "Image Files (*.png *.jpg *.bmp)")
        if file_name[0]:
            image_pixmap = QPixmap(f"{file_name[0]}")
            self.ui.label_encrypt.setPixmap(image_pixmap.scaled(
                self.ui.label_encrypt.size()
            ))
            self.encrypt_image_address = file_name[0]

    def encryption(self):
        if self.encrypt_image_address:
            input_image = cv2.imread(f"{self.encrypt_image_address}", cv2.COLOR_BGR2RGB)
            x, y, z = input_image.shape
            mu, sigma = 0.0, 0.0001
            key = np.random.normal(mu, sigma, (x, y, z))
            np.save('output/secret_key.npy', key)
            input_image = input_image.astype(float) / 255
            image_encrypted = input_image / key
            cv2.imwrite('output/CipherImage.bmp', image_encrypted * 255)
            self.encrypted_image = image_encrypted
            self.key = key
            QMessageBox.information(self, "Success", "Encrypted Image in output Folder")
            encrypt_image_pixmap = QPixmap("output/CipherImage.bmp")
            self.ui.label_decrypt.setPixmap(encrypt_image_pixmap.scaled(
                self.ui.label_decrypt.size()
            ))

    def decryption(self):
        output_image = self.encrypted_image * self.key
        output_image *= 255.0
        cv2.imwrite('output/DecryptImage.jpg', output_image)
        decrypt_image_pixmap = QPixmap("output/DecryptImage.jpg")
        self.ui.label_decrypt.setPixmap(decrypt_image_pixmap.scaled(
            self.ui.label_decrypt.size()
        ))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()