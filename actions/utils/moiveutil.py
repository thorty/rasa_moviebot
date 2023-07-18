# knowledge = Path("data/pokemons.txt").read_text().split("\n")

import pandas as pd


# def main():
#     dataPath = "../data/movies.dat"
#     df_movies = readData(dataPath)


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


# if __name__ == "__main__":
#     main()
