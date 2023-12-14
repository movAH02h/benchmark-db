import psycopg2
import time


db_params = {
    'dbname': 'task',
    'user': 'postgres',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '5432'
}

def firstQuery():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    start = time.time()
    cursor.execute('''SELECT "VendorID", count(*) FROM task GROUP BY 1;''')
    end = time.time()

    print(end - start)

    cursor.close()
    connection.close()


def secondQuery():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    start = time.time()
    cursor.execute('''SELECT passenger_count, avg(total_amount) FROM task GROUP BY 1;''')
    end = time.time()

    print(end - start)

    cursor.close()
    connection.close()


def thirdQuery():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    start = time.time()
    cursor.execute('''SELECT
                     passenger_count,
                     extract(year from tpep_pickup_datetime),
                     count(*)
                    FROM task
                    GROUP BY 1, 2;''')
    end = time.time()

    print(end - start)

    cursor.close()
    connection.close()


def fourthQuery():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    start = time.time()
    cursor.execute('''SELECT
                     passenger_count,
                     extract(year from tpep_pickup_datetime),
                     round(trip_distance),
                     count(*)
                    FROM task
                    GROUP BY 1, 2, 3
                    ORDER BY 2, 4 desc;
''')
    end = time.time()

    print(end - start)

    cursor.close()
    connection.close()


firstQuery()
secondQuery()
thirdQuery()
fourthQuery()
