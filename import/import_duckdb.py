import duckdb

connection = duckdb.connect('database2.duckdb')
cur = connection.cursor()
cur.execute('''CREATE TABLE users AS SELECT * FROM read_csv_auto('D:\\Python\\nyc_yellow_big.csv')''')