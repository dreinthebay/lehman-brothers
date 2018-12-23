'''
doc string
This class will connect to and process the ISS data
It will do analysis and map the coordinates of the ISS
'''

import numpy as np
import pandas as pd

class Mapper():
	"""docstring for ClassName"""
	def __init__(self, csv_file):
		self.csv_file = csv_file
		self.df = pd.read_csv(self.csv_file)
		
	def connect(self):
		pass

if __name__ == '__main__':
	print('hello world')
	#my_mapper = Mapper('ISS_Data.csv')