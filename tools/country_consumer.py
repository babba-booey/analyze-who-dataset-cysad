import json
import psycopg2
import sys

DSN = "host=127.0.0.1 port=5432 user=naive_etl_app password=password dbname=cysad"

connection = psycopg2.connect(DSN)

cursor = connection.cursor()

query = """
insert into who_countries values(
    
)
"""

raw_json = sys.stdin.readline()

while raw_json:
    message = json.loads(raw_json)
    sequence_id = message.get("display_sequence")
    country_code = message.get("label")
    country_name = message.get("display")
    
    raw_json = sys.stdin.readline()
