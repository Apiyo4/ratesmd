from pymongo import MongoClient
from urllib.parse import quote_plus
# from fastapi.exceptions import HTTPException

# import pandas as pd
# import numpy as np

         
def fetch_data(page=None, limit=None):
    
    if page is not None and limit is not None:

        total_documents = ratemdDB.count_documents({})

        # Calculate skip and limit values for pagination
        skip = (page - 1) * limit

        # Fetch data from the collection with pagination
        data = list(ratemdDB.find().skip(skip).limit(limit))

        # if not data:
        #     raise HTTPException(status_code=404, detail="Data not found")

        # Calculate total pages based on the limit
        total_pages = (total_documents + limit - 1) // limit

        return {
            "data": data,
            "page": page,
            "limit": limit,
            "total_documents": total_documents,
            "total_pages": total_pages,
        }
    else:
        # Fetch 20 results if page and limit are not provided
        data = list(ratemdDB.find().limit(20))

        return {
            "data": data
        }

# connect to database 
user = "c1-ds4a-2-team-23"
password = "PhobRoswuBropRaKUM9R"
host = "20.232.135.212:27017"
uri = "mongodb://%s:%s@%s" % (
    quote_plus(user), quote_plus(password), host)
client = MongoClient(uri)

db = client['healthrate']

ratemdDB = db['ratemd']

# Invoke main function to save data to doctors_rating.csv
print(fetch_data())

