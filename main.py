# COMP 490-001
# Senior Design & Development S22
# Dr. John F. Santore
# Gibeom Park

import requests
import secrets


def api_connect():
    return requests.get('https://imdb-api.com/API/Top250TVs/' + secrets.secret_key)

def get_user_data(movie_id):
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.secret_key + '/' + movie_id)

def write_to_file(top_tv_shows_list):
    with open("TV Show Data.txt", "a") as writeFile:
        writeFile.write(top_tv_shows_list)

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
