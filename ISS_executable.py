'''
This file will be run from the cmd line and executed with inputs from the user
'''

from iss_location_now import ISS_Tracker
from ISS_mapper import Mapper
import sys
import argparse


try:
	parser = argparse.ArgumentParser()
	parser.add_argument("steps", help="runs the data collector step times",
	            type=int)
	args = parser.parse_args()

	tracker = ISS_Tracker('file_name.csv')
	tracker.run(args.steps)
	mapper = Mapper('file_name.csv', 'map4')
	mapper.map_points()
	print('opening map...')
	mapper.open_map()
	print('map created in file ' + 'map4')

	#print the square of user input from cmd line.
	print(args.steps)

	#print all the sys argument passed from cmd line including the program name.
	print(sys.argv)

	#print the second argument passed from cmd line; Note it starts from ZERO
	print(sys.argv[1])
except:
	e = sys.exc_info()[0]
	print(e)

