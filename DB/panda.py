import pandas
import sqlalchemy
import time

def firstQuery():

    engine = sqlalchemy.create_engine('sqlite:///database.db')

    start = time.time()
    sql_df = pandas.read_sql('''SELECT "VendorID", count(*) FROM users GROUP BY 1;''', engine)
    end = time.time()

    print(end - start)

def secondQuery():

    engine = sqlalchemy.create_engine('sqlite:///database.db')

    start = time.time()
    sql_df = pandas.read_sql('''SELECT "VendorID", count(*) FROM users GROUP BY 1;''', engine)
    end = time.time()

    print(end - start)

def thirdQuery():

    engine = sqlalchemy.create_engine('sqlite:///database.db')

    start = time.time()
    sql_df = pandas.read_sql('''SELECT "VendorID", count(*) FROM users GROUP BY 1;''', engine)
    end = time.time()

    print(end - start)

def fourthQuery():

    engine = sqlalchemy.create_engine('sqlite:///database.db')

    start = time.time()
    sql_df = pandas.read_sql('''SELECT "VendorID", count(*) FROM users GROUP BY 1;''', engine)
    end = time.time()

    print(end - start)

firstQuery()
secondQuery()
thirdQuery()
fourthQuery()
