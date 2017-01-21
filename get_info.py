
def get_info(lat1, lon1, lat2, lon2):
    import urllib2
    import json
    from pprint import pprint
    
    keys = ["AIzaSyB3yUcVCIRKw6as2WbrAReszeqTlELP1dA"]
    for key in keys:
        url_input = "origins="+str(lat1)+','+str(lon1) + "&destinations="+str(lat2)+','+str(lon2) + "&key="+key        
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=si&"+url_input
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        if data['status'] == "OK":
            return(str(round(data['rows'][0]['elements'][0]['distance']['value']/1000.0,3))+' '+str(round(data['rows'][0]['elements'][0]['duration']['value']/3600.0,2)))
    raise Exception("Ran out of keys")
    
#37.773972 -122.431297
#37.4931367 -121.9453883

def test():
    coord_input_1 = map(float,raw_input('Enter your first coordinates:').split())
    print coord_input_1
    coord_input_2 = map(float,raw_input('Enter your second coordinates:').split())
    print coord_input_2
    lat1 = coord_input_1[0]
    lon1 = coord_input_1[1]
    lat2 = coord_input_2[0]
    lon2 = coord_input_2[1]
    print get_info(lat1, lon1, lat2, lon2)

test()