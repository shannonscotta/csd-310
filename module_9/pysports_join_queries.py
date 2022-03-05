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
    query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    cursor.execute(query)

    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print(f"Player ID: {player[0]}\n" +
              f"First Name: {player[1]}\n" +
              f"Last Name: {player[2]}\n" +
              f"Team: {player[3]}\n")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Invalid database")
    else:
        print(err)
finally:
    db.close()
