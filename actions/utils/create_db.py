import sqlite3
from pathlib import Path
import logging
import os.path

import pandas as pd

logging.basicConfig(level=logging.INFO)


def readData_toDF(dataPath):
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
    return df_movies


def readData_toDict(dataPath):
    movieDict = {}

    with open(dataPath, "r") as dataFile:
        for line in dataFile:
            line = line.replace("\n", "")
            lineSplit = line.split("::")

            id = lineSplit[0]
            title_date = lineSplit[1]
            genre = lineSplit[2]

            title, date = split_title_time(title_date)
            title = title.lower()
            genre = genre.lower()
            genre = genre.split("|")

            movieDict[id] = [title, date, ",".join(genre)]
    return movieDict


def split_title_time(title_date: str):
    title = title_date[:-7]
    date = title_date[len(title_date) - 7 :]

    date = date.replace("(", "").strip(")").strip()
    return title, date


def create_db(dbPath, movieDict):
    if os.path.isfile(dbPath):
        logging.info("DB: Not created, was already there")

        connection = sqlite3.connect(dbPath)
        cursor = connection.cursor()

        for item in movieDict:
            cursor.execute(
                "INSERT OR IGNORE INTO movies (id, title, year, genre) VALUES (?, ?, ?, ?)",
                (
                    item,
                    movieDict[item][0].lower(),
                    movieDict[item][1],
                    movieDict[item][2].lower(),
                ),
            )
            connection.commit()

        connection.close()
    else:
        connection = sqlite3.connect(dbPath)
        cursor = connection.cursor()

        # sql_command = """
        # CREATE TABLE movies (
        # id INTEGER,
        # title TEXT, 
        # year INTEGER, 
        # genre TEXT
        # UNIQUE(id)
        # );"""

        cursor.execute(
            "CREATE TABLE movies (id INTEGER, title TEXT, year INTEGER, genre TEXT, UNIQUE(id))"
        )
        connection.commit()
        connection.close()
        logging.info("DB: created")


if __name__ == "__main__":
    movieDict = readData_toDict("/opt/mybot/actions/data/movies.dat")
    create_db("/opt/mybot/actions/data/movies.db", movieDict)
