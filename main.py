# import urllib2
import json
# from pprint import pprint

with open('charging_stations.json') as data_file:    
    data = json.load(data_file)

coord_input = map(float,raw_input('Enter your input:').split())
print coord_input