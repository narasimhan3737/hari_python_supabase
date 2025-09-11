def read_data(supabase, table_name):
    response = supabase.table(table_name).select("*").execute()
    return response

    # You can also add filters:
    # response = supabase.table('your_table_name').select("*").eq("column_name", "value").execute()
