import urllib3
# pip install -r requirements.txt
import urllib.request as url
import json
import os
import time

req = urllib3.Request("http://api.open-notify.org/iss-now.json")
response = urllib3.urlopen(req)
class ISS_Tracker():
	"""docstring for ClassName"""
	def __init__(self): # arg):
		#self.arg = arg
		self.site_address = "http://api.open-notify.org/iss-now.json"
		self.csv_path = 'ISS_data.csv'
		print('Path for CSV: ',self.check_for_writer_location(self.csv_path))
		# self.path = 
	
	"""docstring for method get_location
	This method will call the ISS api to get data.
	This method returns a list of 3 objects, timestamp, latitude, and longitude"""
	def get_location(self):
		print('inside the get_location method')
		response = url.urlopen(self.site_address)
		obj = json.loads(response.read())
		return [obj['timestamp'],obj['iss_position']['latitude'],obj['iss_position']['longitude']]

		print('inside the write_location method')

	'''
	Checks to see if the csv file exists
	Throws an error if there is no file already
	Create the file later on
	'''
	def check_for_writer_location(self,fname):
		print('Checking if there is a file here...')
		return os.path.isfile(fname)

	# this code checks to see if the csv reader exists, if not, it calls to make the file
	def initialize_writer(self,fname):
		if not t.check_for_writer_location(self,fname):
			print('File ',fname,' not found. attempting to make file...')
		
		with open(self.csv_path, 'wb') as csv_file:
			csv_writer = csv.writer(csv_file, delimiter=',')
		print('end of initialize_writer')
		return csv_writer

	
	def collect_5_second_interval_data(self, steps):
			# initialize writer
			# loop over _steps intervals
			# run get location
			# run writer

			# initialize writer
			loc_writer = self.initialize_writer(self.csv_path)

			# loop over _steps
			for i in range(steps):
				# get location
				loc = self.get_location()

				# write location to file
				loc_writer.write_row(loc)

print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])
				# wait 5 seconds
				time.sleep(60)
			return True	
		
if __name__ == '__main__':
	print('In the main method')
	t = ISS_Tracker()
	fname = 'requirements.txt'
	print('Is there a file in ', fname, '? ', t.check_for_writer_location(fname))
	ls = t.get_location()
	print(ls)
	time.sleep(3)
	print('slept and woke up')

	# goal is to run ISS_Tracker.execute()


'''
print('Hello World')
req = "http://api.open-notify.org/iss-now.json"
response = url.urlopen(req)


obj = json.loads(response.read())

print('The time is: ', obj['timestamp'])
print('The latitude is: ', obj['iss_position']['latitude']) #, obj['data']['iss_position']['latitude'])
print('The longitude is: ', obj['iss_position']['longitude'])
'''
# Example prints:
#   1364795862
#   -47.36999493 151.738540034