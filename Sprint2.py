# COMP 490-001
# Senior Design & Development S22
# Dr. John F. Santore
# Gibeom Park


import sqlite3
import requests
import secrets
from typing import Tuple


def get_top_tv_250_data():
    api_query = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    response = requests.get(api_query)
    show_list = response.json()
    shows = show_list['items']
    return shows

def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()
    return connection, cursor


def set_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS shows (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        fullTitle TEXT NOT NULL,
        year INTEGER DEFAULT 0,
        crew TEXT NOT NULL,
        imDbRating REAL DEFAULT 0,
        imDbRatingCount INTEGER DEFAULT 0
        );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings (
            imDbID TEXT NOT NULL,
            totalRating INTEGER DEFAULT 0,
            totalRatingVotes INTEGER DEFAULT 0,
            ten_rating_percentage REAL DEFAULT 0,
            ten_rating_votes INTEGER DEFAULT 0,
            nine_rating_percentage REAL DEFAULT 0,
            nine_rating_votes INTEGER DEFAULT 0,
            eight_rating_percentage REAL DEFAULT 0,
            eight_rating_votes INTEGER DEFAULT 0,
            seven_rating_percentage REAL DEFAULT 0,
            seven_rating_votes INTEGER DEFAULT 0,
            six_rating_percentage REAL DEFAULT 0,
            six_rating_votes INTEGER DEFAULT 0,
            five_rating_percentage REAL DEFAULT 0,
            five_rating_votes INTEGER DEFAULT 0,
            four_rating_percentage REAL DEFAULT 0,
            four_rating_votes INTEGER DEFAULT 0,
            three_rating_percentage REAL DEFAULT 0,
            three_rating_votes INTEGER DEFAULT 0,
            two_rating_percentage REAL DEFAULT 0,
            two_rating_votes INTEGER DEFAULT 0,
            one_rating_percentage REAL DEFAULT 0,
            one_rating_votes INTEGER DEFAULT 0,
            FOREIGN KEY (imDbId) REFERENCES shows (id)
            ON DELETE CASCADE
            );''')


def fill_shows_table(cursor: sqlite3.Cursor, shows):
    for i in range(0, len(shows)):
        cursor.execute('''INSERT INTO shows (id, title,
                       fullTitle, year, crew, imDbRating, imDbRatingCount)
                       VALUES(?, ?, ?, ?, ?, ?, ?)''',
                       (shows[i]['id'], shows[i]['title'], shows[i]['fullTitle'], shows[i]['year'],
                        shows[i]['crew'], shows[i]['imDbRating'], shows[i]['imDbRatingCount']))

    cursor.execute('SELECT rowid, * FROM shows')
    cursor.fetchall()


def wheel_of_time_into_shows_table(cursor: sqlite3.Cursor):
    cursor.execute('''INSERT INTO shows (id, title,
                           fullTitle, year, crew, imDbRating, imDbRatingCount)
                           VALUES(?, ?, ?, ?, ?, ?, ?)''',
                   ('tt0331080', 'Wheel of Time', 'Wheel of Time (2003)', '2003',
                    'The Dalai Lama, Lama Lhundup Woeser, Takna Jigme Sangpo',
                    0, 0))
    cursor.execute('SELECT rowid, * FROM shows')
    cursor.fetchone()

def fill_ratings_table(cursor: sqlite3.Cursor):
    shows = get_top_tv_250_data()
    user_url = f"https://imdb-api.com/en/API/UserRatings/"
    print('\n')
    for i in range(len(shows)):
        if shows[i]['rank'] == '1' or shows[i]['rank'] == '50' \
                or shows[i]['rank'] == '100' or shows[i]['rank'] == '201':
            r = requests.get(user_url + secrets.secret_key + "/" + shows[i]['id'])
            info = r.json()
            cursor.execute('''INSERT INTO ratings (imDbId, totalRating, totalRatingVotes,
            ten_rating_percentage, ten_rating_votes, nine_rating_percentage, nine_rating_votes,
            eight_rating_percentage, eight_rating_votes, seven_rating_percentage, seven_rating_votes,
            six_rating_percentage, six_rating_votes, five_rating_percentage, five_rating_votes, four_rating_percentage,
            four_rating_votes, three_rating_percentage, three_rating_votes, two_rating_percentage, two_rating_votes,
            one_rating_percentage, one_rating_votes)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (
                               info['imDbId'], info['totalRating'], info['totalRatingVotes'],
                               info['ratings'][0]['percent'], info['ratings'][0]['votes'],
                               info['ratings'][1]['percent'], info['ratings'][1]['votes'],
                               info['ratings'][2]['percent'], info['ratings'][2]['votes'],
                               info['ratings'][3]['percent'], info['ratings'][3]['votes'],
                               info['ratings'][4]['percent'], info['ratings'][4]['votes'],
                               info['ratings'][5]['percent'], info['ratings'][5]['votes'],
                               info['ratings'][6]['percent'], info['ratings'][6]['votes'],
                               info['ratings'][7]['percent'], info['ratings'][7]['votes'],
                               info['ratings'][8]['percent'], info['ratings'][8]['votes'],
                               info['ratings'][9]['percent'], info['ratings'][9]['votes']))

    cursor.execute('SELECT * FROM shows where title is "Wheel of Time"')
    cursor.fetchone()

    wheel_of_time_id = 'tt0331080'
    w = requests.get(user_url + secrets.secret_key + "/" + wheel_of_time_id)
    wheel_info = w.json()
    cursor.execute('''INSERT INTO ratings (imDbId, totalRating, totalRatingVotes,
                ten_rating_percentage, ten_rating_votes, nine_rating_percentage, nine_rating_votes,
                eight_rating_percentage, eight_rating_votes, seven_rating_percentage, seven_rating_votes,
                six_rating_percentage, six_rating_votes,
                five_rating_percentage, five_rating_votes, four_rating_percentage,
                four_rating_votes, three_rating_percentage, three_rating_votes, two_rating_percentage, two_rating_votes,
                one_rating_percentage, one_rating_votes)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (wheel_of_time_id, wheel_info['totalRating'],
                    wheel_info['totalRatingVotes'], wheel_info['ratings'][0]['percent'],
                    wheel_info['ratings'][0]['votes'], wheel_info['ratings'][1]['percent'],
                    wheel_info['ratings'][1]['votes'], wheel_info['ratings'][2]['percent'],
                    wheel_info['ratings'][2]['votes'], wheel_info['ratings'][3]['percent'],
                    wheel_info['ratings'][3]['votes'], wheel_info['ratings'][4]['percent'],
                    wheel_info['ratings'][4]['votes'], wheel_info['ratings'][5]['percent'],
                    wheel_info['ratings'][5]['votes'], wheel_info['ratings'][6]['percent'],
                    wheel_info['ratings'][6]['votes'], wheel_info['ratings'][7]['percent'],
                    wheel_info['ratings'][7]['votes'], wheel_info['ratings'][8]['percent'],
                    wheel_info['ratings'][8]['votes'], wheel_info['ratings'][9]['percent'],
                    wheel_info['ratings'][9]['votes']))

    cursor.execute('SELECT rowid, * FROM ratings')
    cursor.fetchall()

def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()

def main():
    shows = get_top_tv_250_data()
    conn, cursor = open_db('TV Show Data.db')
    print(type(conn))
    set_db(cursor)
    fill_shows_table(cursor, shows)
    wheel_of_time_into_shows_table(cursor)
    fill_ratings_table(cursor)
    close_db(conn)

if __name__ == '__main__':
    main()