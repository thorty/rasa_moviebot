# knowledge = Path("data/pokemons.txt").read_text().split("\n")
import sqlite3
from pathlib import Path

import pandas as pd


def readData(dataPath):
    movieDict = {"id": [], "title": [], "date": [], "genre": []}

    with open(dataPath, "r") as dataFile:
        for line in dataFile:
            line = line.replace("\n", "")
            lineSplit = line.split("::")

            id = lineSplit[0]
            title_date = lineSplit[1]
            genre = lineSplit[2]

            title, date = split_title_time(title_date)
            genre = split_genre(genre)

            movieDict["id"].append(id)
            movieDict["title"].append(title)
            movieDict["date"].append(date)
            movieDict["genre"].append(",".join(genre))

            # print(f"{id}; {title}; {date}; {genre}")

    df_movies = pd.DataFrame.from_dict(movieDict)
    print(df_movies)
    return df_movies


def split_title_time(title_date: str):
    title = title_date[:-7]
    date = title_date[len(title_date) - 7 :]

    date = date.replace("(", "").strip(")").strip()
    return title, date


def split_genre(genre: str):
    return genre.split("|")


def create_db(dbPath):
    my_db = Path(dbPath)
    if my_db.is_file():
        connection = sqlite3.connect(dbPath)
        cursor = connection.cursor()

        sql_command = """
        CREATE TABLE movies (
        id INTEGER,
        title TEXT, 
        year INTEGER, 
        genre TEXT
        );"""

        cursor.execute(sql_command)

        connection.commit()
        connection.close()
        return True
    else:
        return False


if __name__ == "__main__":
    create_db("/opt/mybot/actions/data/movies.db")
    df_movies = readData("/opt/mybot/actions/data/movies.dat")
