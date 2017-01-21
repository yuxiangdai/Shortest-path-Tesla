def dist(lat1, lon1, lat2, lon2):
    import math
    R = 6371000.0
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    delta_lat = (lat2 - lat1)
    delta_lon = (lon2 - lon1)
    a = math.sin(delta_lat/2.0) * math.sin(delta_lat/2.0) +  math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon/2.0) * math.sin(delta_lon/2.0)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

