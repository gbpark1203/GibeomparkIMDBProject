# COMP 490-001
# Senior Design & Development S22
# Dr. John F. Santore
# Gibeom Park

import requests
import secrets
import sqlite3
from typing import Tuple


def api_connect():
    return requests.get('https://imdb-api.com/API/Top250TVs/' + secrets.secret_key)

def get_user_data(movie_id):
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.secret_key + '/' + movie_id)

def write_to_file(top_tv_shows_list):
    with open("TV Show Data.txt", "a") as writeFile:
        writeFile.write(top_tv_shows_list)

#

def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename) # connect to existing DB or crete new one
    cursor = db_connection.cursor() # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit() # make sure any changes get saved
    connection.close()


def test_db():
    connection, cursor = open_db('demo_db.sqlite')
    print(type(connection))
    close_db(connection)

def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_250_tv_shows(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating REAL DEFAULT 0,
    imdb_rating_count INTEGER DEFAULT 0
    );''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_ratings(
    imdb_id TEXT PRIMARY KEY,
    total_rating INTEGER DEFAULT 0,
    total_rating_votes INTEGER DEFAULT 0,
    ten_rating_percent REAL DEFAULT 0,
    ten_rating_votes INTEGER DEFAULT 0,
    nine_rating_percent REAL DEFAULT 0,
    nine_rating_votes INTEGER DEFAULT 0,
    eight_rating_percent REAL DEFAULT 0,
    eight_rating_votes INTEGER DEFAULT 0,
    seven_rating_percent REAL DEFAULT 0,
    seven_rating_votes INTEGER DEFAULT 0,
    six_rating_percent REAL DEFAULT 0,
    six_rating_votes INTEGER DEFAULT 0,
    five_rating_percent REAL DEFAULT 0,
    five_rating_votes INTEGER DEFAULT 0,
    four_rating_percent REAL DEFAULT 0,
    four_rating_votes INTEGER DEFAULT 0,
    three_rating_percent REAL DEFAULT 0,
    three_rating_votes INTEGER DEFAULT 0,
    two_rating_percent REAL DEFAULT 0,
    two_rating_votes INTEGER DEFAULT 0,
    one_rating_percent REAL DEFAULT 0,
    one_rating_votes INTEGER DEFAULT 0,
    FOREIGN KEY (imdb_id) REFERENCES top_250_tv_shows (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')

if __name__ == '__main__':
    imdb_API = api_connect()
    print(imdb_API.status_code)

    #rank 1
    write_to_file("User Ratings:" + "\n")
    rank1_rated_show = get_user_data('tt5491994') # Planet Earth II (TV Mini Series 2016) - IMDb
    write_to_file(str(rank1_rated_show.json()) + "\n")
    print(rank1_rated_show.json())

    #rank 50
    rank50_rated_show = get_user_data('tt2297757') # Nathan for You (TV Series 2013–2017) - IMDb
    write_to_file(str(rank50_rated_show.json()) + "\n")
    print(rank50_rated_show.json())

    #rank 100
    rank100_rated_show = get_user_data('tt0286486') # The Shield (TV Series 2002–2008) - IMDb
    write_to_file(str(rank100_rated_show.json()) + "\n")
    print(rank100_rated_show.json())

    #rank 200
    rank200_rated_show = get_user_data('tt1492966') # Louie (TV Series 2010–2015) - IMDb
    write_to_file(str(rank200_rated_show.json()) + "\n")
    print(rank200_rated_show.json())

    #wheel of time rating
    Wheel_Of_Time_rating = get_user_data('tt7462410') # The Wheel of Time (TV Series 2021– ) - IMDb
    write_to_file(str(Wheel_Of_Time_rating.json()) + "\n")
    print(Wheel_Of_Time_rating.json())

    write_to_file("List of Top 250 TV Shows:" + "\n")
    text_value = imdb_API.text
    value_list = text_value.split('},{')
    value_list[0] = value_list[0][11:]
    for n in value_list:
        print(n)
        write_to_file(n + "\n")
    conn, cur = open_db('imdb_db.sqlite')
    setup_db(cur)
    close_db(conn)
