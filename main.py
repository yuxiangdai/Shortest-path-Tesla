import json

with open('charging_stations.json') as data_file:    
    data = json.load(data_file)

#When it asks for input, paste this: 38.8977 -77.0365
coord_input = input('Enter your input:').split()
coord_input = (float(coord_input[0]), float(coord_input[1]))
print(coord_input)

def dist(lat1, lon1, lat2, lon2):
    import math
    R = 6371000.0000
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    delta_lat = (lat2 - lat1)
    delta_lon = (lon2 - lon1)
    a = math.sin(delta_lat/2.0) * math.sin(delta_lat/2.0) +  math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon/2.0) * math.sin(delta_lon/2.0)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d/1000.0

def get_sort_keys_by_spherical_dist(lat, lon, sta_info):
    keys = []
    for key in sta_info:
        keys.append(key)
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            t_dist_i = dist(sta_info[keys[i]]['latitude'], sta_info[keys[i]]['longitude'], lat, lon)
            t_dist_j = dist(sta_info[keys[j]]['latitude'], sta_info[keys[j]]['longitude'], lat, lon)
            if t_dist_i > t_dist_j:
                keys[i], keys[j] = keys[j], keys[i]
    return keys

def print_top_3(lat, lon, sta_info):
    keys = get_sort_keys_by_spherical_dist(lat, lon, sta_info)
    #39.0250017 -77.148335 Westfield Montgomery Mall - Tesla 17.137
    for i in range(3):
        print(str(sta_info[keys[i]]['latitude']) + " " + str(sta_info[keys[i]]['longitude']) + " " + sta_info[keys[i]]['station_name'] + " " + "%.3f" % dist(sta_info[keys[i]]['latitude'], sta_info[keys[i]]['longitude'], lat, lon))
    
# get lat,lon,city, station name, id number_of_results

number_of_results = data['total_results']

sta_info = {}

for i in range(number_of_results):
    sta_temp = {}
    sta_temp["latitude"] = data['fuel_stations'][i]['latitude']
    sta_temp["longitude"] = data['fuel_stations'][i]['longitude']
    sta_temp["station_name"] = data['fuel_stations'][i]['station_name']
    sta_temp["city"] = data['fuel_stations'][i]['city']
    sta_info[data['fuel_stations'][i]['id']] = sta_temp
    

print_top_3(coord_input[0], coord_input[1], sta_info)
