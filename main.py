# COMP 490-001
# Senior Design & Development S22
# Dr. John F. Santore
# Gibeom Park

import sys
import requests
import secrets
import sqlite3
import firstwindow
from typing import Tuple
from PyQt5.QtWidgets import QApplication, QMainWindow


# Sprint 1

def get_data(datalist):
    with open("predata.txt", "w") as predata:
        for item in datalist:
            predata.write("id:%s, rank:%s, title:%s, fullTitle:%s, year:%s, image:%s, crew:%s, imDbRating:%s, "
                          "imDbRatingCount:%s \n" % (item['id'], item['rank'], item['title'], item['fullTitle'],
                                                     item['year'], item['image'], item['crew'], item['imDbRating'],
                                                     item['imDbRatingCount']))
    predata.close()
    return


def write_data(datalist):
    with open("show_data.txt", "a") as showdata:
        for item in datalist:
            showdata.write("Title:%s, Rank:%s \n" % (item['title'], item['rank']))
    showdata.close()
    return


def get_ratings(datalist_one, datalist_two, datalist_three, datalist_four, datalist_five):
    with open("show_data.txt", "w") as showdata:
        for ratings in datalist_one:
            showdata.write("Rank 1: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                           ratings['votes']))
        for ratings in datalist_two:
            showdata.write("Rank 50: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                            ratings['votes']))
        for ratings in datalist_three:
            showdata.write("Rank 100: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                             ratings['votes']))
        for ratings in datalist_four:
            showdata.write("Rank 200: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                             ratings['votes']))
        for ratings in datalist_five:
            showdata.write("Wheel of Time: Rating:%s, Percent:%s, Votes:%s \n" % (ratings['rating'], ratings['percent'],
                                                                                  ratings['votes']))
    return


# Sprint 2

def db_setup(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS show_data(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    showYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings_data(
    imdbID TEXT DEFAULT '',
    totalRating FLOAT DEFAULT 0,
    totalVotes INTEGER DEFAULT 0,
    tenRating FLOAT NOT NULL ,
    tenVotes INTEGER NOT NULL ,
    nineRating FLOAT NOT NULL ,
    nineVotes INTEGER NOT NULL ,
    eightRating FLOAT NOT NULL ,
    eightVotes INTEGER NOT NULL ,
    sevenRating FLOAT NOT NULL ,
    sevenVotes INTEGER NOT NULL ,
    sixRating FLOAT NOT NULL ,
    sixVotes INTEGER NOT NULL ,
    fiveRating FLOAT NOT NULL ,
    fiveVotes INTEGER NOT NULL ,
    fourRating FLOAT NOT NULL ,
    fourVotes INTEGER NOT NULL ,
    threeRating FLOAT NOT NULL ,
    threeVotes INTEGER NOT NULL ,
    twoRating FLOAT NOT NULL ,
    twoVotes INTEGER NOT NULL ,
    oneRating FLOAT NOT NULL ,
    oneVotes INTEGER NOT NULL ,
    FOREIGN KEY (imdbID) REFERENCES show_data (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')
    return


def db_open(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()
    return connection, cursor


def db_close(connection: sqlite3.Connection):
    connection.commit()
    connection.close()
    return


def db_populate_top250(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist):
    for item in datalist:
        cursor.execute("""INSERT INTO show_data (id, title, fullTitle, crew, showYear, imdbRating, imdbRatingCount)
        VALUES (?,?,?,?,?,?,?)""", (item['id'], item['title'], item['fullTitle'], item['crew'], item['year'],
                                    item['imDbRating'], item['imDbRatingCount']))
    connection.commit()
    return


def db_populate_ratings(connection: sqlite3.Connection, cursor: sqlite3.Cursor,
                        datalist_one, iddata_one, datalist_two, iddata_two, datalist_three,
                        iddata_three, datalist_four, iddata_four, datalist_five, iddata_five):
    for ratings in datalist_one:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes,
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata_one['imDbId'], iddata_one['totalRating'], iddata_one['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist_two:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes,
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata_two['imDbId'], iddata_two['totalRating'], iddata_two['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist_three:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes,
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata_three['imDbId'], iddata_three['totalRating'], iddata_three['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist_four:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes,
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata_four['imDbId'], iddata_four['totalRating'], iddata_four['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))

    for ratings in datalist_five:
        cursor.execute("""INSERT INTO ratings_data (imdbID, totalRating, totalVotes, tenRating, tenVotes,
         nineRating, nineVotes, eightRating, eightVotes, sevenRating, sevenVotes, sixRating, sixVotes,
         fiveRating, fiveVotes, fourRating, fourVotes, threeRating, threeVotes, twoRating, twoVotes,
          oneRating, oneVotes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (iddata_five['imDbId'], iddata_five['totalRating'], iddata_five['totalRatingVotes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes'],
                        ratings['percent'], ratings['votes'], ratings['percent'], ratings['votes']))
    connection.commit()
    return


# Sprint 3

def db_setup_two(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_tv_data(
    id TEXT PRIMARY KEY,
    rank INTEGER NOT NULL,
    rankUpDown FLOAT NOT NULL,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    showYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS top250_movie_data(
    id TEXT PRIMARY KEY,
    rank INTEGER NOT NULL,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    movieYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_movie_data(
    id TEXT PRIMARY KEY,
    rank INTEGER NOT NULL,
    rankUpDown FLOAT NOT NULL,
    title TEXT NOT NULL,
    fullTitle TEXT NOT NULL,
    crew TEXT NOT NULL,
    showYear INTEGER NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS rank_updown_data(
    id TEXT NOT NULL ,
    title TEXT NOT NULL ,
    rank INTEGER NOT NULL ,
    rankUpDown FLOAT NOT NULL,
    imdbRating FLOAT NOT NULL,
    imdbRatingCount FLOAT NOT NULL,
    FOREIGN KEY (id) REFERENCES popular_movie_data (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    )''')
    return


def db_populate_popular_tv(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist_tv):
    for item in datalist_tv:
        cursor.execute("""INSERT INTO popular_tv_data (id, rank, rankUpDown, title, fullTitle,
         crew, showYear, imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?,?,?,?)""",
                       (item['id'], item['rank'], item['rankUpDown'], item['title'], item['fullTitle'],
                        item['crew'], item['year'], item['imDbRating'], item['imDbRatingCount']))
    connection.commit()
    return


def db_populate_top250_movies(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist_topmovies):
    for item in datalist_topmovies:
        cursor.execute("""INSERT INTO top250_movie_data (id, rank, title, fullTitle,
        crew, movieYear, imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?,?,?)""",
                       (item['id'], item['rank'], item['title'], item['fullTitle'],
                        item['crew'], item['year'], item['imDbRating'], item['imDbRatingCount']))
        connection.commit()
    return


def db_populate_popular_movies(connection: sqlite3.Connection, cursor: sqlite3.Cursor, datalist_movies):
    for item in datalist_movies:
        cursor.execute("""INSERT INTO popular_movie_data (id, rank, rankUpDown, title, fullTitle,
        crew, showYear, imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?,?,?,?)""",
                       (item['id'], item['rank'], item['rankUpDown'], item['title'], item['fullTitle'],
                        item['crew'], item['year'], item['imDbRating'], item['imDbRatingCount']))
    connection.commit()
    return


def get_rank_updown(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute('SELECT MAX(rankUpDown) FROM popular_movie_data')
    res_one = cursor.fetchall()
    max_rank_one = res_one[0]
    cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rankUpDown DESC LIMIT 1 OFFSET 1')
    res_two = cursor.fetchall()
    max_rank_two = res_two[0]
    cursor.execute('SELECT rankUpDown FROM popular_movie_data ORDER BY rankUpDown DESC LIMIT 1 OFFSET 2')
    res_three = cursor.fetchall()
    max_rank_three = res_three[0]
    cursor.execute('SELECT MIN(rankUpDown) FROM popular_movie_data')
    res_four = cursor.fetchall()
    min_rank = res_four[0]

    # getting data from the select movies
    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (max_rank_one[0],))
    row_one = cursor.fetchall()

    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (max_rank_two[0],))
    row_two = cursor.fetchall()

    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (max_rank_three[0],))
    row_three = cursor.fetchall()

    cursor.execute('SELECT id, title, rank, imdbRating, imdbRatingCount FROM popular_movie_data '
                   'WHERE rankUpDown = ?', (min_rank[0],))
    row_four = cursor.fetchall()

    for item in row_one:  # first max rank
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], max_rank_one[0], item[1],
                        item[3], item[4]))

    for item in row_two:  # second max rank
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], max_rank_two[0], item[1],
                        item[3], item[4]))

    for item in row_three:  # third max rank
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], max_rank_three[0], item[1],
                        item[3], item[4]))

    for item in row_four:  # minrank
        cursor.execute("""INSERT INTO rank_updown_data (id, rank, rankUpDown, title,
                        imdbRating, imdbRatingCount)VALUES (?,?,?,?,?,?)""",
                       (item[0], item[2], min_rank[0], item[1],
                        item[3], item[4]))
    connection.commit()
    return


# Sprint 4

def gui_setup():
    app = QApplication(sys.argv)
    Firstwindow = firstwindow.FirstWindow()
    Firstwindow.show()
    sys.exit(app.exec())

def main():  # Main
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print("You got the Error!")
        return
    data = response.json()
    datalist = data['items']

    url_tv = f"https://imdb-api.com/en/API/MostPopularTVs/{secrets.secret_key}"
    response_tv = requests.get(url_tv)
    if response_tv.status_code != 200:
        print("You got the Error!")
        return
    data_tv = response_tv.json()
    datalist_tv = data_tv['items']

    url_topmovies = f"https://imdb-api.com/en/API/Top250Movies/{secrets.secret_key}"
    response_topmovies = requests.get(url_topmovies)
    if response_topmovies.status_code != 200:
        print("You got the Error!")
        return
    data_topmovies = response_topmovies.json()
    datalist_topmovies = data_topmovies['items']

    url_movies = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.secret_key}"
    response_movies = requests.get(url_movies)
    if response_movies.status_code != 200:
        print("You got the Error!")
        return
    data_movies = response_movies.json()
    datalist_movies = data_movies['items']

    rank_one = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt5491994"
    response_one = requests.get(rank_one)
    data_one = response_one.json()
    iddata_one = {key: data_one[key] for key in data_one.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist_one = data_one['ratings']
    rank50 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt2297757"
    response_two = requests.get(rank50)
    data_two = response_two.json()
    iddata_two = {key: data_two[key] for key in data_two.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist_two = data_two['ratings']
    rank100 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt0286486"
    response_three = requests.get(rank100)
    data_three = response_three.json()
    iddata_three = {key: data_three[key] for key in data_three.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist_three = data_three['ratings']
    rank200 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt1492966"
    response_four = requests.get(rank200)
    data_four = response_four.json()
    iddata_four = {key: data_four[key] for key in data_four.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist_four = data_four['ratings']
    rankwheelof = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"
    response_five = requests.get(rankwheelof)
    data_five = response_five.json()
    iddata_five = {key: data_five[key] for key in data_five.keys() & {'imDbId', 'totalRating', 'totalRatingVotes'}}
    datalist_five = data_five['ratings']

    name = 'show_data.db'
    connection, cursor = db_open(name)

    # sprint 1
    get_data(datalist)
    get_ratings(datalist_one, datalist_two, datalist_three, datalist_four, datalist_five)
    write_data(datalist)
    # sprint 2
    db_setup(cursor)
    db_populate_top250(connection, cursor, datalist)
    db_populate_ratings(connection, cursor,
                        datalist_one, iddata_one, datalist_two, iddata_two, datalist_three, iddata_three, datalist_four,
                        iddata_four, datalist_five, iddata_five)
    db_close(connection)

    # sprint 3
    db_setup_two(cursor)
    db_populate_popular_tv(connection, cursor, datalist_tv)
    db_populate_top250_movies(connection, cursor, datalist_topmovies)
    db_populate_popular_movies(connection, cursor, datalist_movies)
    get_rank_updown(connection, cursor)
    db_close(connection)

    gui_setup()
    return


if __name__ == '__main__':
    main()
