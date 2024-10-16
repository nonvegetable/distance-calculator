from math import radians, sin, cos, sqrt, atan2

def calculate_distance(coord1, coord2, unit='km'):
    # Haversine formula
    R = 6371  # Radius of the Earth in kilometers

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    # Convert to requested unit
    if unit == 'mi':
        distance *= 0.621371
    elif unit == 'nm':
        distance *= 0.539957

    return distance

def get_unit_name(unit):
    unit_names = {
        'km': 'kilometers',
        'mi': 'miles',
        'nm': 'nautical miles'
    }
    return unit_names.get(unit, 'unknown units')