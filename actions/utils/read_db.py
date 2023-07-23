import sqlite3
import logging

logging.basicConfig(level=logging.INFO)


def search_title(title):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies WHERE title LIKE ?", (f"%{title}%",))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


def search_year(year):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies WHERE year=?", (year,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


def search_genre(genre):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM movies WHERE genre LIKE '%{genre}%'")
    rows = cursor.fetchall()

    # for row in rows:
    #     print(row)
    connection.close()
    return(rows)


def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("/opt/mybot/actions/data/movies.db")
    except Exception as e:
        logging.error(e)

    return connection


if __name__ == "__main__":
    # search_genre("Crime")
    # search_year(2000)
    search_title("Boys Don't Cry")
