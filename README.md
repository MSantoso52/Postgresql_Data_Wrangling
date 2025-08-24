# Postgresql_Data_Wrangling
# *Overview*
Project repo to demonstrate Data Wrangling in PostgreSQL, process start with importing Data Source JSON file into PostgreSQL, Data Observation using Jupyterlab by checking duplication, missing value, inconsistent data type. Data Cleaning refer to Data Observation & Finally Geneate Business Insight for Data Analytics or Data Science.
# *Prererquisites*
To follow along this project neeb to be available on your system:
- Python3 with psycopgy2, jupyterlab
  ```bash
  sudo apt install python3

  pip install psycopg2, jupyterlab
  ```
- PostgreSQL running on system
  ```bash
  sudo systemctl status postgresql
  ```
- Vim installed (optional)
  ```bash
  sudo apt install vim
  ```
# *Project Flow*
1. Import necessary library
   ```python3
   import psycopg2
   from psycopg2 import extras
   ```
3. Create postgreSQL connection
   ```python3
   conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
   cur = conn.cursor()
   ```
5. Import JSON file into postgresql
   ```python3
   # Insert the record into the database
    cur.execute(insert_sql, record_values)
   ....
   # Commit the changes and close the connection
   conn.commit()
   ```
7. Data observation
   ```python3
   import pandas as pd

   columns = [desc[0] for desc in cur.description]
   df = pd.DataFrame(data, columns = columns)
   df.head()
   .....
   # Checking duplicate value
   cur.execute(duplicate_order_id)
   duplicates = cur.fetchall()
   if duplicates:
        print("Duplicate order_id found")
   else:
       print("No duplicate found on order_id")
   # Checking null value
   def check_for_none(cursor, table_name, column_name):
     query = f"SELECT * FROM {table_name} WHERE {column_name} IS NULL;"
     print(f"Executing {query}")
     cursor.execute(query)
     result = cursor.fetchall()
     if result:
        print(f"Found NULL on {column_name}")
     else:
        print(f"Not found NULL on {column_name}")
   ```
9. Data cleaning
10. Generate Business Insight
11. CLose connindtion
   ```python3
   # Close cursor
   cur.close()
   # Close connection
   conn.close()
   ```
