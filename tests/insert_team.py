import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connect import connect
from datetime import timedelta
from db_insert.insert import insert_data
if __name__ == "__main__":
    supabase = connect()
    table='team_db'
    data = {
        'team_name': 'Tottenham Girls',
        'club_name': 'Tottenham',
        'city': 'London',
        'location': 'UK',
    }
    print("Inserting data")
    insert_data(supabase, table,data)