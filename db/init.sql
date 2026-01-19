CREATE TABLE fitness_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    steps INT NOT NULL,
    heart_rate INT NOT NULL,
    calories FLOAT NOT NULL,
    activity_type VARCHAR(20) NOT NULL
);
