<div align="center">

# 🌦️ Weather

### Real-time weather. Clean interface. Detailed data.

A modern Flask-powered weather dashboard with current conditions, forecasts, air quality, weather alerts, and more — all in a polished responsive interface.

<br/>

<a href="https://weather-info-by-hidden-rhythm.vercel.app">
  <img src="https://img.shields.io/badge/🌐%20LIVE%20WEBSITE-weather--info--by--hidden--rhythm.vercel.app-111111?style=for-the-badge" alt="Live Website"/>
</a>
&nbsp;
<a href="./">
  <img src="https://img.shields.io/badge/💻%20SOURCE%20CODE-GitHub-24292f?style=for-the-badge&logo=github" alt="Source Code"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-2.3.3-000000?style=flat-square&logo=flask"/>
<img src="https://img.shields.io/badge/WeatherAPI-API-4A90E2?style=flat-square"/>
<img src="https://img.shields.io/badge/Status-Live-22C55E?style=flat-square"/>

</div>

---

## ✨ About

**Weather** is a real-time weather dashboard built with **Python + Flask** and powered by **WeatherAPI.com**.

It combines detailed weather information with a clean dark interface designed to make everything important visible at a glance.

### What you get

* 🌡️ Current temperature & conditions
* 🌤️ 5-day weather forecast
* 💧 Humidity & precipitation
* 💨 Wind information
* 🌫️ Visibility
* 🌡️ Heat index & wind chill
* 💦 Dew point & wet bulb temperature
* ☁️ Cloud coverage
* 🌧️ Rain probability
* 🧭 Atmospheric pressure
* 🌍 Air Quality Index
* 🧪 Individual pollutant levels
* ⚠️ Weather alerts
* 🔄 Automatic refresh
* 🌐 Metric / Imperial units
* 📱 Responsive mobile interface
* 🕘 Recent city searches

---

## 🖥️ Interface

The dashboard uses a modern dark UI with glassmorphism-inspired cards, subtle gradients, responsive layouts, and smooth animations.

The main dashboard includes:

| Section             | Data                                           |
| ------------------- | ---------------------------------------------- |
| **Current Weather** | Temperature, condition, feels-like, heat index |
| **Metrics**         | Humidity, wind, visibility                     |
| **Detailed**        | Wind chill, dew point, wet bulb                |
| **Atmospheric**     | Pressure, cloud cover, precipitation           |
| **Air Quality**     | US EPA, UK Defra, pollutants                   |
| **Alerts**          | Active weather warnings                        |
| **Forecast**        | 5-day forecast                                 |

---

## 🧱 Tech Stack

* **Python**
* **Flask**
* **Flask-CORS**
* **Requests**
* **WeatherAPI.com**
* **HTML / CSS / JavaScript**

---

## 📁 Project Structure

```text
Weather/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

---

## ⚙️ How It Works

```text
User
 │
 ▼
Weather Dashboard
 │
 │  City Search
 ▼
Flask API
 │
 ▼
WeatherAPI.com
 │
 ├── Current Weather
 ├── 5-Day Forecast
 ├── Air Quality
 └── Weather Alerts
 │
 ▼
Dashboard
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Hidden-Rhythm/Weather-info.git
cd Weather-info
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create an environment variable for your WeatherAPI key instead of keeping the key directly in source code.

Example:

```env
WEATHER_API_KEY=your_api_key_here
```

> **Security:** Never commit your real API key to GitHub. If an API key has previously been exposed in a public repository, rotate it.

### 4. Start the server

```bash
python app.py
```

The application will run locally on:

```text
http://localhost:5000
```

---

## 🔌 API Endpoint

The Flask backend exposes:

```text
GET /api/weather?city=<city>
```

Example:

```text
/api/weather?city=Gurgaon
```

The response contains:

* Current weather
* Forecast data
* Air quality information
* Weather alerts
* API/error status

---

## 🔄 Automatic Updates

The dashboard automatically refreshes weather information every **5 minutes**, while also providing a manual refresh button.

Recent searches are stored locally in the browser for quick access.

---

## 🌐 Live

<div align="center">

### Try it now

<a href="https://weather-info-by-hidden-rhythm.vercel.app">

**🌦️ Open Weather Dashboard →**

</a>

<br/><br/>

Built with Python, Flask & WeatherAPI.

**[@Hidden_Rhythm](https://github.com/Hidden-Rhythm)**

</div>
