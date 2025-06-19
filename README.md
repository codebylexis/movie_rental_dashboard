# 🎬 Movie Rental Analytics Dashboard

An interactive data analytics dashboard built using **Streamlit**, **MySQL**, and **Python** to visualize business performance for a fictional company, **ReelTime Rentals**, using 2024 data.

> 💡 Great for showcasing full-stack data skills — from database design and data generation to SQL querying, visualization, and interactive deployment.

---

## 🌟 Features

- 📊 KPI summary cards (revenue, rentals, customers)
- 📈 Revenue charts with time-based filtering
- 👥 Top customers and customers by store
- 🎬 Genre insights with dynamic top-N filtering
- 📅 Rental heatmap by hour of day
- ⏳ Average rental duration + daily revenue
- 🔽 Downloadable CSV exports
- 🎛️ Store-level filtering (e.g. ReelTime East vs. West)

---

## 🚀 Live Demo

📌 **App:** [https://movie-rental-dashboard.streamlit.app](https://movie-rental-dashboard.streamlit.app)  
📁 **Code:** [https://github.com/codebylexis/movie_rental_dashboard](https://github.com/codebylexis/movie_rental_dashboard)

---

## 📦 Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend/DB:** MySQL 8+  
- **Data Source:** Synthetic (Faker)  
- **Python Libraries:** `pandas`, `streamlit`, `mysql-connector-python`, `faker`

---

## 📁 Project Structure

```text
movie_rental_dashboard/
│
├── app/
│   ├── dashboard.py           # Main Streamlit app
│   ├── db_connection.py       # MySQL connector logic
│   ├── queries.py             # SQL templates for reuse
│   └── test_connection.py     # (Optional) test script
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
```

---

## 💻 Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/codebylexis/movie_rental_dashboard.git
cd movie_rental_dashboard
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create a MySQL database

```sql
CREATE DATABASE rental_2024;
```

### 4. Generate and load fake data

```bash
python generate_fake_movie_data.py
```

### 5. Run the dashboard

```bash
streamlit run app/dashboard.py
```

---

## ☁️ Deploying to Streamlit Cloud

1. Push to GitHub  
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)  
3. Click **"New app"**  
4. Choose your repo and branch  
5. Set main file path: `app/dashboard.py`  
6. Click **Deploy** 🎉

---

## 📬 Contact

Made with ❤️ by **Lexi Sierfeld**  
📫 sierfeld@sas.upenn.edu  
🌐 [https://lexisierfeld.dev](https://lexisierfeld.dev)
