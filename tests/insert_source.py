import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_connect import connect
from datetime import timedelta
from db_insert.insert import insert_data

if __name__ == "__main__":
    supabase = connect()
    table = "source_db"
    data = {
        "run_id": 1,
        "source_name": "test_video",
        "match_id": 4,
        "source_path": "/videos/match1/cam1.mp4",
        "length": timedelta(minutes=90, seconds=30).total_seconds(),
    }
    print("Inserting data")
    insert_data(supabase, table, data)
