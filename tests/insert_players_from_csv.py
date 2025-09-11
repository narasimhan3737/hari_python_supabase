import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from typing import List, Dict, Optional
import pandas as pd
from db_connect import connect


def load_dataframe(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df


def add_or_override_team_id(df: pd.DataFrame, team_id: Optional[int]) -> pd.DataFrame:
    if team_id is None:
        return df
    df = df.copy()
    df["team_id"] = team_id
    return df


def dataframe_to_records(df: pd.DataFrame) -> List[Dict]:
    # Convert NaN to None so they become NULL in the database
    return df.where(pd.notnull(df), None).to_dict(orient="records")


def insert_in_chunks(
    supabase, table: str, records: List[Dict], chunk_size: int, dry_run: bool = False
) -> int:
    if chunk_size <= 0:
        chunk_size = len(records)

    inserted_count = 0
    for start in range(0, len(records), chunk_size):
        chunk = records[start : start + chunk_size]
        if dry_run:
            print(
                f"[DRY-RUN] Would insert {len(chunk)} rows into {table} (rows {start + 1}-{start + len(chunk)})"
            )
            inserted_count += len(chunk)
            continue

        response = supabase.table(table).insert(chunk).execute()
        if response.data:
            print(
                f"Inserted {len(response.data)} rows into {table} (rows {start + 1}-{start + len(response.data)})"
            )
            inserted_count += len(response.data)
        else:
            # Supabase may return no data when Prefer: return=representation is not set; still count optimistically
            print(
                f"Insert attempted for {len(chunk)} rows (rows {start + 1}-{start + len(chunk)});no representation returned."
            )
            inserted_count += len(chunk)
    return inserted_count


def main():
    parser = argparse.ArgumentParser(
        description="Bulk insert players from a CSV into a Supabase table using pandas."
    )
    parser.add_argument("--csv", required=True, help="Path to CSV file")
    parser.add_argument(
        "--table", default="player_db", help="Target table name (default: player_db)"
    )
    parser.add_argument(
        "--team-id",
        type=int,
        default=None,
        help="Override/add a single team_id for all rows",
    )
    parser.add_argument(
        "--chunk-size", type=int, default=500, help="Insert batch size (default: 500)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not insert, only print what would happen",
    )

    args = parser.parse_args()

    supabase = connect()

    print(f"Loading CSV: {args.csv}")
    df = load_dataframe(args.csv)
    print(f"Loaded {len(df)} rows")

    if args.team_id is not None:
        print(f"Setting team_id={args.team_id} for all rows")
        df = add_or_override_team_id(df, args.team_id)

    records = dataframe_to_records(df)
    if not records:
        print("No records to insert. Exiting.")
        return

    print(
        f"Inserting into table: {args.table} | chunk_size={args.chunk_size} | dry_run={args.dry_run}"
    )
    total_inserted = insert_in_chunks(
        supabase=supabase,
        table=args.table,
        records=records,
        chunk_size=args.chunk_size,
        dry_run=args.dry_run,
    )

    print(f"Done. Total rows processed: {total_inserted}")


if __name__ == "__main__":
    main()
