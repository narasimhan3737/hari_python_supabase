import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connect import connect
from datetime import timedelta
from db_insert.source import insert_source
if __name__ == "__main__":
    supabase = connect()
    source_id_to_update = 1
    insert_data = {
        'run_id': 1,
        'source_name': 'test_video',
        'match_id': 1,
        'source_path': '/videos/match1/cam1.mp4',
        'length': timedelta(minutes=90, seconds=30).total_seconds()
    }

    print(f"Attempting to perform a full update on source record {source_id_to_update}...")
    insert_source(supabase,source_id_to_update, insert_data)