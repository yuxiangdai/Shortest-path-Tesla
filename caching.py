import urllib2
import json
from pprint import pprint


def get_info(lat1, lon1, lat2, lon2):
    ## Make requests to Google API for the given latitudes and longitudes.
    ## Return the distance and duration of the road trip at current time.
    ## Input: lat1, lon1 (floats) is starting location. lat2, lon2 (floats) is destination location
    ## Output: string in format "-distance- -duration-" (string)    
    
    keys = ["AIzaSyB3yUcVCIRKw6as2WbrAReszeqTlELP1dA","AIzaSyCgkQH8kVHzZ-nWyz9uazvwq9L5CY0qvL8","IzaSyDdRaFyIOzwPMwENHQVgrgr6DKzKYbnsNc","AIzaSyAAUAxUbaOFJ-pfx7epLMHfZ04wFrg-JMs","AIzaSyA9tVDmhB76ox5V5NuOxA2nXsix9T0vroQ","AIzaSyCT53zc5BiWIvLn5rkWJSz3F3JOU5paX1o","AIzaSyBxl-BjkVOFJ2SHy6YA0VrWgtuauMjE1dw","AIzaSyAyBVyYJtQO0v4jIuN2RR4Cj-99_rmZ6NQ","AIzaSyCwwiq6Z_gkFYPHZiwAvOq6S07DCPalB8I","AIzaSyAUuV53ZWF9l2JzangdtpQHtc_3WLGhhaY"]
    
    for key in keys:
        url_input = "origins="+str(lat1)+','+str(lon1) + "&destinations="+str(lat2)+','+str(lon2) + "&key="+key        
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=si&"+url_input
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        
        ## If key is valid:
        if data['status'] == "OK":
            return(str(round(data['rows'][0]['elements'][0]['distance']['value']/1000.0,3))+' '+str(round(data['rows'][0]['elements'][0]['duration']['value']/3600.0,2)))
        
    ## If none of the keys are valid
    raise Exception("Ran out of keys")


def request_google(lat1, lon1, lat2, lon2):
    ## Return the distance and duration of the road trip at current time for the given latitudes and longitudes.
    ## Load cache file "cache.json", and make requests to Google API only if the results are not cached.
    ## Save the new cache in "cache.json".
    ## Input: lat1, lon1 (floats) is starting location. lat2, lon2 (floats) is destination location
    ## Output: string in format "-distance- -duration-" (string)    
    
    
    ## Open existing cache file if it exists
    try:
        with open('cache.json','r') as fp:
            cache = json.load(fp)
    except IOError:
        cache = {}
    
    request_str = str(lat1)+str(lon1)+str(lat2)+str(lon2)
    ## Cache for the given coordiantes doesn't exist
    if request_str not in cache:
        data = get_info(lat1,lon1,lat2,lon2)
        cache[request_str] = data
        print ("new request")
        with open('cache.json','w') as fp:
            json.dump(cache,fp)
    ## Cache exists    
    else:
        data = cache[request_str]
        print("cache exists")
    return data


def test():
    ## Tests request_google with user input
    ## Input: none
    ## Output: string in format "-distance- -duration-" (string)    

    coord_input_1 = map(float,raw_input('Enter your first coordinates:').split())
    ##print coord_input_1
    coord_input_2 = map(float,raw_input('Enter your second coordinates:').split())
    ##print coord_input_2
    lat1 = coord_input_1[0]
    lon1 = coord_input_1[1]
    lat2 = coord_input_2[0]
    lon2 = coord_input_2[1]
    print request_google(lat1, lon1, lat2, lon2)