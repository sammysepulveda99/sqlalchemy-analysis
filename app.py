#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
import numpy as np
import pandas as pd
from datetime import timedelta


# In[13]:


#Create to engine to connect to sqlite database
engine  = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[14]:


#Reflect tables into classes and save into classes called station and measurement
Base = automap_base()
Base.prepare(engine, reflect = True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


# In[ ]:


#Creaing Flask App to reflect
app = Flask(__name__)
#Homepage
@app.route("/")
#lsting routes available
def Home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
#Returning the JSON representation of our dictionary
        f"/api/v1.0/stations<br/>"
#Returing a JSON list of stations from the dataset
        f"/api/v1.0/tobs<br/>"
#Returning a JSON list of observations for the previous year
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def percipitation():

    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    first_date = last_date - timedelta(days = 365)
    prcp_results = (session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= first_date).order_by(Measurement.date).all())
    return jsonify(prcp_results)

@app.route("/api/v1.0/stations")
def stations():
  session  = Session(engine)
  stations_results = session.query(Station.station, Station.name).all()
  return jsonify(stations_results)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    first_date = last_date - timedelta(days = 365)
    station_counts = (session.query(Measurement.station, func.count).filter(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    top_sation = (station_counts[0])
    top_station = (top_station[0])
    #Calculating the min, max, and average temperature
    session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).    filter(Measurement.station == top_station).all()
    top_station_year_obs = session.query(Measurement.tobs).    filter(Measurement.station == top_station).filter(Measurement.date >= first_date).all()
    return jsonify(top_station_year_obs)
#Making sure data is all date inclusive
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def start(start = 0, end = 1000):
    session = Session(engine)

    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)        

    results = session.query(*sel).        filter(Measurement.date >= start).        filter(Measurement.date <= end).all()
  
    return jsonify(results)


if __name__ == '__main__':
    app.run()


# In[ ]:




