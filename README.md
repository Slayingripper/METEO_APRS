# METEO_APRS

Meteo APRS uses the Cyprus Meterological Center's API to query and push data to the APRS Network.
It downloads the XML file and covrets it to json (For easier handling) and queries the data for specific 
Stations. They are then pushed to the APRS network using TCP/IP. 

## Requirments
1. Python 3.7 +
2. Aprslib
3. Figlet


## To Do

- [x] Sends data to APRS
- [x] Pulls data from API 
- [x] Fixes some of the format issues of API 
- [ ] Uses TNC to send data 
- [ ] config-file 
