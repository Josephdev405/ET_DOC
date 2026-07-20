# imports. These are connections to external libraries that contain more code than Python has by default
import requests
import os
import time
from dotenv import load_dotenv
from pymongo import MongoClient


#### LOAD YOUR CREDENTIALS ####

# This reads your API keys and MongoDB connection string from a .env file on your server
# You will need to create a .env file with the following three variables (see documentation for instructions)
load_dotenv()

# REPLACE THE VARIABLE NAMES BELOW ONLY IF YOU NAMED THEM DIFFERENTLY IN YOUR .env FILE
api_key = os.getenv("AMBIENT_API_KEY")
app_key = os.getenv("AMBIENT_APPLICATION_KEY")
mongo_uri = os.getenv("MONGODB_URI")

# these will stop the script and tell you exactly which key is missing if something is wrong
if not api_key:
    raise ValueError("AMBIENT_API_KEY missing in environment variables")
if not app_key:
    raise ValueError("AMBIENT_APPLICATION_KEY missing in environment variables")
if not mongo_uri:
    raise ValueError("MONGODB_URI missing in environment variables")


#### CONNECT TO MONGODB ####

client = MongoClient(mongo_uri)

try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")

# REPLACE "SCARECRO" WITH THE NAME OF YOUR DATABASE
database = client["SCARECRO"]

# REPLACE THESE COLLECTION NAMES IF YOU NAMED YOURS DIFFERENTLY
weather_station = database["WEATHER_STATION"]
air_quality_collection = database["AIR_QUALITY"]
leaf_collection = database["LEAF_WETNESS"]


#### FETCH DATA FROM AMBIENT WEATHER ####

# this calls the Ambient Weather API and gets the latest readings from your station
response = requests.get(
    url="https://rt.ambientweather.net/v1/devices",
    params={
        "applicationKey": app_key,
        "apiKey": api_key,
    }
)

# required pause so we don't exceed the API rate limit
time.sleep(1)

print(response.status_code)
data = response.json()

# NOTE: data[0] assumes you have one weather station. If you have multiple stations,
# this will only pull data from the first one in your account
record = data[0]["lastData"]
record["macAddress"] = data[0]["macAddress"]

print(record)


#### SEPARATE DATA INTO THREE COLLECTIONS ####

# leaf wetness sensor readings
leaf_record = {
    "leafwetness1": record["leafwetness1"],
    "batt_lw1": record["batt_lw1"],
    "macAddress": record["macAddress"],
    "date": record["date"]
}

# air quality sensor readings
air_quality_record = {
    "aqi_pm25": record["aqi_pm25"],
    "aqi_pm25_24h": record["aqi_pm25_24h"],
    "pm25": record["pm25"],
    "pm25_24h": record["pm25_24h"],
    "batt_25": record["batt_25"],
    "macAddress": record["macAddress"],
    "date": record["date"],
}

# all remaining weather station readings (temperature, humidity, wind, pressure, etc.)
weather_record = dict(record)
weather_record.pop("leafwetness1")
weather_record.pop("batt_lw1")
weather_record.pop("pm25")
weather_record.pop("pm25_24h")
weather_record.pop("aqi_pm25")
weather_record.pop("aqi_pm25_24h")
weather_record.pop("batt_25")


#### SAVE TO MONGODB ####

# upsert=True means it will insert new data or update existing — no duplicates
leaf_collection.update_one(
    {"macAddress": record["macAddress"], "date": record["date"]},
    {"$set": leaf_record},
    upsert=True
)

air_quality_collection.update_one(
    {"macAddress": record["macAddress"], "date": record["date"]},
    {"$set": air_quality_record},
    upsert=True
)

weather_station.update_one(
    {"macAddress": record["macAddress"], "date": record["date"]},
    {"$set": weather_record},
    upsert=True
)

print("Data synchronized successfully")
