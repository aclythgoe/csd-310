import mysql.connector
from mysql.connector import errorcode


config = {
    "user" : "pysports_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warings" : True
}

try:
    db = mysql.connector.connect(config)

    print(f"\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]
    print("\n\n Press any key to continue...")


except mysql.connector.error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplies username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
    finally:
        db.close()
