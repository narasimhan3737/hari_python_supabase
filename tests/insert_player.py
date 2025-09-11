import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connect import connect
import datetime
from datetime import timedelta
from db_insert.insert import insert_data
if __name__ == "__main__":
    supabase = connect()
    table='player_db'
    players = [
        {'first_name': 'Natalie', 'last_name': 'Parker', 'date_of_birth': '02/14/1998', 'position': 'Goalkeeper', 'location': 'USA', 'jersey_number': 1, 'team_id': 2},
        {'first_name': 'Olivia', 'last_name': 'Reed', 'date_of_birth': '07/22/1999', 'position': 'Defender', 'location': 'USA', 'jersey_number': 2, 'team_id': 2},
        {'first_name': 'Paige', 'last_name': 'Carter', 'date_of_birth': '03/10/2000', 'position': 'Defender', 'location': 'Canada', 'jersey_number': 3, 'team_id': 2},
        {'first_name': 'Quinn', 'last_name': 'Morales', 'date_of_birth': '11/05/1997', 'position': 'Defender', 'location': 'Mexico', 'jersey_number': 4, 'team_id': 2},
        {'first_name': 'Riley', 'last_name': 'Stewart', 'date_of_birth': '08/30/1998', 'position': 'Defender', 'location': 'UK', 'jersey_number': 5, 'team_id': 2},
        {'first_name': 'Sabrina', 'last_name': 'Patel', 'date_of_birth': '01/18/2001', 'position': 'Midfielder', 'location': 'USA', 'jersey_number': 6, 'team_id': 2},
        {'first_name': 'Tessa', 'last_name': 'Morgan', 'date_of_birth': '05/26/2000', 'position': 'Midfielder', 'location': 'Korea', 'jersey_number': 7, 'team_id': 2},
        {'first_name': 'Uma', 'last_name': 'Flores', 'date_of_birth': '09/09/1999', 'position': 'Midfielder', 'location': 'India', 'jersey_number': 8, 'team_id': 2},
        {'first_name': 'Violet', 'last_name': 'James', 'date_of_birth': '12/12/1998', 'position': 'Midfielder', 'location': 'USA', 'jersey_number': 9, 'team_id': 2},
        {'first_name': 'Willow', 'last_name': 'Barnes', 'date_of_birth': '04/04/1997', 'position': 'Forward', 'location': 'USA', 'jersey_number': 10, 'team_id': 2},
        {'first_name': 'Zoe', 'last_name': 'Phillips', 'date_of_birth': '06/15/2001', 'position': 'Forward', 'location': 'USA', 'jersey_number': 11, 'team_id': 2}
    ]
    
    print("Inserting full team roster for team_id = 2")
    for player in players:
        insert_data(supabase, table, player)
    print(f"Inserted {len(players)} players into {table} for team_id 2")