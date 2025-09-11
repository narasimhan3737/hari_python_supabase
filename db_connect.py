from dotenv import load_dotenv
import os
from supabase import Client, create_client

load_dotenv()


def connect():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    try:
        # Initialize the Supabase client
        supabase: Client = create_client(url, key)
    except Exception as e:
        print(f"Failed to create Supabase client: {e}")
        exit()

    return supabase
