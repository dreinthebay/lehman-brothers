'''
This file will be run from the cmd line and executed with inputs from the user
'''

# example cmd line
# python ISS_executable 10 ISS_data_file ISS_map
# this example call will run for 50 seconds collecting 5 lat/long points and storing it in \data\ISS_data_file.csv. The map is then created in \map\ISS_map.html

from ISS_location_grabber.iss_location_grabber import ISS_Tracker
from ISS_map_maker.ISS_map_maker import Mapper
import sys
import argparse


try:
	parser = argparse.ArgumentParser()
	parser.add_argument("steps", help="runs the data collector step times",
	            type=int)
	parser.add_argument("csv_name", help='the file name for the csv', type=str)
	parser.add_argument("map_name", help="the file name for the map", type=str)
	args = parser.parse_args()

	if args.steps > 0:
		tracker = ISS_Tracker(args.csv_name)
		tracker.run(args.steps)
	mapper = Mapper(args.csv_name, args.map_name)
	mapper.map_points()
	print('opening map...')
	mapper.open_map()
	print('map created in file ' + args.map_name)

	#print the square of user input from cmd line.
	print(args.steps)

	#print all the sys argument passed from cmd line including the program name.
	print(sys.argv)

	#print the second argument passed from cmd line; Note it starts from ZERO
	print(sys.argv[1])
except:
	e = sys.exc_info()[0]
	print(e)

