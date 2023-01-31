import json
import datetime
from psycopg2 import extras

# Get the largest single-day jump in vaccinations for a given month.
# This function skips any non-consecutive days, i.e., if the 2nd of the month is missing,
# then we won't count the 1st and the 3rd as a single-day jump.
def single_day_jump(connection, state, month, year):
  query = f"SELECT * FROM covid WHERE location='{state}' AND date::text LIKE '{year}-{month}-__'"

  cursor = connection.cursor(cursor_factory = extras.RealDictCursor)
  cursor.execute(query)
  entries = cursor.fetchall()

  jumps = {}

  # Create a dictionary that holds jumps
  # Key of 1 symbolizes the jump from the 1st to the 2nd of the month
  for index, entry in enumerate(entries):
    current_day = entry[0]
    if index + 1 == len(entries):
      break
    next_day = entries[index + 1][0]
    timedelta = next_day - current_day

# Returns a state's data from start to end date (inclusive)
def fetch_date_range(connection, state, start_date, end_date):
  query = f"SELECT * FROM covid WHERE location='{state}' AND date >= '{start_date}' AND date <= '{end_date}'"
  cursor = connection.cursor(cursor_factory = extras.RealDictCursor)

  cursor.execute(query)
  entries = cursor.fetchall()
  return entries

# Returns a list of all states vaccination numbers
def fetch_latest_records_per_state(connection):
  # 2023-01-18 is the latest populated entry
  # Exclude 'United States' from this query because it skews data
  query = f"SELECT * FROM covid WHERE date='2023-01-18' AND location != 'United States'"
  cursor = connection.cursor(cursor_factory = extras.RealDictCursor)
  cursor.execute(query)
  entries = cursor.fetchall()
  return entries
