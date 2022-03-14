from PyQt5.QtWidgets import QMainWindow, QPushButton, QListWidget, QLabel, QVBoxLayout
import main

class MovieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label_one = None
        self.label_two = None
        self.pop_movies_list = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Movie Data Window")
        self.setGeometry(0, 0, 800, 800)
        self.layout = QVBoxLayout()
        self.label_one = QLabel("Popular Movies")
        self.label_one.move(100, 10)
        self.layout.addWidget(self.label_one)
        pop_movies_list = QListWidget(self)
        pop_movies_list.move(50, 20)
        pop_movies_list.resize(300, 500)
        self.layout.addWidget(pop_movies_list)
        self.label_two = QLabel("Top 250 Movies")
        self.label_two.move(500, 100)
        self.layout.addWidget(self.label_two)
        top250movies_list = QListWidget(self)
        top250movies_list.move(450, 20)
        top250movies_list.resize(300, 500)
        self.layout.addWidget(top250movies_list)
        crossover_list = QListWidget(self)
        crossover_list.move(250, 600)
        crossover_list.resize(300, 150)
        self.layout.addWidget(crossover_list)

        name = 'show_data.db'
        connection, cursor = main.db_open(name)

        rank_button = QPushButton("Rank", self)
        rank_button.clicked.connect(lambda: self.add_list_data_rank(pop_movies_list, cursor))
        rank_button.move(50, 550)
        self.layout.addWidget(rank_button)
        rank_updown_button = QPushButton("UpDown", self)
        rank_updown_button.clicked.connect(lambda: self.add_list_data_rank_updown(pop_movies_list, cursor))
        rank_updown_button.move(150, 550)
        clear_button = QPushButton("Clear", self)
        clear_button.clicked.connect(lambda: self.clear_list(pop_movies_list))
        clear_button.move(250, 550)
        self.layout.addWidget(rank_updown_button)
        self.setLayout(self.layout)
        self.add_list_data_top250(top250movies_list, cursor)
        self.add_list_data_crossover(crossover_list, cursor)

    def add_list_data_rank(self, pop_movies_list, cursor):
        cursor.execute('SELECT title FROM popular_movie_data ORDER BY rank ASC ')
        result_one = cursor.fetchall()

        cursor.execute('SELECT rank FROM popular_movie_data ORDER BY rank ASC ')
        result_two = cursor.fetchall()

        cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rank ASC')
        result_three = cursor.fetchall()

        result = []
        for count in range(0, len(result_one)):
            result.append("Title: " + str(result_one[count]) +
                          " Rank: " + str(result_two[count]) + " RankUpDown " + str(result_three[count]))

        pop_movies_list.addItems(result)
        return

    def add_list_data_rankupdown(self, pop_movies_list, cursor):
        cursor.execute('SELECT title FROM popular_movie_data ORDER BY rankUpDown DESC ')
        result_one = cursor.fetchall()

        cursor.execute('SELECT rank FROM popular_movie_data ORDER BY rankUpDown DESC ')
        result_two = cursor.fetchall()

        cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rankUpDown DESC ')
        result_three = cursor.fetchall()

        result = []
        for count in range(0, len(result_one)):
            result.append("Title: " + str(result_one[count]) +
                          " Rank: " + str(result_two[count]) + " RankUpDown " + str(result_three[count]))

        pop_movies_list.addItems(result)
        return

    def add_list_data_top250(self, top250movies_list, cursor):
        cursor.execute('SELECT title FROM main.top250_movie_data ')
        result_one = cursor.fetchall()

        result = []
        for count in range(0, len(result_one)):
            result.append("Title: " + str(result_one[count]))

        top250movies_list.addItems(result)
        return

    def add_list_data_crossover(self, crossover_list, cursor):
        cursor.execute('SELECT main.top250_movie_data.title FROM main.top250_movie_data '
                       'INNER JOIN main.popular_movie_data ON top250_movie_data.id = popular_movie_data.id')
        title_list = cursor.fetchall()

        result = []
        for count in range(0, len(title_list)):
            result.append("Title: " + str(title_list[count]))
        crossover_list.addItems(result)
        return

    def clear_list(self, pop_movies_list):
        pop_movies_list.clear()
        return
