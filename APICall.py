from opencage.geocoder import OpenCageGeocode

def api_call(place):
    key = 'YOUR-API-KEY'
    geocoder = OpenCageGeocode(key)

    query = place

    # No need to URI encode query, module does that for you
    results = geocoder.geocode(query)

    return results[0]['geometry']['lat'], results[0]['geometry']['lng']
