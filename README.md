# METEO APRS

![Alt text](https://github.com/Slayingripper/METEO_APRS/blob/main/logos/met.png) ![alt](https://github.com/Slayingripper/METEO_APRS/blob/main/logos/cars.png)

Meteo APRS uses the Cyprus Meterological Center's API to query and push data to the APRS Network.
It downloads the XML file and covrets it to json (For easier handling) and queries the data for specific 
Stations. They are then pushed to the APRS network using TCP/IP. 

## Requirments
1. Python 3.7 +
2. Aprslib
3. Figlet


## Issues to tackle

The "live" XML file provided by the Depratment of Metereology has a major incosistancy issue . For example,when updating the file it would sometimes remove some stations from the list which made using hard coded numbering impossible. One other flaw is that not all stations measure the same information which makes the accuratly  dippicting the area quite difficult . To get around this , data is used from neighbouring stations for example "Humidity" and "Wind Direction" .


```xml  
</observation>
    <observation>
      <observation_name>Recom. Heavy Work Load</observation_name>
      <observation_value>100</observation_value>
      <observation_unit>%</observation_unit>
    </observation>
    <observation>
      <observation_name>Relative Humidity (1.2m)</observation_name>
      <observation_value>60</observation_value>
      <observation_unit>%</observation_unit>
    </observation>
    <observation>
      <observation_name>Accumulated Rainfall (10 min.)</observation_name>
      <observation_value>0.00</observation_value>
      <observation_unit>mm</observation_unit>
    </observation>
  </observations>
```

# Running

To run the program just run the main file : 
```
./meteoaprs.py 
```

## To Do

- [x] Sends data to APRS
- [x] Pulls data from API 
- [x] Fixes some of the format issues of API 
- [ ] Uses TNC to send data 
- [ ] config-file 
- [ ] refactoring 

