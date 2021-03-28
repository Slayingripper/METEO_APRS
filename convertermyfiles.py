import wget
import json
import xmltodict
import os
def fileconverter():
	url = "https://www.dom.org.cy/AWS/OpenData/CyDoM.xml"
	weatherfile="cydom.xml"
	jsonweather="jsonweather.json"

	if os.path.exists(weatherfile):
	  os.remove(weatherfile)
	else:
	  print("The file does not exist")

	if os.path.exists(jsonweather):
	  os.remove(jsonweather)
	else:
	  print("The file does not exist")


	wget.download(url, weatherfile)

	with open(weatherfile) as xml_file:
		data_dict = xmltodict.parse(xml_file.read())

	xml_file.close()

	json_data = json.dumps(data_dict)

	with open(jsonweather, "w") as json_file:
			json_file.write(json_data)
			json_file.close()
if __name__ == "__main__":
	fileconverter()