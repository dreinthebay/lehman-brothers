# pip install -r requirements.txt
import urllib.request as url
import json
import csv
import os
import time
from tqdm import tqdm # progress bar

class ISS_Tracker():
	"""docstring for ClassName"""
	def __init__(self,csv_file_name): # arg):
		#self.arg = arg
		self.site_address = "http://api.open-notify.org/iss-now.json"
		self.csv_path = os.getcwd() + '//data//' + csv_file_name
		print('Path for CSV: ',self.check_for_writer_location(self.csv_path))
		# self.path = 
	
	"""
	docstring for method get_location
	This method will call the ISS api to get data.
	This method returns a list of 3 objects, timestamp, latitude, and longitude
	"""
	def get_location(self):
		# print('getting location...')
		response = url.urlopen(self.site_address)
		obj = json.loads(response.read())
		return [obj['timestamp'],obj['iss_position']['latitude'],obj['iss_position']['longitude']]

	# this function should be depricated
	def write_location(self):
		print('inside the write_location method')

	'''
	Checks to see if the csv file exists
	Throws an error if there is no file already
	Create the file later on
	'''
	def check_for_writer_location(self, fname):
		# print('Checking if there is a file here...')
		if not os.path.exists(os.getcwd()+'//data'):
			os.mkdir(os.getcwd()+'//data')

		return os.path.isfile(fname)

	# this code checks to see if the csv reader exists, if not, it calls to make the file
	# it makes a csv writer which can be used to write rows
	def initialize_writer(self, fname):
		if not t.check_for_writer_location(fname):
			print('File ',fname,' not found. attempting to make file...')
		
		with open(self.csv_path, 'wb') as csv_file:
			csv_writer = csv.writer(csv_file, delimiter=',')
		print('end of initialize_writer')
		print('writer type: ',type(csv_writer))
		return csv_writer

	
	def collect_5_second_interval_data(self, steps):
			# initialize writer
			# loop over _steps intervals
			# run get location
			# run writer
			
			# initialize writer
			'''
			loc_writer = self.initialize_writer(self.csv_path)
			print('made the writer!')
			loc_writer.writerow(['Time','Latitiude','Longitude'])

			# loop over _steps
			for i in range(steps):
				# get location
				loc = self.get_location()

				# write location to file
				loc_writer.writerow(loc)

				# wait 5 seconds
				time.sleep(5)
			'''

			with open(self.csv_path, 'w') as csv_file:
				loc_writer = csv.writer(csv_file, delimiter=',')
				
				loc_writer.writerow(['Time','Latitude','Longitude'])

				print('Getting location ', steps, ' times...')
				# loop over _steps
				for i in tqdm(range(steps)):
					# get location
					loc = self.get_location()

					# write location to file
					loc_writer.writerow(loc)

					# wait 5 seconds
					time.sleep(5)

					# progress bar goes here

			#'''
			return True	
		
if __name__ == '__main__':
	print('Connecting to ISS...')
	t = ISS_Tracker('generic_data_file.csv')
	t.collect_5_second_interval_data(10)

	# goal is to run ISS_Tracker.execute()