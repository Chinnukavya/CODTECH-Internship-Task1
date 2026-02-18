import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "d14aa832bff2a5c025dcec9e8aaae4b8"
city = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Check if API returned error
if data.get("cod") != "200":
    print("Error from API:", data)
    exit()

dates = []
temperatures = []
humidity = []

for item in data['list']:
    dates.append(item['dt_txt'])
    temperatures.append(item['main']['temp'])
    humidity.append(item['main']['humidity'])

df = pd.DataFrame({
    "Date": dates,
    "Temperature (°C)": temperatures,
    "Humidity (%)": humidity
})

plt.figure(figsize=(12,6))
sns.lineplot(x="Date", y="Temperature (°C)", data=df)
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {city}")
plt.tight_layout()
plt.show()