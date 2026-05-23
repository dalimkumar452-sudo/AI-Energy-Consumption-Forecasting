import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
import os

# 1. Generate Virtual Simulation Dataset
print("Generating synthetic energy data...")
# এখানে freq="H" এর জায়গায় freq="h" করা হয়েছে
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="h")
np.random.seed(42)

# Simulating human behavior: More energy in daytime, less at night, varied by weekends
energy = []
for d in dates:
    base = 100
    hour_factor = np.sin(d.hour * np.pi / 12) * 40  # Peak during day
    weekend_factor = -20 if d.dayofweek >= 5 else 10 # Less on weekends
    noise = np.random.normal(0, 10)
    energy.append(abs(base + hour_factor + weekend_factor + noise))

df = pd.DataFrame({'Datetime': dates, 'Energy': energy})
df['hour'] = df['Datetime'].dt.hour
df['day'] = df['Datetime'].dt.dayofweek
df['month'] = df['Datetime'].dt.month
df['is_weekend'] = df['day'].apply(lambda x: 1 if x >= 5 else 0)

# Save dataset
os.makedirs("data", exist_ok=True)
df.to_csv("data/energy_dataset.csv", index=False)

# 2. Train the Model
print("Training AI Model...")
X = df[['hour', 'day', 'month', 'is_weekend']]
y = df['Energy']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
print(f"Model Mean Absolute Error: {mae:.2f}")

# 3. Save the Model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/rf_model.pkl")
print("Model saved successfully in 'models/rf_model.pkl'")