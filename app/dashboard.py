import streamlit as st
from db_connection import run_query
from queries import (
    REVENUE_BY_MONTH,
    TOP_CUSTOMERS,
    POPULAR_GENRES,
    TOTAL_CUSTOMERS,
    TOTAL_RENTALS,
    TOTAL_REVENUE
)
import pandas as pd

st.set_page_config(page_title="Movie Rental Dashboard", layout="wide")
st.title("🎬 Movie Rental Analytics Dashboard")

# --- 🔧 Top Filter ---
store_filter = st.selectbox("🏬 Filter by Store", ["All", "Store 1", "Store 2"])
store_id = 1 if store_filter == "Store 1" else 2 if store_filter == "Store 2" else None

# --- WHERE clause builder ---
conditions = []
if store_id:
    conditions.append(f"store_id = {store_id}")
where_clause = " AND ".join(conditions)
if where_clause:
    where_clause = "WHERE " + where_clause

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview", "📈 Revenue", "👥 Customers", "🎬 Genres", "🌎 More Insights"
])

# --- 📊 Overview Tab ---
with tab1:
    st.markdown("### 💡 Summary of Core Business KPIs")
    col1, col2, col3 = st.columns(3)

    revenue_query = f"""
    SELECT ROUND(SUM(amount)::numeric, 2) AS total_revenue
    FROM payments
    JOIN customers USING(customer_id)
    {where_clause}
    """
    revenue = run_query(revenue_query)['total_revenue'].iloc[0]
    col1.metric("💰 Total Revenue", f"${revenue:,.2f}" if pd.notna(revenue) else "$0.00")

    rentals = run_query(f"""
    SELECT COUNT(*) AS total_rentals
    FROM rentals
    JOIN customers USING(customer_id)
    {where_clause}
    """)['total_rentals'].iloc[0]
    col2.metric("🎬 Total Rentals", f"{rentals:,}" if pd.notna(rentals) else "0")

    customers_query = f"""
    SELECT COUNT(*) AS total_customers
    FROM customers
    {where_clause}
    AND active = 1
    """ if where_clause else "SELECT COUNT(*) AS total_customers FROM customers WHERE active = 1"
    customers = run_query(customers_query)['total_customers'].iloc[0]
    col3.metric("👥 Active Customers", f"{customers:,}" if pd.notna(customers) else "0")

# --- 📈 Revenue Tab ---
with tab2:
    st.markdown("### 📆 Revenue Trends Over Time")
    df = run_query(REVENUE_BY_MONTH)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    start_date, end_date = st.date_input("Select Date Range", [df['date'].min(), df['date'].max()])
    filtered = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

    st.line_chart(filtered.set_index('date'))

    if st.checkbox("🔍 Show Data Table - Revenue"):
        st.dataframe(filtered)

    st.download_button("⬇️ Download CSV", filtered.to_csv(index=False), file_name="revenue_filtered.csv")

    st.markdown("### 📈 Monthly Revenue Growth")
    df['month'] = df['date'].dt.to_period('M')
    monthly = df.groupby('month')['revenue'].sum().reset_index()
    monthly['pct_change'] = monthly['revenue'].pct_change().fillna(0)
    st.dataframe(monthly.rename(columns={'pct_change': 'MoM Growth'}))
    st.line_chart(monthly.set_index('month')['revenue'])

# --- 👥 Customers Tab ---
with tab3:
    st.markdown("### 💵 Top 10 Customers by Spending")
    df = run_query(TOP_CUSTOMERS)
    st.bar_chart(df.set_index('customer_name'))

    if st.checkbox("🔍 Show Data Table - Top Customers"):
        st.dataframe(df)

    st.download_button("⬇️ Download CSV", df.to_csv(index=False), file_name="top_customers.csv")

    st.markdown("### 🏪 Customers by Store")
    cust_by_store = run_query("""
    SELECT store_id, COUNT(*) AS customer_count
    FROM customers
    WHERE active = TRUE
    GROUP BY store_id
    """)
    st.bar_chart(cust_by_store.set_index('store_id'))

# --- 🎬 Genres Tab ---
with tab4:
    st.markdown("### 🎥 Top-Rented Movie Genres")
    df = run_query(POPULAR_GENRES)
    top_n = st.slider("🎚 Top N Genres", 3, 15, 10)
    st.bar_chart(df.head(top_n).set_index('genre'))

    if st.checkbox("🔍 Show Data Table - Genres"):
        st.dataframe(df.head(top_n))

    st.download_button("⬇️ Download CSV", df.to_csv(index=False), file_name="genres.csv")

# --- 🌎 More Insights Tab ---
with tab5:
    st.markdown("### 🧭 Other Operational Insights")

    st.subheader("🏙️ Revenue by Store")
    store_rev_df = run_query("""
    SELECT s.store_id, ROUND(SUM(p.amount)::numeric, 2) AS revenue
    FROM payments p
    JOIN customers c ON p.customer_id = c.customer_id
    JOIN stores s ON c.store_id = s.store_id
    GROUP BY s.store_id
    ORDER BY s.store_id
    """)
    st.bar_chart(store_rev_df.set_index('store_id'))

    st.subheader("📆 Average Daily Revenue")
    avg_df = run_query("""
    SELECT DATE(payment_date) AS day, SUM(amount) AS daily_total
    FROM payments
    GROUP BY day
    """)
    avg_revenue = avg_df['daily_total'].mean()
    st.metric("📅 Avg Daily Revenue", f"${avg_revenue:,.2f}")
    st.line_chart(avg_df.set_index('day'))

    st.subheader("⏳ Average Rental Duration")
    avg_duration = run_query("""
    SELECT ROUND(AVG(EXTRACT(EPOCH FROM return_date - rental_date) / 86400), 2) AS avg_days
    FROM rentals
    WHERE return_date IS NOT NULL
    """)['avg_days'].iloc[0]
    st.metric("⏳ Avg Duration", f"{avg_duration:.2f} days")

    st.subheader("🕓 Rentals by Hour")
    hour_df = run_query("""
    SELECT EXTRACT(HOUR FROM rental_date) AS hour, COUNT(*) AS rentals
    FROM rentals
    GROUP BY hour
    ORDER BY hour
    """)
    st.bar_chart(hour_df.set_index('hour'))

    st.subheader("📊 Revenue Histogram")
    hist_df = run_query("SELECT amount FROM payments")
    st.area_chart(hist_df['amount'].value_counts().sort_index())

# --- Footer ---
st.markdown("---")
st.caption("Built by Lexi Sierfeld · Powered by PostgreSQL, Python, and Streamlit · © 2025")
