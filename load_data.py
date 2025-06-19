import pandas as pd
from sqlalchemy import create_engine
import os

# ⬇️ Replace this with your actual Neon PostgreSQL connection string
DATABASE_URL = "postgresql://neondb_owner:npg_TZLmdp6rRaY2@ep-cool-thunder-a5bnqnfj-pooler.us-east-2.aws.neon.tech/rental_2024?sslmode=require"

engine = create_engine(DATABASE_URL)

csv_table_map = {
    "stores.csv": "stores",
    "genres.csv": "genres",
    "films.csv": "films",
    "customers.csv": "customers",
    "rentals.csv": "rentals",
    "payments.csv": "payments",
}

for csv_file, table_name in csv_table_map.items():
    csv_path = os.path.join("data", csv_file)
    print(f"Loading {csv_file} into {table_name}...")
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"✅ Loaded {len(df)} rows into {table_name}")
