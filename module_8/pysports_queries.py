import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    queryOne = "SELECT * FROM team"
    cursor.execute(queryOne)

    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print(f"Team ID: {team[0]}\n" +
              f"Team Name: {team[1]}\n" +
              f"Team Mascot: {team[2]}\n")

    cursor = db.cursor()
    queryTwo = "SELECT * FROM player"
    cursor.execute(queryTwo)

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}\n" +
              f"First Name: {player[1]}\n" +
              f"Last Name: {player[2]}\n" +
              f"Team: {player[3]}\n")

    input("\n  Press any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Invalid database")
    else:
        print(err)
finally:
    db.close()
