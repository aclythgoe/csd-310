"""
Andrew Lythgoe 
December 12, 2021
Module 9 Assignment 9.3
"""

# Import Connector and Error code
import mysql.connector
from mysql.connector import Error

# Create connection to database
db = mysql.connector.connect(host='localhost',
                             database='pysports',
                             user='pysports_user',
                             password='MySQL8IsGreat!')

# Print Cursor

# Create and execute cursors for INSERT and display output
insert = db.cursor(buffered=True)
insert.execute("""\
INSERT INTO player (first_name, last_name, team_id)
   VALUES('Smeagol', 'Shire Folk', 1);""")

# Display output after INSERT
print1 = db.cursor(buffered=True)
print1.execute("""\
    SELECT player_id, first_name, last_name, team_name FROM player
    INNER JOIN team
        ON player.team_id = team.team_id""")

# Fetch and Print  
print("-- DISPLAYING PLAYERS AFTER INSERT -- ")
players = print1.fetchall()
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team: {player[3]}")
    print("\n")
# Create and execute cursors for UPDATE and display output
update = db.cursor(buffered=True)
update.execute("""\
    UPDATE player
    SET first_name = 'Gollum',last_name = 'Ring Stealer'
    WHERE first_name='Gollum';""")


# Display output after UPDATE
print2 = db.cursor(buffered=True)
print2.execute("""\
    SELECT player_id, first_name, last_name, team_name FROM player
    INNER JOIN team
        ON player.team_id = team.team_id""")

# Fetch and Print  
print("-- DISPLAYING PLAYERS AFTER UPDATE -- ")
players2 = print2.fetchall()
for players in players2:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team: {player[3]}")
    print("\n")

delete = db.cursor(buffered=True)
delete.execute("""\
DELETE FROM player
WHERE first_name = 'Gollum';""")

# Display output after DELETE
print3 = db.cursor(buffered=True)
print3.execute("""\
    SELECT player_id, first_name, last_name, team_name FROM player
    INNER JOIN team
        ON player.team_id = team.team_id""")

# Fetch and Print  
print("-- DISPLAYING PLAYERS AFTER DELETE -- ")
players3 = print3.fetchall()
for players in players3:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team: {player[3]}")
    print("\n")


# Press any key to continue text
print("\n\n\nPress any key to continue...")
