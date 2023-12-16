import duckdb
import time

def firstQuery():
    connection = duckdb.connect('database2.duckdb')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, avg(total_amount) FROM users GROUP BY 1;''')
    end = time.time()

    print(round(end - start, 3))

    cur.close()
    connection.close()


def secondQuery():
    connection = duckdb.connect('database2.duckdb')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM users GROUP BY 1, 2;''')
    end = time.time()

    print(round(end - start, 3))

    cur.close()
    connection.close()


def thirdQuery():
    connection = duckdb.connect('database2.duckdb')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS pickup_year, 
    count(*) FROM users GROUP BY 1, 2;''')
    end = time.time()

    print(round(end - start, 3))

    cur.close()
    connection.close()


def fourthQuery():
    connection = duckdb.connect('database2.duckdb')
    cur = connection.cursor()

    start = time.time()
    cur.execute('''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS year, round(trip_distance), 
    count(*) FROM users GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC''')
    end = time.time()

    print(round(end - start, 3))

    cur.close()
    connection.close()

firstQuery()
secondQuery()
thirdQuery()
fourthQuery()

