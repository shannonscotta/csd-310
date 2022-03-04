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
    query = "SELECT * FROM team"
    cursor.execute(query)

    teams = cursor.fetchall()
    print("\n  -- DISPLAYING ALL TEAMS --")
    for team in teams: 
        print(f"Team ID: {team[0]}")
        print(f"Team Name: {team[1]}")
        print(f"Team Mascot: {team[2]}\n")

    cursor = db.cursor()
    query = "SELECT * FROM player"
    cursor.execute(query)

    players = cursor.fetchall()
    print ("\n  -- DISPLAYING ALL PLAYERS --")
    for player in players:
        print(f"Player ID: {player[0]}")
        print(f"First Name: {player[1]}")
        print(f"Last Name: {player[2]}")
        print(f"Team: {player[3]}\n")

    input("\n\n  Press any key to continue")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The specified username or password does not exist")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)
finally:
    db.close()

#added 