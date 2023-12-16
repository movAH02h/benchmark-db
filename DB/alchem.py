import sqlalchemy
import time

def firstQuery():
    engine = sqlalchemy.create_engine('sqlite:///database.db')

    connection = engine.connect()
    query = sqlalchemy.text('''SELECT "VendorID", count(*) FROM users GROUP BY 1;''')

    start = time.time()
    connection.execute(query)
    end = time.time()

    print(end - start)

    connection.close()

def secondQuery():
    engine = sqlalchemy.create_engine('sqlite:///database.db')

    connection = engine.connect()
    query = sqlalchemy.text('''SELECT passenger_count, avg(total_amount) FROM users GROUP BY 1;''')

    start = time.time()
    connection.execute(query)
    end = time.time()

    print(end - start)

    connection.close()

def thirdQuery():
    engine = sqlalchemy.create_engine('sqlite:///database.db')

    connection = engine.connect()
    query = sqlalchemy.text('''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS pickup_year, 
    count(*) FROM users GROUP BY 1, 2;''')

    start = time.time()
    connection.execute(query)
    end = time.time()

    print(end - start)

    connection.close()

def fourthQuery():
    engine = sqlalchemy.create_engine('sqlite:///database.db')

    connection = engine.connect()
    query = sqlalchemy.text('''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS year, round(trip_distance), 
    count(*) FROM users GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''')

    start = time.time()
    connection.execute(query)
    end = time.time()

    print(end - start)

    connection.close()

firstQuery()
secondQuery()
thirdQuery()
fourthQuery()
