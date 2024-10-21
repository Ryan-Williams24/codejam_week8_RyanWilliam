import matplotlib.pyplot as plt
import requests
import json

api_key = "2c06c1f2073a4acc85f225211242010"
cities = ["New York", "London", "Tokyo", "Sydney"] # Popular Cities To Track

all_weather_data = {}

for city in cities:
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    city_data = response.json()
    
    all_weather_data[city] = city_data  # Store Data For Each City

# Save Weather Data In Readable File
with open("weather_data.json", "w") as file:
    json.dump(all_weather_data, file, indent=4)

import json

# Load The Saved Weather Data
with open("weather_data.json", "r") as file:
    all_weather_data = json.load(file)

organized_data = {}

# Strip Data To Only Wanted Parts
for city, data in all_weather_data.items():
    if "current" in data:  
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]

        organized_data[city] = { 
            "temperature": temp,
            "humidity": humidity,
            "wind_speed": wind_speed
        }

# Save Organized Data
with open("organized_weather_data.json", "w") as file:
    json.dump(organized_data, file, indent=4)

import json

# Load Organized Data
with open("organized_weather_data.json", "r") as file:
    weather_data = json.load(file)

cities = list(weather_data.keys())
temperatures = [data["temperature"] for data in weather_data.values()]
humidities = [data["humidity"] for data in weather_data.values()]
wind_speeds = [data["wind_speed"] for data in weather_data.values()]

# Plot Temperature Data
plt.figure(figsize=(10, 5))
plt.bar(cities, temperatures, color='skyblue')
plt.title("Temperature Comparison (°C)")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.show()

# Plot Humidity Data
plt.figure(figsize=(10, 5))
plt.bar(cities, humidities, color='lightgreen')
plt.title("Humidity Comparison (%)")
plt.xlabel("City")
plt.ylabel("Humidity (%)")
plt.show()

# Plot Wind Speed Data
plt.figure(figsize=(10, 5))
plt.bar(cities, wind_speeds, color='lightcoral')
plt.title("Wind Speed Comparison (kph)")
plt.xlabel("City")
plt.ylabel("Wind Speed (kph)")
plt.show()