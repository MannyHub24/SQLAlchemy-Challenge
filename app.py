# Import the dependencies.

from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table

Measurement_ref = Base.classes.measurement

Station_ref = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

hawaii_flask_api = Flask(__name__)




#################################################
# Flask Routes
#################################################

#Home page route
@hawaii_flask_api.route("/")
def home():
    return (
        f"Welcome to the Hawaii Weather API!<br/>"
        f"Here we'll present you with some weather data from Hawaii over the past 12 months!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Precipitation route
# shows precipitation data for the last year
# Returns a JSON list of dictionaries containing date and precipitation data

@hawaii_flask_api.route("/api/v1.0/precipitation")

def precipitation():
    session = Session(engine)
    ending_date = dt.datetime(2017, 8, 23)
    one_year_ago = ending_date - dt.timedelta(days=365)

    precipitation_results = session.query(Measurement_ref.date, Measurement_ref.prcp).\
    filter(Measurement_ref.date >= one_year_ago).all()

    session.close()

    precipitation_data = []
    for date, prcp in precipitation_results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_data.append(precipitation_dict)

        return jsonify(precipitation_data)


# Stations route
# Returns a JSON list of stations from the dataset

@hawaii_flask_api.route("/api/v1.0/stations")

def stations():
    session = Session(engine)
    total_stations = session.query(Station_ref.station).all()
    
    session.close()
    
    stations_list = [station[0] for station in total_stations]
    return jsonify(stations_list)


# Temperature Observations route
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.

@hawaii_flask_api.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    ending_date = dt.datetime(2017, 8, 23)
    one_year_ago = ending_date - dt.timedelta(days=365)
    most_active_previous_year = session.query(Measurement_ref.tobs).\
    filter(Measurement_ref.station == "USC00519281")\
    .filter(Measurement_ref.date>= one_year_ago).all()

    session.close()

    temperatures = [temperature[0] for temperature in most_active_previous_year]
    return jsonify(temperatures)


# Start only route
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature
# for a specified start or start-end range.
# We use the most active station USC00519281 for this query.
# Please note that the start date should be in the format YYYY-MM-DD.

@hawaii_flask_api.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    query_start = session.query(func.min(Measurement_ref.tobs),
    func.avg(Measurement_ref.tobs),
    func.mac(Measurement_ref.tobs)).filter(Measurement_ref.date >= start).all()
    
    session.close()

    query_temperature_start = list(query_start[0])
    return jsonify(query_temperature_start)


# Start and end route
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature
# for a specified start or start-end range.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@hawaii_flask_api.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    query_start_end = session.query(func.min(Measurement_ref.tobs),
    func.avg(Measurement_ref.tobs),
    func.mac(Measurement_ref.tobs)).filter(Measurement_ref.date >= start)\
    .filter(Measurement_ref.date <= end).all()
    
    session.close()

    query_temperature_start_end = list(query_start_end[0])
    return jsonify(query_temperature_start_end)


# Run the Flask app
if __name__ == "__main__":
    app.run(deebug = True) 