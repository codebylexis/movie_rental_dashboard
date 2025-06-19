# 🎬 ReelTime Rentals – 2024 Analytics Dashboard

An interactive data analytics dashboard built using **Streamlit**, **PostgreSQL**, and **Python** to visualize business performance for a fictional company, **ReelTime Rentals**, using 2024 data.

> 💡 Great for showcasing full-stack data skills — from schema design and data generation to SQL querying, visualization, and cloud deployment.

---

## 🌟 Features

- 📊 KPI summary cards (revenue, rentals, active customers)
- 📈 Revenue trends with interactive date filtering
- 👥 Top customers + customer count per store
- 🎬 Genre insights with adjustable top-N filtering
- 📅 Rental heatmap by hour
- ⏳ Avg. rental duration + daily revenue
- 🔽 Downloadable CSV exports
- 🎛️ Store-level filtering (e.g. ReelTime East vs. West)

---

## 🚀 Live Demo

📌 **App:** [https://reeltime-rentals-2024-analytics.streamlit.app](https://reeltime-rentals-2024-analytics.streamlit.app)  
📁 **Code:** [https://github.com/codebylexis/movie_rental_dashboard](https://github.com/codebylexis/movie_rental_dashboard)

---

## 📦 Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend/DB:** PostgreSQL (hosted on Neon)  
- **Data Source:** Synthetic data generated with Faker  
- **Python Libraries:** `pandas`, `streamlit`, `sqlalchemy`, `faker`

---

## 📁 Project Structure

```text
movie_rental_dashboard/
│
├── app/
│   ├── dashboard.py           # Main Streamlit app
│   ├── db_connection.py       # PostgreSQL connection via SQLAlchemy
│   ├── queries.py             # SQL query templates
│   └── test_connection.py     # (Optional) connection check
│
├── data/
│   ├── customers.csv
│   ├── stores.csv
│   ├── payments.csv
│   ├── films.csv
│   ├── rentals.csv
│   └── genres.csv
│
├── generate_fake_movie_data.py
├── requirements.txt
├── .gitignore
└── README.md
