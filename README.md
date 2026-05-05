\# 🌦️ Weather Forecast \& Alert Application



!\[Python](https://img.shields.io/badge/Python-3.11-blue.svg)

!\[FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)

!\[Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)

!\[Status](https://img.shields.io/badge/Project-Completed-brightgreen.svg)



\---



\## 🚀 Project Overview



The \*\*Weather Forecast \& Alert Application\*\* is a Python-based real-time weather monitoring system that fetches weather data using APIs and generates intelligent alerts for extreme conditions like:



\- 🌧️ Rain Alerts  

\- 🔥 Heatwave Alerts  

\- 🌬️ Wind Alerts  

\- 🌫️ Humidity/Weather Condition Alerts  



It also includes a \*\*Streamlit dashboard\*\* for visualization and monitoring.



\---



\## 🎯 Problem Statement



People and industries often face difficulties in tracking sudden weather changes. This system solves that by:



\- Providing real-time weather updates  

\- Generating automated alerts  

\- Helping in decision-making for travel, farming, logistics, and events  



\---



\## 🏭 Industry Use Cases



\- 🚚 Logistics \& Transport Planning  

\- 🌾 Agriculture \& Farming  

\- 🎪 Event Management  

\- ✈️ Travel \& Aviation  

\- ⚡ Disaster Management  



\---



\## 🧠 Features



\- 🌍 Real-time weather data via API  

\- ⚠️ Automated alert generation system  

\- 📊 Streamlit dashboard visualization  

\- 📁 Clean report generation  

\- 🔄 Modular Python architecture  

\- 🧪 Simulation mode (without API dependency)  



\---



\## 🛠️ Tech Stack



\- Python 3.11  

\- FastAPI (Backend API)  

\- Streamlit (Dashboard UI)  

\- Requests (API calls)  

\- Pandas (data handling)  

\- JSON handling  

\- OpenWeatherMap / Open-Meteo API  



\---



\## 📂 Project Structure

Weather Forecast \& Alert Application/

│

├── src/ # Core logic (API + rules)

├── api/ # FastAPI backend

├── dashboard/ # Streamlit UI

├── jobs/ # Scheduler scripts

├── reports/ # Generated weather reports

├── images/ # Screenshots (IMPORTANT)

├── main.py # Entry point

├── requirements.txt # Dependencies

└── README.md



\---



\## ⚙️ How to Run Project



\### 1️⃣ Install dependencies

```bash

pip install -r requirements.txt

2️⃣ Start FastAPI backend

uvicorn api.app:app --reload

3️⃣ Start Streamlit dashboard

streamlit run dashboard/streamlit\_app.py

🔐 API Setup

Create .env file

API\_KEY=your\_api\_key\_here

Never upload .env to GitHub ❌

\#📸 Screenshots

\### 🏠 1. Streamlit Dashboard UI

> Main dashboard showing weather input, current conditions, and alerts.



!\[Dashboard UI](images/dashboard.png)



\---



\### 🌤️ 2. Weather API Output

> Raw or formatted weather data fetched from API.



!\[Weather Output](images/weather.png)



\---



\### ⚠️ 3. Alert System Output

> Automated alerts generated for rain, heatwave, wind, or humidity.



!\[ Temp Trend \& Alerts](images/temp\_trend\_alert.png)

!\[ Hour Data](images/hour\_data.png)



\---



📊 Sample Output

City: Delhi

Temperature: 34°C

Condition: Clear Sky

Alert: Heatwave Warning ⚠️

💡 Key Learnings

API integration in Python

FastAPI backend development

Real-time data processing

Alert rule engine design

Streamlit dashboard creation

Project structuring for GitHub

🚀 Future Improvements

SMS/Email alerts

Mobile app version

AI-based weather prediction

Map-based visualization

Multi-city tracking

👨‍💻 Author



Sanskritika Awasthi

