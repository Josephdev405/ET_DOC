# imports. These are connections to external libraries that contain more code than Python has by default

import os
from pymongo import MongoClient
import requests
import json
from datetime import datetime
from datetime import date
from datetime import timedelta


#### CONNECT TO MONGODB CONNECTION STRING AND OPENET API KEY: ####

# ET Connection
OPEN_ET_API_KEY = os.environ.get("OPEN_ET_KEY") # gets secret api key from the environment which is
						# injected in there by the yml file from Github Secrets
# MongoDB Connection
connection_string = os.environ.get("MDB_STRING")



#### TIMING (The most recent that OpenET data gets is from four days ago)  ####
today = datetime.today()
end_date = today - timedelta(days=4)
two_weeks = today - timedelta(days=18)









# your coordinates here. Delete the comments # and insert code that looks like this

# replace myCoordinateDictionary with the name of your site, and any time myCoordinateDictionary appears
# replace that name with the new name.

# myCoordinateDictionary = {			
# "site_id":"NAME_OF_YOUR_LOCATION"
# "longitude": LONGITUDE_OF_YOUR_LOCATION_IN_DECIMAL_DEGREES_NO_QUOTATION_MARKS!
# "latitude": LATITUDE_OF_YOUR_LOCATION_IN_DECIMAL_DEGREES_NO_QUOTATION_MARKS!
# }





                   
#### setting up MongoDB  ####

# client
client = MongoClient(connection_string)

# setting up databases and collections
databases = client.list_database_names() # lists databases in the client cluster
working_database = client["NAME_OF_YOUR_DATABASE"] # sets the database I will be working on to my experiment database
openet_collection = working_database["NAME_OF_YOUR_ET_COLLECTION"]
# collections_list = working_database.list_collection_names()  # lists the collections within my db
# print(collections_list) # prints




    
#####################################################################      OPEN ET         #############################################################
# set your API key before making the request
header = {"Authorization": OPEN_ET_API_KEY}




# endpoint arguments
args = {
"date_range": [
    two_weeks.date().isoformat(), # uses input from user
    end_date.date().isoformat()
],
"interval": "daily", # uses input from user
"geometry": [
    myCoordinateDictionary["longitude"], # SUPER IMPORTANT LONGITUDE, YES LONGITUDE, GOES FIRST THEN LATITUDE this is because computers use x then y, whereas lat then long is acutally y and x
    myCoordinateDictionary["latitude"]  # 
], # input can be made for these, but most of this is standard and good already
"model": "Ensemble",
"variable": "ET",
"reference_et": "gridMET",
"units": "mm",
"file_format": "JSON"
}

# query the api 
resp = requests.post(
    headers=header,
    json=args,
    url="https://openet-api.org/raster/timeseries/point"
)

data = resp.json()
print(resp.status_code)




# put this in your code right after the end of your request to openET (probably after data = resp.json() )
# response code error handling
# THIS CODE TELLS YOU WHAT WENT WRONG IF SOMETHING DID

# if something went wrong:
if resp.status_code != 200:
    print("REQUEST FAILURE!")
    print(json.dumps(data, indent=4))
    error_collection.insert_one({
        
            "time":datetime.now(),
            "response":data,
            "Payload":args,
            "status":resp.status_code

        
    })

# if there is no data available (i.e. no cloud free data)
if not isinstance(data, list):
    print("Unexpected response, invalid input or zero cloud free rasters avaiable")
    print(json.dumps(data, indent=4))
    quit()

# No data error handling
if len(data) == 0:
    print("NO DATA AVAILABLE")






# update and insert to mongo db
for record in data:

    timestamp = datetime.strptime(
        record["time"],
        "%Y-%m-%d"
    )

    document = {

        "timestamp": timestamp,

        "metadata": {
            "site_id": myCoordinateDictionary["site_id"],
            "latitude": myCoordinateDictionary["latitude"],
            "longitude": myCoordinateDictionary["longitude"]
        },

        "et_mm": record["et"]

    }

    openet_collection.update_one(

        #FILTER
        {
            "timestamp": timestamp,
            "metadata.site_id": myCoordinateDictionary["site_id"]
        },

        # UPDATE
        {
            "$set": document
        },

        # INSERT IF NOT FOUND
        upsert=True
    )




print("data synchronized")



for doc in openet_collection.find():
    print(doc)




