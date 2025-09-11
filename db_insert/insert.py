def insert_data(supabase, db_table,data: dict):
    """
    Inserts a new record into the source_db table.

    Args:
        supabase: The Supabase client instance.
        data (dict): A dictionary containing the data to insert.
    """
    try:
        response = supabase.table(db_table).insert(data).execute()

        if response.data:
            print("Successfully inserted new source record.")
            print("Inserted data:", response.data)
        else:
            print("Failed to insert new source record.")

    except Exception as e:
        print(f"An error occurred during the insertion: {e}")