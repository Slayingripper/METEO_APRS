import aprssend
import convertermyfiles
import json
#convertermyfiles.fileconverter()
windirection = '200'
pressure = '1029.3'
json = json.loads(open('jsonweather.json').read())
#value = json['meteorology']['stations']['station']['18']

stationname =json['meteorology']['stations']['station'][18]['station_code']
station_latitude =json['meteorology']['stations']['station'][18]['station_latitude']
station_longitude =json['meteorology']['stations']['station'][18]['station_longitude']
temprature = json['meteorology']['observations'][18]['observation'][0]['observation_value']
humidity = json['meteorology']['observations'][18]['observation'][7]['observation_value']
windspeed = json['meteorology']['observations'][18]['observation'][3]['observation_value']
rain10m = json['meteorology']['observations'][18]['observation'][8]['observation_value']
rain24h = json['meteorology']['observations'][18]['observation'][9]['observation_value']
print(stationname,station_latitude,station_longitude,temprature,humidity,windspeed,rain10m,rain24h)


aprssend.sendmypacket(station_latitude,station_longitude,windirection,temprature,humidity,pressure,"0")