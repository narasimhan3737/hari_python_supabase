def insert_data(supabase, table_name: str):
    data = (
        supabase.table(table_name)
        .insert({"column1": "value1", "column2": "value2"})
        .execute()
    )
    return data
