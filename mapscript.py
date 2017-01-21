import folium

# Array of latitudes and longitudes found by the path-finding algorithm
# Sample data:
# 37.773972 -122.431297 Start 0
# 39.3272037 -120.2064298 Truckee 63115
testarr = [{'lat':37.773972,'lon':-122.431297,'city':'Start','id':0},{'lat':39.3272037,'lon':-120.2064298,'city':'Truckee','id':63115}]


# Initialize map
map = folium.Map(location=[testarr[0]['lat'], testarr[0]['lon']], zoom_start=8)


       
def color(item):
    ## Define color of marker based on if it is a Start point
    ## Return the color of the marker
    ## Input: item is a dictionary containing the latitude, longitude, and City name of an array
    ## Output: color in format "color" (string) 
    if item['city'] == 'Start':
        col='green'
    else:
        col='red'
    return col


for item in testarr:
    # Add markers to map based on items in array
    map.add_child(folium.Marker(location=[item['lat'],item['lon']],popup=item['city'], icon=folium.Icon(color=color(item),icon_color='white')))

# Map is saved in map.html
map.save(outfile='map.html')