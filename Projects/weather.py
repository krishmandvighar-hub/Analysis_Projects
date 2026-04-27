
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os


# 🔹 Step 1: API Key
API_KEY = "adfe2db78e83534547503cc43e4839a4"

# 🔹 Step 2: User input
city = input("Enter city name: ")


# 🔹 Step 3: API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# 🔹 Step 4: Fetch data
response = requests.get(url)
data = response.json()

# 🔹 Step 5: Error handling
if data["cod"] != 200:
    print("Error:", data["message"])
    exit()

# 🔹 Step 6: Extract data
temperature = data['main']['temp']
humidity = data['main']['humidity']
condition = data['weather'][0]['description']

# 🔹 Step 7: Date & time
now = datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

# 🔹 Step 8: Print output
print("\n--- Weather Data ---")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Condition:", condition)
print("Date & Time:", date_time)

# 🔹 Step 9: Save to CSV
file_name = "weather_data.csv"

new_data = pd.DataFrame([{
    "City": city,
    "Temperature": temperature,
    "Humidity": humidity,
    "Condition": condition,
    "DateTime": date_time
}])

# Append without duplicate header
if not os.path.isfile(file_name):
    new_data.to_csv(file_name, index=False)
else:
    new_data.to_csv(file_name, mode='a', header=False, index=False)

print("\nData saved to weather_data.csv ✅")

# 🔹 Step 10: Visualization
df = pd.read_csv(file_name)

plt.figure()
plt.plot(df['Temperature'])
plt.title("Temperature Trend")
plt.xlabel("Records")
plt.ylabel("Temperature (°C)")
plt.show()
