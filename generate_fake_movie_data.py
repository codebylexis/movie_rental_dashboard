import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Config
NUM_STORES = 2
NUM_GENRES = 8
NUM_FILMS = 100
NUM_CUSTOMERS = 500
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

# 1. Stores
stores = pd.DataFrame({
    'store_id': [1, 2],
    'city': ['New York', 'Los Angeles']
})

# 2. Genres
genre_list = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance', 'Thriller', 'Animation']
genres = pd.DataFrame({
    'genre_id': range(1, NUM_GENRES + 1),
    'genre_name': genre_list
})

# 3. Films
films = pd.DataFrame({
    'film_id': range(1, NUM_FILMS + 1),
    'title': [fake.sentence(nb_words=3).replace('.', '') for _ in range(NUM_FILMS)],
    'genre_id': [random.randint(1, NUM_GENRES) for _ in range(NUM_FILMS)]
})

# 4. Customers
customers = pd.DataFrame({
    'customer_id': range(1, NUM_CUSTOMERS + 1),
    'first_name': [fake.first_name() for _ in range(NUM_CUSTOMERS)],
    'last_name': [fake.last_name() for _ in range(NUM_CUSTOMERS)],
    'email': [fake.email() for _ in range(NUM_CUSTOMERS)],
    'store_id': [random.choice([1, 2]) for _ in range(NUM_CUSTOMERS)],
    'active': [1 for _ in range(NUM_CUSTOMERS)]
})

# 5. Rentals
def generate_rentals(num_rentals):
    rentals = []
    for i in range(1, num_rentals + 1):
        rental_date = fake.date_time_between(start_date=START_DATE, end_date=END_DATE)
        customer_id = random.randint(1, NUM_CUSTOMERS)
        film_id = random.randint(1, NUM_FILMS)
        return_date = rental_date + timedelta(days=random.randint(1, 5))
        rentals.append((i, rental_date, return_date, film_id, customer_id))
    return pd.DataFrame(rentals, columns=['rental_id', 'rental_date', 'return_date', 'film_id', 'customer_id'])

rentals = generate_rentals(80000)

# 6. Payments
payments = rentals.copy()
payments['payment_id'] = payments['rental_id']
payments['amount'] = [round(random.uniform(2.99, 6.99), 2) for _ in range(len(payments))]
payments['payment_date'] = payments['rental_date']
payments = payments[['payment_id', 'customer_id', 'amount', 'payment_date']]

# --- Save to CSVs (or ready for DB load) ---
stores.to_csv('stores.csv', index=False)
genres.to_csv('genres.csv', index=False)
films.to_csv('films.csv', index=False)
customers.to_csv('customers.csv', index=False)
rentals.to_csv('rentals.csv', index=False)
payments.to_csv('payments.csv', index=False)

print("✅ Fake data generated and saved to CSV files.")
