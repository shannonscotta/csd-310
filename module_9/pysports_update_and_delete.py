# scott shannon               Mod 9.3 DB                5 March 2022
#  The purpose of this code is to update, delete, and insert mysql

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

def showPlayers(collection):
    for row in collection:
        print(f"Player ID: {row[0]}\n" +
              f"First Name: {row[1]}\n" +
              f"Last Name: {row[2]}\n" +
              f"Team: {row[3]}\n")


# insert a new record into the player table for team gandalf
try:
    query = "INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1);"
    cursor = db.cursor()
    cursor.execute(query)

    # end transaction
    db.commit()

    query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;"
    cursor.execute(query)

    all_rows = cursor.fetchall()

    print(f"\n - - DISPLAYING PLAYERS AFTER INSERT - -")
    showPlayers(all_rows)


# update players team to team sauron
    query = "UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';"
    cursor = db.cursor()
    cursor.execute(query)

    db.commit()

    query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;"
    cursor.execute(query)

    all_rows = cursor.fetchall()

    print(f"\n - - DISPLAYING PLAYERS AFTER UPDATE - -")
    showPlayers(all_rows)


# delete the updated record
    query = "DELETE FROM player WHERE first_name = 'Gollum'"

    cursor = db.cursor()
    cursor.execute(query)

    db.commit()

    query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;"

    cursor.execute(query)

    all_rows = cursor.fetchall()

    print(f"\n - - DISPLAYING PLAYERS AFTER DELETE - -")
    showPlayers(all_rows)

    # add input to match expectation image from documentation
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
