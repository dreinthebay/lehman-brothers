from iss_location_now import ISS_Tracker
from ISS_mapper import Mapper

intro = input('Would you like an intro? y/n')
if intro == 'y':
	print('Welcome to the ISS tracker program. This program will track where the International Space Station (ISS) is over the earth and then plot its course.')
	print('The program will record a data point every 5 seconds of latitude and longitude of the space ship. The program will ask for the number of data points to collect. Entering large numbers will take quite some time.')
	print('For example, entering 10 would be 50 seconds.')
_steps = input('Enter the number of data points would you like to collect? ')
_steps = int(_steps)
print(type(_steps))
tracker = ISS_Tracker('file_name.csv')
tracker.run(_steps)

print('tracker ran')

# map_path = os.getcwd() + '\\maps\\' + 'map4.html'
mapper = Mapper('file_name.csv', 'map4')
mapper.map_points()
print('opening map...')
mapper.open_map()
print('map created in file ' + 'map4')

