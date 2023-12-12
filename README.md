# benchmark-db

**Подготовка:**
- Загрузить библиотки для работы с БД в Python:
  * psycopg2
  * sqlite3
  * duckdb
  * sqlalchemy
  * pandas
     
- Загрузить pgadmin для работы с postgreSQL
  
- После импорта csv файла в pgadmin столбцы с датами имеют тип TEXT. Нужно поменять этот тип на TIMETAMP without timezone для работы ф-ии EXTRACT:
  * *ALTER TABLE <имя таблицы> ALTER COLUMN tpep_pickup_datetime type TIMESTAMP USING create_time::TIMESTAMP;*
  * *ALTER TABLE <имя таблицы> ALTER COLUMN tpep_dropoff_datetime type TIMESTAMP USING create_time::TIMESTAMP;*
   
- При импорте в .db из csv файла нужно поменять название столбца Airport_fee или удалить его вообще, т.к. там находятся NULL. Он выдает ошибку, потому что airport_fee (предпоследний столбец) = Airport_fee (последний столбец):
  	* df.columns = [*df.columns[:-1], 'last_fee'] -> перед командой to_sql
  
- Для duckdb лучше использовать отдельный файл .duckdb, чтобы не подключать сторонние штучки по типу sqlite_scanner

**Объяснение:**

- В файле benchmark.xlsx лежат все проделанные тесты и полученные сравнительные графики
  
- В файлах import_postgresql, import_db, import_duckdb находятся программы для импорта базы данных из csv файлов, чтобы мы могли с ними спокойно работать
