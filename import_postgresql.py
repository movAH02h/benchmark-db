from sqlalchemy import create_engine
import psycopg2
import pandas as pd

engine = create_engine("postgresql://postgres:admin@localhost:5432/task")

#Относительный путь к файлу
filename = 'D:\\Python\\nyc_yellow_big.csv'

df = pd.read_csv(filename)

df.to_sql('task', engine, if_exists='replace', index=False, chunksize=1000, method='multi')