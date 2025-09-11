import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_connect import connect
import datetime
from datetime import timedelta
from db_insert.insert import insert_data

if __name__ == "__main__":
    supabase = connect()
    table = "match_db"
    data = {
        "match_name": "Inspire Girls v Tottenham Girls",
        "match_date": datetime.date.strftime(datetime.date.today(), format="%d/%m/%Y"),
        "duration": timedelta(minutes=90, seconds=30).total_seconds(),
        "location": "UK",
        "team1_id": 1,
        "team2_id": 2,
        "match_status": "Full time",
    }

    print("Inserting data")
    insert_data(supabase, table, data)
