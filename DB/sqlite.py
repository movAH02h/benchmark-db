import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import time

def firstQuery():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT "VendorID", count(*) FROM users GROUP BY 1;''')
    end = time.time()

    print(end - start)

    cur.close()
    connection.close()


def secondQuery():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, avg(total_amount) FROM users GROUP BY 1;''')
    end = time.time()

    print(end - start)

    cur.close()
    connection.close()


def thirdQuery():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS pickup_year, 
    count(*) FROM users GROUP BY 1, 2;''')
    end = time.time()

    print(end - start)

    cur.close()
    connection.close()


def fourthQuery():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS year, round(trip_distance), 
    count(*) FROM users GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''')
    end = time.time()

    print(end - start)

    cur.close()
    connection.close()

firstQuery()
secondQuery()
thirdQuery()
fourthQuery()