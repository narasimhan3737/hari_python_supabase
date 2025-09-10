def update_match(supabase,match_id: int, new_status: str, new_location: str):
    """
    Updates the match_status and location of a specific match in the match_db table.

    Args:
        match_id (int): The ID of the match to update.
        new_status (str): The new status for the match.
        new_location (str): The new location for the match.
    """
    try:
        response = supabase.table('match_db').update(
            {'match_status': new_status, 'location': new_location}
        ).eq('match_id', match_id).execute()

        # Check for errors in the response
        if response.data:
            print(f"Successfully updated match with ID: {match_id}")
            print("Updated data:", response.data)
        else:
            print(f"No match found with ID: {match_id} or update failed.")

    except Exception as e:
        print(f"An error occurred during the update: {e}")