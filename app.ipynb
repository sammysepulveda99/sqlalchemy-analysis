{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import dependencies\n",
    "from flask import Flask, jsonify\n",
    "import sqlalchemy\n",
    "from sqlalchemy import create_engine, func\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from datetime import timedelta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create to engine to connect to sqlite database\n",
    "engine  = create_engine(\"sqlite:///Resources/hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reflect tables into classes and save into classes called station and measurement\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect = True)\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "#Creaing Flask App to reflect\n",
    "app = Flask(__name__)\n",
    "#Homepage\n",
    "@app.route(\"/\")\n",
    "#lsting routes available\n",
    "def Home():\n",
    "    return (\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "#Returning the JSON representation of our dictionary\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "#Returing a JSON list of stations from the dataset\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "#Returning a JSON list of observations for the previous year\n",
    "        f\"/api/v1.0/temp/start/end\"\n",
    "    )\n",
    "\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def percipitation():\n",
    "\n",
    "    session = Session(engine)\n",
    "    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date\n",
    "    last_date = dt.datetime.strptime(last_date, \"%Y-%m-%d\")\n",
    "    first_date = last_date - timedelta(days = 365)\n",
    "    prcp_results = (session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= first_date).order_by(Measurement.date).all())\n",
    "    return jsonify(prcp_results)\n",
    "\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "  session  = Session(engine)\n",
    "  stations_results = session.query(Station.station, Station.name).all()\n",
    "  return jsonify(stations_results)\n",
    "\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    session = Session(engine)\n",
    "    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date\n",
    "    last_date = dt.datetime.strptime(last_date, \"%Y-%m-%d\")\n",
    "    first_date = last_date - timedelta(days = 365)\n",
    "    station_counts = (session.query(Measurement.station, func.count).filter(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()\n",
    "    top_sation = (station_counts[0])\n",
    "    top_station = (top_station[0])\n",
    "    #Calculating the min, max, and average temperature\n",
    "    session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\\\n",
    "    filter(Measurement.station == top_station).all()\n",
    "    top_station_year_obs = session.query(Measurement.tobs).\\\n",
    "    filter(Measurement.station == top_station).filter(Measurement.date >= first_date).all()\n",
    "    return jsonify(top_station_year_obs)\n",
    "#Making sure data is all date inclusive\n",
    "@app.route(\"/api/v1.0/temp/<start>\")\n",
    "@app.route(\"/api/v1.0/temp/<start>/<end>\")\n",
    "def start(start = 0, end = 1000):\n",
    "    session = Session(engine)\n",
    "\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "\n",
    "    if not end:\n",
    "        results = session.query(*sel).\\\n",
    "            filter(Measurement.date >= start).all()\n",
    "        temps = list(np.ravel(results))\n",
    "        return jsonify(temps)        \n",
    "\n",
    "    results = session.query(*sel).\\\n",
    "        filter(Measurement.date >= start).\\\n",
    "        filter(Measurement.date <= end).all()\n",
    "  \n",
    "    return jsonify(results)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
