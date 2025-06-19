# 🎬 Movie Rental Analytics Dashboard

An interactive data analytics dashboard built using **Streamlit**, **MySQL**, and **Python** to visualize business performance for a fictional movie rental company with data from 2024.

> 💡 This project is ideal for showcasing full-stack data skills — from database design and data generation to query building, visualization, and interactive deployment.

---

## 🌟 Features

- 📊 KPI summary cards (revenue, rentals, customers)
- 📈 Revenue charts with time-based filtering
- 👥 Top customers and customers by store
- 🎬 Genre insights with dynamic top-N filtering
- 📅 Rental heatmap by hour of day
- ⏳ Average rental duration + daily revenue
- 🔽 Download CSV exports
- 🎛️ Store filter

---

## 🚀 Live Demo

📌 **Live App:** [https://movie-rental-dashboard.streamlit.app](https://movie-rental-dashboard.streamlit.app)

📁 **GitHub Repo:** [https://github.com/yourusername/movie-rental-dashboard](https://github.com/yourusername/movie-rental-dashboard)

---

## 📸 Preview

![Dashboard Screenshot](preview.png) <!-- Optional: Add preview.png to your repo -->

---

## 📦 Tech Stack

- **Frontend/UI:** Streamlit
- **Backend/DB:** MySQL 8+
- **Data Source:** Synthetic data (generated using Faker)
- **Python Libraries:** pandas, streamlit, mysql-connector-python, faker

---

## 📁 Project Structure

```
movie_rental_dashboard/
│
├── app/
│   ├── dashboard.py           # Streamlit app
│   ├── db_connection.py       # MySQL connector
│   ├── queries.py             # Reusable SQL templates
│   └── test_connection.py     # Optional connection test
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

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/movie-rental-dashboard.git
cd movie-rental-dashboard
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create database in MySQL

```sql
CREATE DATABASE rental_2024;
```

### 4. Generate and load data

```bash
python generate_fake_movie_data.py
```

### 5. Run the dashboard

```bash
streamlit run app/dashboard.py
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to: https://streamlit.io/cloud
3. Click **"New app"**
4. Choose your repo + branch
5. Set **Main file path** to: `app/dashboard.py`
6. Click **Deploy** 🎉

---

## 📬 Contact

Made with ❤️ by **[Lexi Sierfeld]**  
📫 [sierfeld@sas.upenn.edu]  
🌐 [lexisierfeld.dev]

---
