import urllib.request
import json
from pprint import pprint
import codecs
    
def get_info(lat1, lon1, lat2, lon2):
    keys = ["AIzaSyB3yUcVCIRKw6as2WbrAReszeqTlELP1dA","AIzaSyCgkQH8kVHzZ-nWyz9uazvwq9L5CY0qvL8","IzaSyDdRaFyIOzwPMwENHQVgrgr6DKzKYbnsNc","AIzaSyAAUAxUbaOFJ-pfx7epLMHfZ04wFrg-JMs","AIzaSyA9tVDmhB76ox5V5NuOxA2nXsix9T0vroQ","AIzaSyCT53zc5BiWIvLn5rkWJSz3F3JOU5paX1o","AIzaSyBxl-BjkVOFJ2SHy6YA0VrWgtuauMjE1dw","AIzaSyAyBVyYJtQO0v4jIuN2RR4Cj-99_rmZ6NQ","AIzaSyCwwiq6Z_gkFYPHZiwAvOq6S07DCPalB8I","AIzaSyAUuV53ZWF9l2JzangdtpQHtc_3WLGhhaY"]
    for key in keys:
        url_input = "origins="+str(lat1)+','+str(lon1) + "&destinations="+str(lat2)+','+str(lon2) + "&key="+key        
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=si&"+url_input
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))
        #print(data)
        if data['status'] == "OK":
            return (data['rows'][0]['elements'][0]['distance']['value']/1000.0, data['rows'][0]['elements'][0]['duration']['value']/3600.0)
    raise Exception("Ran out of keys")

def request_google(lat1, lon1, lat2, lon2):
    try:
        with open('cache.json','r') as fp:
            cache = json.load(fp)
    except IOError:
        cache = {}
    
    request_str = str(lat1)+str(lon1)+str(lat2)+str(lon2)
    if request_str not in cache:
        data = get_info(lat1,lon1,lat2,lon2)
        cache[request_str] = data
        print ("new request")
        with open('cache.json','w') as fp:
            json.dump(cache,fp)
    else:
        data = cache[request_str]
        #print("no cache")
    return data

