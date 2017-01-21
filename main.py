import json
import caching

with open('charging_stations.json') as data_file:    
    data = json.load(data_file)

sta_info = {}
sts = []

def dist(lat1, lon1, lat2, lon2):
    import math
    R = 6378137.0000
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    delta_lat = (lat2 - lat1)
    delta_lon = (lon2 - lon1)
    #a = math.sin(delta_lat/2.0) * math.sin(delta_lat/2.0) +  math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon/2.0) * math.sin(delta_lon/2.0)
    a = math.sqrt((math.cos(lat2)*math.sin(delta_lon))**2 + ((math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon))**2))
    b = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(delta_lon)
    #c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    c = math.atan2(a, b)
    d = R * c
    return d/1000.0

def get_keys():
    keys = []
    for key in sta_info:
        keys.append(key)
    return keys                               

def get_sort_keys_by_spherical_dist(lat, lon, keys):
    
    global sts, sta_info
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            t_dist_i = dist(sta_info[keys[i]]['latitude'], sta_info[keys[i]]['longitude'], lat, lon)
            t_dist_j = dist(sta_info[keys[j]]['latitude'], sta_info[keys[j]]['longitude'], lat, lon)
            if t_dist_i > t_dist_j:
                keys[i], keys[j] = keys[j], keys[i]
    return keys

def print_top_3(lat, lon):
    global sts, sta_info
    keys = get_sort_keys_by_spherical_dist(lat, lon, get_keys())
    for i in range(3):
        print(str(sta_info[keys[i]]['latitude']) + " " + str(sta_info[keys[i]]['longitude']) + " " + sta_info[keys[i]]['station_name'] + " " + "%.3f" % dist(sta_info[keys[i]]['latitude'], sta_info[keys[i]]['longitude'], lat, lon))


def get_API_info(st1, st2):
    global sts, sta_info
    return caching.request_google(sta_info[st1]['latitude'], sta_info[st1]['longitude'], sta_info[st2]['latitude'], sta_info[st2]['longitude'])
    
def get_dist(st1, st2):
    global sts, sta_info
    return dist(sta_info[st1]['latitude'], sta_info[st1]['longitude'], sta_info[st2]['latitude'], sta_info[st2]['longitude'])

def initialization():
    global sts, sta_info
    sts = []
    for key in sta_info:
        sts.append(key)
    sts.append(0)
    sts.append(1)

def Dijkstra():
    global sts, sta_info
    
    end_pt = len(sts) - 1
    start_pt = len(sts) - 2
    node_num = len(sts)
    MAX = 10000
    total_dist = []
    
    in_queue = []
    shortest_time = []
    total_dist = []
    back_track = []
    for i in range(node_num):
        shortest_time.append(MAX)
        total_dist.append(0)
        back_track.append(-1)
        in_queue.append(False)

    in_queue[start_pt] = True
    shortest_time[start_pt] = 0
    curr = start_pt
    while curr != end_pt:
        curr_min = MAX
        for i in range(node_num):
            if in_queue[i] == False:
                if i != curr and get_dist(sts[curr], sts[i]) <= 480:
                    dis, time = get_API_info(sts[curr], sts[i])
                    if dis <= 480 and (dis / 80.0 + dis / 480.0 / 3.0) + shortest_time[curr] < shortest_time[i]:
                        shortest_time[i] = (dis / 80.0 + dis / 480.0 / 3.0) + shortest_time[curr]
                        total_dist[i] = total_dist[curr] + dis
                        back_track[i] = curr
                if shortest_time[i] < curr_min:
                    curr_min = shortest_time[i]
                    nxt_curr = i
        curr = nxt_curr
        in_queue[curr] = True
        print("curr:" + str(curr))
        print("time:" + str(shortest_time[curr]))
    
    temp_pt = end_pt
    path = []
    path.append(sts[end_pt])
    while back_track[temp_pt]!=-1:
        temp_pt = back_track[temp_pt]
        t_id = sts[temp_pt]
        path.append(t_id)

    res = []
    
    for i in range(len(path)):
        t_id = path[len(path)-i-1]
        first_part = str(sta_info[t_id]['latitude']) + " " + str(sta_info[t_id]['longitude']) + " " + sta_info[t_id]['city']
        d_t = {}
        d_t['latitude'] = sta_info[t_id]['latitude']
        d_t['longitude'] = sta_info[t_id]['longitude']
        d_t['city'] = sta_info[t_id]['city']
        res.append(d_t)
        print(first_part + " " + str(t_id))
    print(shortest_time[end_pt], total_dist[end_pt])
    return res

def path_finding(lat1, lon1, lat2, lon2):
    global sts, sta_info
    sta_info[0] = {}
    sta_info[1] = {}

    sta_info[0]['latitude'] = lat1
    sta_info[0]['longitude'] = lon1
    sta_info[0]['city'] = "Start"

    sta_info[1]['latitude'] = lat2
    sta_info[1]['longitude'] = lon2
    sta_info[1]['city'] = "End"

    initialization()
    
    return Dijkstra()

# get lat,lon,city, station name, id number_of_results

number_of_results = data['total_results']

for i in range(number_of_results):
    sta_temp = {}
    sta_temp["latitude"] = data['fuel_stations'][i]['latitude']
    sta_temp["longitude"] = data['fuel_stations'][i]['longitude']
    sta_temp["station_name"] = data['fuel_stations'][i]['station_name']
    sta_temp["city"] = data['fuel_stations'][i]['city']
    sta_info[data['fuel_stations'][i]['id']] = sta_temp



# Part 1
print("Part 1:")
coord_input = input('Enter your input:').split()
coord_input = (float(coord_input[0]), float(coord_input[1]))
print(coord_input)
print_top_3(coord_input[0], coord_input[1])

# Part 2

print("Part 2:")
start = input('Enter your input:').split()
start = (float(start[0]), float(start[1]))

end = input('Enter your input:').split()
end = (float(end[0]), float(end[1]))

dis, time = caching.request_google(start[0], start[1], end[0], end[1])
print("%.3f" % dis, "%.2f" % time)

# Part 4

print("Part 4:")
start = input('Enter your input:').split()
start = (float(start[0]), float(start[1]))

end = input('Enter your input:').split()
end = (float(end[0]), float(end[1]))

path_finding(start[0], start[1], end[0], end[1])

