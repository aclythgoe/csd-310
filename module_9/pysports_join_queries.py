"""
Andrew Lythgoe 
December 12, 2021
Module 9 Assignment 9.2
"""
# Import MySQL Connector and Error code
import mysql.connector
from mysql.connector import Error

# Create Database pysports connection
db = mysql.connector.connect(host='localhost',
                             database='pysports',
                             user='pysports_user',
                             password='MySQL8IsGreat!')

# Iterate the cursor for the query
cursor = db.cursor(buffered=True)

# Set up and execute the inner join query
cursor.execute("""\
SELECT player_id, first_name, last_name, team_name FROM player
INNER JOIN team
    ON player.team_id = team.team_id""")

# Fetch player records
players = cursor.fetchall()

# Output
print(" -- DISPLAYING PLAYER RECORDS -- ")

# Output of player records
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team Name: {player[3]}")
    print("\n")
