def update_data(supabase, table_name: str):
    data = (
        supabase.table(table_name)
        .update({"column1": "new_value"})
        .eq("id", 1)
        .execute()
    )
    return data
