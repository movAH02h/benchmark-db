import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
df = pd.read_csv('D:\\Python\\nyc_yellow_big.csv')
df.columns = [*df.columns[:-1], 'last_fee']
df.to_sql('users', con=engine, if_exists='replace', index=False, chunksize=1000, method='multi')