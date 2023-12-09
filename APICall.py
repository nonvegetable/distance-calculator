from opencage.geocoder import OpenCageGeocode

def api_call(place):
    key = 'f5ea0c6a6fbb4983ba6d89d226c82513'
    geocoder = OpenCageGeocode(key)

    query = place

    # No need to URI encode query, module does that for you
    results = geocoder.geocode(query)

    return results[0]['geometry']['lat'], results[0]['geometry']['lng']
