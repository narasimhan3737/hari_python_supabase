def update_source(supabase, source_id: int, updates: dict):
    """
    Updates multiple fields of a specific record in the source_db table.

    Args:
        source_id (int): The ID of the source record to update.
        updates (dict): A dictionary of column names and their new values.
    """
    try:
        response = (
            supabase.table("source_db")
            .update(updates)
            .eq("source_id", source_id)
            .execute()
        )

        if response.data:
            print(f"Successfully updated source with ID: {source_id}")
            print("Updated data:", response.data)
        else:
            print(f"No source record found with ID: {source_id} or update failed.")

    except Exception as e:
        print(f"An error occurred during the update: {e}")
