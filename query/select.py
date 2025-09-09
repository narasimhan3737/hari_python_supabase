import pandas as pd

def select_data(supabase):
    result = supabase.table("ewntal_spaces").select("*").execute()
    data = result.data
    df_rentalspaces = pd.DataFrame(data)