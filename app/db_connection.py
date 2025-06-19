# db_connection.py (PostgreSQL version)

import pandas as pd
from sqlalchemy import create_engine
import os

def get_connection():
    return create_engine(
        f"postgresql+psycopg2://{os.environ['PGUSER']}:{os.environ['PGPASSWORD']}@{os.environ['PGHOST']}/{os.environ['PGDATABASE']}"
    )

def run_query(query):
    engine = get_connection()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)
