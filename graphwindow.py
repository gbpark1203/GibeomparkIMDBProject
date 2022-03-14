import main
import sqlite3
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt



class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Graph Data Window")
        self.setGeometry(0, 0, 800, 800)
        self.graph_setup()
        self.show()

    def count_tv_up(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_tv_data '
                       'WHERE rankUpDown > 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def count_tv_down(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_tv_data '
                       'WHERE rankUpDown < 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def count_movie_up(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_movie_data '
                       'WHERE rankUpDown > 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def count_movie_down(self, connection: sqlite3.Connection, cursor: sqlite3.Cursor):
        cursor.execute('SELECT rankUpDown FROM popular_movie_data '
                       'WHERE rankUpDown < 0')
        result = cursor.fetchall()
        count = len(result)
        return count

    def graph_setup(self):
        name = 'show_data.db'
        connection, cursor = main.db_open(name)
        count_tv_up = self.count_tvup(connection, cursor)
        count_tv_down = self.count_tvup(connection, cursor)
        count_movie_up = self.count_tvup(connection, cursor)
        count_movie_down = self.count_tvup(connection, cursor)

        barset_one = QBarSet("Rank Up")
        barset_two = QBarSet("Rank Down")

        barset_one << count_tv_up << count_movie_up
        barset_two << count_tv_down << count_movie_down

        series = QPercentBarSeries()
        series.append(barset_one)
        series.append(barset_two)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Popular Rank Data")
        categories = ["TVs", "Movies"]
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)

        return