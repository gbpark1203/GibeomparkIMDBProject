from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import datawindow


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.data_window = None

    def setup_window(self):
        self.setWindowTitle("IMDB First Window")
        self.setGeometry(50, 50, 200, 100)
        update_button = QPushButton("Update Data!", self)
        update_button.move(150, 0)
        data_button = QPushButton("Visualization", self)
        data_button.clicked.connect(lambda: self.setup_data_window())
        data_button.move(150, 50)
        close_button = QPushButton("Close Now", self)
        close_button.clicked.connect(QApplication.instance().close)
        close_button.move(150, 100)
        self.show()

    def setup_data_window(self):
        self.data_window = datawindow.DataWindow()
        self.data_window.show()