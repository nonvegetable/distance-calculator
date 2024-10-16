from json import load
from opencage.geocoder import OpenCageGeocode
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def api_call(place):
    key = os.getenv("YOUR_API_KEY")
    geocoder = OpenCageGeocode(key)

    query = place

    # No need to URI encode query, module does that for you
    results = geocoder.geocode(query)

    return results[0]['geometry']['lat'], results[0]['geometry']['lng']
