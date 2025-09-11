def delete_data(supabase, table_name):
    data = supabase.table(table_name).delete().eq("id", 1).execute()
    return data
