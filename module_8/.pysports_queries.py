"""
Andrew Lythgoe
December 11,2021
Module 8.3 Assignment
"""

"""
Allow connection to Pysports Database
"""

import mysql.connector
from mysql.connector import Error

"""
Connect to pysports database
"""

connection = mysql.connector.connect(host='localhost',
                                     database='pysports',
                                     user='pysports_user',
                                     password='MySQL8IsGreat!')

"""
1 - Iterate the cursor for executing MySQL Code
2 - Select the tables from the pysports database
"""

cursor = connection.cursor(buffered=True)
cursor2 = connection.cursor(buffered=True)
cursor.execute("SELECT team_id, team_name, mascot FROM team;")
cursor2.execute("SELECT player_id, first_name, last_name, team_id FROM player")

# Fetch all data for teams and players
teams = cursor.fetchall()
players = cursor2.fetchall()

# Output 
print(" -- DISPLAYING TEAM RECORDS -- ")

# Output for all teams in the teams table
for team in teams:
    print(f"Team ID: {team[0]}")
    print(f"Team Name: {team[1]}")
    print(f"Mascot: {team[2]}")
    print("\n")

print("\n -- DISPLAYING PLAYER RECORDS --")

# Output for all players in player table
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team ID: {player[3]}")
    print("\n")



    




