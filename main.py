from db_connect import connect
from query.update import update_data
from query.insert import insert_data
if __name__ == "__main__":
    supabase = connect()
    data = insert_data(supabase,"test_table")
    print(data)
    

