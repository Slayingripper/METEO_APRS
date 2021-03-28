import aprslib

def sendmypacket(LAT,LONG,WINDDIRECTION,WINDSPEED,TEMP,HUMIDITY,PRESSURE):


	# a valid passcode for the callsign is required in order to send
	AIS = aprslib.IS("5B4ANU", passwd="15540", port=14580)
	AIS.connect()
	# send a single status message
	#AIS.sendall("5B4ANU-WX>APRS:>Hello World!")
	AIS.sendall("5B4ANU-13>APDR15,WIDE1-1:= "+LAT+"N/"+LONG+"E_"+WINDDIRECTION+"/00"+WINDSPEED+"g000t"
	+TEMP+"r000p000P000h"+HUMIDITY+"b"+PRESSURE+"1L000"
	"testing")

if __name__ == "__main__":
	sendmypacket("")

