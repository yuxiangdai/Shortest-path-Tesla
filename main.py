import json

with open('charging_stations.json') as data_file:    
    data = json.load(data_file)

#When it asks for input, paste this: 38.8977 -77.0365
coord_input = map(float,raw_input('Enter your input:').split())
print coord_input

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

# get lat,lon,city, station name, id number_of_results

number_of_results = data['total_results']
print "Number of Results: " + str(number_of_results)
num = 0

print data['fuel_stations'][336]['latitude']
print data['fuel_stations'][336]['longitude']



for i in range(number_of_results - 3, number_of_results - 1):
    print dist(coord_input[0], coord_input[1], data['fuel_stations'][i]['latitude'],data['fuel_stations'][i]['longitude'])
    
    ##currently prints distance, make it make some fancy dictionary!!
    

print num