from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.label = QLabel("Hello world!")

        # self.pixmap = QPixmap("scripts/dummy/pizzeria.jpeg")
        # self.label.setPixmap(self.pixmap)

        layout.addWidget(self.label)
        central_widget.setLayout(layout)

        self.setWindowTitle("TicketScanner")
