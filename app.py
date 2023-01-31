from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from queries import fetch_date_range, fetch_latest_records_per_state
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = 'Content-Type'

connection = psycopg2.connect(os.getenv('POSTGRES_URL'))

@app.route("/")
def hello_world():
  return "<p>I am working :)</p>"

# Receives a state, month (1-12) and a year.
@app.route("/vaccinations/daily")
@cross_origin()
def vaccinations_daily():
  start_date = request.args.get("start_date")
  end_date = request.args.get("end_date")
  return jsonify(fetch_date_range(connection, "New York State", start_date, end_date))

@app.route("/vaccinations/by-state")
@cross_origin()
def vaccinations_by_state():
  return jsonify(fetch_latest_records_per_state(connection))
