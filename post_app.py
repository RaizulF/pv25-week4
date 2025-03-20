import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class PostApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 550)
        self.setWindowTitle("Post App")
        
        form_layout = QFormLayout()
        self.product = QComboBox()
        self.product.addItems(["", "Bimoli (Rp. 20,000)", 
                               "Beras 5 Kg (Rp. 75,000)", 
                               "Kecap ABC (Rp. 7,000)", 
                               "Saos Saset (Rp. 2,000)"])
        self.discount = QComboBox()
        self.discount.addItems(["", "0%", "5%", "10%", "15%"])
        self.quantity_edit = QLineEdit()
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Product</span>"), self.product)
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Quantity</span>"), self.quantity_edit)
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Discount</span>"), self.discount)

        self.listView = QListWidget()
        self.listView.setStyleSheet("background-color: #57B4BA; color: #000; font-weight: bold;")
        self.listView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.total = 0
        self.label_total = QLabel("Total: Rp. {}".format(self.total))

        button_layout = QHBoxLayout()
        self.button_add = QPushButton("Add to Cart")
        self.button_clear = QPushButton("Clear")
        self.button_add.setProperty('class', 'success')
        self.button_clear.setProperty('class', 'danger')
        self.button_add.clicked.connect(self.addToCart)
        self.button_clear.clicked.connect(self.clearProduct)
        button_layout.addWidget(self.button_add)
        button_layout.addWidget(self.button_clear)

        self.label_nama = QLabel("<span style='font-weight: bold; color: #000; font-size:10pt;'>Nama: Raizul Furkon</span>")
        self.label_nim = QLabel("<span style='font-weight: bold; color: #000; font-size:10pt'>NIM: F1D022024</span>")
        self.label_kelas = QLabel("<span style='font-weight: bold; color: #000; font-size:10pt'>Kelas: C</span>")
        self.label_nama.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label_nim.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label_kelas.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label_nama)
        main_layout.addWidget(self.label_nim)
        main_layout.addWidget(self.label_kelas)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.listView)
        main_layout.addWidget(self.label_total)

        self.setLayout(main_layout)

    def addToCart(self):
        product = self.product.currentText()
        discount = self.discount.currentText()
        quantity = self.quantity_edit.text()

        if quantity.isdigit() and product and discount:
            display_price = "Rp. " + product.split("(Rp. ")[1].split(")")[0]
            price = int(product.split("(Rp. ")[1].split(")")[0].replace(",", ""))
            discount = int(discount.replace("%", ""))
            priceAfterDiscount = int(quantity) * price * (100 - discount) / 100
            self.listView.addItem(f"{product} - {quantity} x - {display_price} (disc {discount}%) = price: Rp. {int(priceAfterDiscount):,}")
            self.total += priceAfterDiscount
            self.label_total.setText(f"Total: Rp. {int(self.total):,}")
        else:
            self.label_total.setText("Invalid input")

    def clearProduct(self):
        self.listView.clear()
        self.total = 0
        self.label_total.setText("Total: Rp. {}".format(self.total))

extra = {
    'danger': '#dc3545',
    'success': '#8BC34A',
}

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PostApp()
    apply_stylesheet(app, theme='light_red.xml', invert_secondary=True, extra=extra)
    window.show()
    sys.exit(app.exec_())
