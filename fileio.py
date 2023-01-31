def load_csv_into_table(cursor):
  # Drop table just so we start fresh
  # cursor.execute("DROP TABLE entries")
  file = open("us_state_vaccinations.csv", "r")
  cursor.execute(
    """
      CREATE TABLE covid (
          date date,
          location text,
          total_vaccinations decimal,
          total_distributed decimal,
          people_vaccinated decimal,
          people_fully_vaccinated_per_hundred decimal,
          total_vaccinations_per_hundred decimal,
          people_fully_vaccinated decimal,
          people_vaccinated_per_hundred decimal,
          distributed_per_hundred decimal,
          daily_vaccinations_raw decimal,
          daily_vaccinations decimal,
          daily_vaccinations_per_million decimal,
          share_doses_used decimal,
          total_boosters decimal,
          total_boosters_per_hundred decimal
      )
    """
  )
  cursor.execute(
    """
      COPY entries FROM '/Users/willkim/Documents/interview/covid/us_state_vaccinations.csv' WITH (FORMAT CSV, DELIMITER(','), NULL '')
    """
  )