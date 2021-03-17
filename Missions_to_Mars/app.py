import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
########################3engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
######### measurement = Base.classes.measurement
######### station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################




#FROM OLD HW

# @app.route("/")
# def home():
#     """List all available api routes."""
#     return (
#         f"<h3>For data add below paths to url:</h3>"
#         f"<ul><li>/api/v1.0/precipitation</li>"
#         f"<li>/api/v1.0/stations</li>"
#         f"<li>/api/v1.0/tobs</li>"
#         f"<li>/api/v1.0/<start>/<end></li>"
#         f"<li>/api/v1.0/<start></li></ul>"
#     )

# @app.route("/api/v1.0/precipitation")
# def prcp():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)
#     return { date: prcp for date, prcp in session.query(measurement.date, measurement.prcp).all() }
#     # results = session.query(measurement.date, measurement.prcp).all()
#     # res = {}
#     # for date, prcp in results:
#     #     res[date] = prcp
#     # return res 

# @app.route("/api/v1.0/stations")
# def get_stations():
#     session = Session(engine)
#     return { station: name for station, name in session.query(station.station, station.name).all() }


# @app.route("/api/v1.0/tobs")
# def get_tobs():
#     session = Session(engine)
#     return { measurement: tobs for measurement, tobs in session.query(measurement.date, measurement.station).all() }


# @app.route("/api/v1.0/<start>")
# @app.route("/api/v1.0/<end>")
# def start(start, end = '2017-08-23'):
#     session = Session(engine)
#     return { measurement: date for measurement, date in session.query(measurement.date, measurement.station).all() }



if __name__ == '__main__':
    app.run(debug=True)
