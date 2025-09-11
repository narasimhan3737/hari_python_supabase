from typing import Dict, List
import pandas as pd

def load_dataframe(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df

def dataframe_to_records(df: pd.DataFrame) -> List[Dict]:
    # Convert NaN to None so they become NULL in the database
    return df.where(pd.notnull(df), None).to_dict(orient="records")

def insert_in_chunks(
    supabase, table_name: str, records: List[Dict], chunk_size: int, dry_run: bool = False
) -> int:
    if chunk_size <= 0:
        chunk_size = len(records)

    inserted_count = 0
    for start in range(0, len(records), chunk_size):
        chunk = records[start : start + chunk_size]
        if dry_run:
            print(
                f"[DRY-RUN] Would insert {len(chunk)} rows into {table_name} (rows {start + 1}-{start + len(chunk)})"
            )
            inserted_count += len(chunk)
            continue

        response = supabase.table(table_name).insert(chunk).execute()
        if response.data:
            print(
                f"Inserted {len(response.data)} rows into {table_name} (rows {start + 1}-{start + len(response.data)})"
            )
            inserted_count += len(response.data)
        else:
            print(
                f"Insert attempted for {len(chunk)} rows (rows {start + 1}-{start + len(chunk)});no representation returned."
            )
            inserted_count += len(chunk)
    return inserted_count

def insert_df_data(supabase, pd, table_name, dry_run):

    records = dataframe_to_records(pd)
    if not records:
        print("No records to insert. Exiting")
        return None
    total_inserted = insert_in_chunks(
        supabase=supabase,
        table_name=table_name,
        records=records,
        chunk_size=0,
        dry_run=dry_run
    )
    print(f"Done. Total rows processed: {total_inserted}")    