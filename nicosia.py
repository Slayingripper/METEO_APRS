import aprslib
import json
import math
json = json.loads(open('jsonweather.json').read())
def fetchweather():
	
#value = json['meteorology']['stations']['station']['18']

	stationname =json['meteorology']['stations']['station'][3]['station_code']
	station_latitude =json['meteorology']['stations']['station'][3]['station_latitude']
	station_longitude =json['meteorology']['stations']['station'][3]['station_longitude']
	temprature = json['meteorology']['observations'][3]['observation'][0]['observation_value']
	humidity = json['meteorology']['observations'][3]['observation'][10]['observation_value']
	windspeed = json['meteorology']['observations'][3]['observation'][5]['observation_value']
	windirection = json['meteorology']['observations'][3]['observation'][6]['observation_value']
	rain10m = json['meteorology']['observations'][18]['observation'][8]['observation_value']
	rain24h = json['meteorology']['observations'][18]['observation'][9]['observation_value']
	pressure = json['meteorology']['observations'][3]['observation'][12]['observation_value']
	pressure = math.trunc(float(pressure)*10)
	pressure=str(pressure)
	windspeed=str(math.trunc(float(windspeed)*10))
	temprature =str(math.trunc((float(temprature) * 1.8) + 32))

	sendmypacket(windirection,windspeed,temprature,humidity,pressure)

def sendmypacket(WINDDIRECTION,WINDSPEED,TEMP,HUMIDITY,PRESSURE):


	# a valid passcode for the callsign is required in order to send
	#AIS = aprslib.IS("5B4NC", passwd="12782", port=14580)
	AIS = aprslib.IS("5B4ANU", passwd="15540", port=14580)
	AIS.connect()
	# send a single status message
	#AIS.sendall("5B4ANU-WX>APRS:>Hello World!")
	AIS.sendall("5B4NC-13>APDR15,WIDE1-1:=3508.4 N/""03323.8 E_"+WINDDIRECTION+"/0"+WINDSPEED+"g000t"+TEMP+"r000p000P000h"+HUMIDITY+"b"+PRESSURE+"L000")
	#AIS.sendall("5B4ANU-13>APDR15,WIDE1-1,qAS,5B4ANU:=3506.1 N/03321.5 E_084/002g000t62r000p000P000h29b10251L000")
if __name__ == "__main__":
	fetchweather()
