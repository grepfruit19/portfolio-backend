import psycopg2
import csv
from fileio import load_csv_into_table
from queries import single_day_jump, fetch_date_range

conn = psycopg2.connect(
  host="localhost",
  database="covid"
)
cursor = conn.cursor()
# load_csv_into_table(cursor)
fetch_date_range(cursor, "New York State", "12", "2021")
conn.commit()
cursor.close()
conn.close()

# print(parse_csv())