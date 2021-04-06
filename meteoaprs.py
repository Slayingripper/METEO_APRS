import aprssend
import nicosia,limassol,cavogreco,kyperunda,agros
import grabweather
import time
import sys
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Meteo APRS'))


#grabweather.fileconverter()
# time.sleep(3)
# print("Fetching Nicosia Weather")
#nicosia.fetchweather()
# time.sleep(3)
# print("Fetching Cavogreco Weather")
# #time.sleep(3)
# #cavogreco.fetchweather()
# print("Fetching Agros Weather")
# time.sleep(3) 
agros.fetchweather()
#kyperunda.fetchweather()
#limassol.fetchweather()