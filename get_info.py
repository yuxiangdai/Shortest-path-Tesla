
def get_info(lat1, lon1, lat2, lon2):
    import urllib2
    import json
    from pprint import pprint
    
    keys = ["AIzaSyB3yUcVCIRKw6as2WbrAReszeqTlELP1dA","AIzaSyCgkQH8kVHzZ-nWyz9uazvwq9L5CY0qvL8","IzaSyDdRaFyIOzwPMwENHQVgrgr6DKzKYbnsNc","AIzaSyAAUAxUbaOFJ-pfx7epLMHfZ04wFrg-JMs","AIzaSyA9tVDmhB76ox5V5NuOxA2nXsix9T0vroQ","AIzaSyCT53zc5BiWIvLn5rkWJSz3F3JOU5paX1o","AIzaSyBxl-BjkVOFJ2SHy6YA0VrWgtuauMjE1dw","AIzaSyAyBVyYJtQO0v4jIuN2RR4Cj-99_rmZ6NQ","AIzaSyCwwiq6Z_gkFYPHZiwAvOq6S07DCPalB8I","AIzaSyAUuV53ZWF9l2JzangdtpQHtc_3WLGhhaY"]
    for key in keys:
        url_input = "origins="+str(lat1)+','+str(lon1) + "&destinations="+str(lat2)+','+str(lon2) + "&key="+key        
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=si&"+url_input
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)
        if data['status'] == "OK":
            return(str(round(data['rows'][0]['elements'][0]['distance']['value']/1000.0,3))+' '+str(round(data['rows'][0]['elements'][0]['duration']['value']/3600.0,2)))
    raise Exception("Ran out of keys")
    
def test():
    lat1 = 37.773972
    lon1 = -122.431297
    lat2 = 37.4931367
    lon2 = -121.9453883
    return(get_info(lat1, lon1, lat2, lon2))