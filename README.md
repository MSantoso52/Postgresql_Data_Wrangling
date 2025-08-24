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
2. Create postgreSQL connection
3. Import JSON file into postgresql
4. Data observation
5. Data cleaning
6. Generate Business Insight
7. CLose connindtion
   ```python3
   # Close cursor
   cur.close()
   # Close connection
   conn.close()
   ```
