from iss_location_now import ISS_Tracker
from ISS_mapper import Mapper

print('Hello world')

tracker = ISS_Tracker('file_name.csv')
tracker.run(5)

print('tracker ran')

# map_path = os.getcwd() + '\\maps\\' + 'map4.html'
mapper = Mapper('file_name.csv', 'map4')
mapper.map_points()
print('opening map...')
mapper.open_map()
print('map created in file ' + 'map4')

