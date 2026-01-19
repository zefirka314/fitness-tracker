import time
import random
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="fitness-db",
    database="fitness",
    user="user",
    password="password"
)
cursor = conn.cursor()

activities = ["rest", "walk", "run"]
def generate_data(steps, calories):
    activity = random.choice(activities)
    if activity == "rest":
        heart_rate = random.randint(55, 70)
        calories+=random.uniform(0.5, 1.5)
    elif activity == "walk":
        steps+=random.randint(20, 60)
        heart_rate=random.randint(80, 100)
        calories+=random.uniform(3, 6)
    else:
        steps+=random.randint(80, 150)
        heart_rate=random.randint(120, 160)
        calories+=random.uniform(8, 15)

    cursor.execute(
        """
        INSERT INTO fitness_data (timestamp, steps, heart_rate, calories, activity_type)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (datetime.now(), steps, heart_rate, calories, activity)
    )
    conn.commit()
    return steps, calories
steps=0
calories=0
while True:
    steps, calories=generate_data(steps, calories)
    time.sleep(1)
