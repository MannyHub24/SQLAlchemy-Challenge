
# Hawaii Climate Analysis and API

## 🌴 Project Overview

This project analyzes weather data for the island of Oahu, Hawaii. The data comes from a SQLite database of historical weather records. Using SQLAlchemy, I queried the database to explore precipitation, temperature, and station activity. Then, I built a simple Flask API so the data can be accessed through a web browser.

---

## 🔧 Technologies Used

- Python
- Jupyter Notebook
- SQLAlchemy (ORM)
- Flask (for the API)
- Pandas
- Matplotlib
- SQLite

---

## 📁 Files Included

- `hawaii.sqlite`: The climate database
- `climate_starter.ipynb`: Jupyter Notebook with my data analysis
- `app.py`: Flask app that returns the results of my queries as JSON
- `hawaii_measurements.csv` and `hawaii_stations.csv`: Raw data files (not used directly in this project but included for reference)

---

## 📊 Part 1: Climate Analysis (in Jupyter Notebook)

In the notebook, I:
- Connected to the SQLite database using SQLAlchemy
- Reflected the existing tables: `measurement` and `station`
- Queried the most recent 12 months of precipitation data and created a line plot
- Found the most active station and plotted a histogram of its temperature observations
- Printed summary statistics for both precipitation and temperature

---

## 🔥 Part 2: Flask API

I created routes using Flask that return JSON data from the queries I wrote. These routes include:

### Available Routes:
- `/` — Homepage with route listing
- `/api/v1.0/precipitation` — Precipitation data from the last 12 months
- `/api/v1.0/stations` — List of weather stations
- `/api/v1.0/tobs` — Temperature observations for the most active station over the last year
- `/api/v1.0/<start>` — Min, average, and max temperature from a given start date
- `/api/v1.0/<start>/<end>` — Same as above, but between a start and end date

---

## ▶️ How to Run It

### 1. Clone this repo
```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Run the Jupyter Notebook
Open `climate_starter.ipynb` and run each cell to see the climate analysis.

### 3. Run the Flask App
Make sure you're in the folder with `app.py`, then run:
```bash
flask run
```

Go to your browser and visit `http://127.0.0.1:5000/` to see the routes!

