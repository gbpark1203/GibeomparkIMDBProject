from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import graphwindow
import moviedatawindow
import tvdatawindow


class DataWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.graph_window = None
        self.tv_window = None
        self.movie_window = None


    def setup_window(self):
        self.setWindowTitle("Data Window")
        self.setGeometry(50, 50, 200, 100)
        graph_button = QPushButton("Ranking Graph Data", self)
        graph_button.clicked.connect(lambda: self.setup_graph_window())
        graph_button.move(250, 0)
        tv_button = QPushButton("TV Data Chart", self)
        tv_button.clicked.connect(lambda: self.setup_tv_window())
        tv_button.move(250, 50)
        movie_button = QPushButton("Movie Data Chart", self)
        movie_button.clicked.connect(lambda: self.setup_movie_window())
        movie_button.move(250, 100)
        self.show()

    def setup_graph_window(self):
        self.graph_window = graphwindow.GraphWindow()
        self.graph_window.show()

    def setup_tv_window(self):
        self.tv_window = tvdatawindow.TVWindow()
        self.tv_window.show()

    def setup_movie_window(self):
        self.movie_window = moviedatawindow.MovieWindow()
        self.movie_window.show()