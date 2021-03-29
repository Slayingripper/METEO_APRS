import aprslib
import json
import math
json = json.loads(open('jsonweather.json').read())
def fetchweather():
    station_latitude =json['meteorology']['stations']['station'][9]['station_latitude']
    station_longitude =json['meteorology']['stations']['station'][9]['station_longitude']
    temprature = json['meteorology']['observations'][9]['observation'][0]['observation_value']
    humidity = json['meteorology']['observations'][9]['observation'][6]['observation_value']
    windspeed = json['meteorology']['observations'][9]['observation'][4]['observation_value']
    windirection = json['meteorology']['observations'][9]['observation'][5]['observation_value']
    pressure = json['meteorology']['observations'][9]['observation'][12]['observation_value']
    rain10m = json['meteorology']['observations'][9]['observation'][7]['observation_value']
    rain24h = json['meteorology']['observations'][9]['observation'][7]['observation_value']
	
    rain10m = str(math.trunc(float(rain10m)*10))
    rain24h = str(math.trunc(float(rain24h)*10))
    pressure = str(math.trunc(float(pressure)*10))
    windspeed=str(math.trunc(float(windspeed)*10))
    temprature =str(math.trunc((float(temprature) * 1.8) + 32))
    print(station_latitude,station_longitude)
	#sendmypacket(windirection,windspeed,temprature,humidity,pressure,rain10m,rain24h)

def sendmypacket(WINDDIRECTION,WINDSPEED,TEMP,HUMIDITY,PRESSURE,RAIN10,RAIN24):


	# a valid passcode for the callsign is required in order to send
	#AIS = aprslib.IS("5B4NC", passwd="12782", port=14580)
	AIS = aprslib.IS("5B4ANU", passwd="15540", port=14580)
	AIS.connect()
	# send a single status message
	#AIS.sendall("5B4ANU-WX>APRS:>Hello World!")
	AIS.sendall("5B4LC-13>APDR15,WIDE1-1:=3508.4 N/""03323.8 E_"+WINDDIRECTION+"/0"+WINDSPEED+"g000t"+TEMP+"r00"+RAIN10+"p00"+RAIN24+"P000h"+HUMIDITY+"b"+PRESSURE+"L000")
	#AIS.sendall("5B4ANU-13>APDR15,WIDE1-1,qAS,5B4ANU:=3506.1 N/03321.5 E_084/002g000t62r000p000P000h29b10251L000")
if __name__ == "__main__":
	fetchweather()
