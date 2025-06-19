from app.db_connection import run_query
from app.queries import REVENUE_BY_MONTH  # Try TOP_CUSTOMERS or POPULAR_GENRES too

df = run_query(REVENUE_BY_MONTH)
print(df)
