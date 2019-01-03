'''
doc string

Author:
Date:
This class will connect to and process the ISS data
It will do analysis and map the coordinates of the ISS

Instructions:
In main method, choose a csv file with time, latitude, and longitude coordinates.
Choose a location for the map html file
Run the program

> python ISS_mapper.py
'''

import numpy as np
import pandas as pd
from math import radians, cos, sin, asin, sqrt
import gmplot

class Mapper():
	"""docstring for ClassName
	The mapper class is used to map lat and long points
	"""
	def __init__(self, csv_file, map_path):
		self.csv_file = csv_file
		self.df = pd.read_csv(self.csv_file)
		self.map_path = map_path
		print('constructor')

	def haversine(self, lat1, lon1, lat2, lon2):
		"""
	    Calculate the great circle distance between two points 
	    on the earth (specified in decimal degrees)
	    """
	    # convert decimal degrees to radians 
		lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

		# haversine formula 
		dlon = lon2 - lon1 
		dlat = lat2 - lat1 
		a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
		c = 2 * asin(sqrt(a)) 
		r = 6371 # Radius of earth in kilometers. Use 3956 for miles
		return c * r

	def make_distance_column(self):
		self.df['Distance'] = 0
		for row in range(len(self.df.index)):
			if row > 0:
				a , b = self.df.iloc[row-1,1], self.df.iloc[row-1,2]
				c, d = self.df.iloc[row,1], self.df.iloc[row,2]
				self.df['Distance'].iloc[row] = self.haversine(a,b,c,d)
			else:
				self.df['Distance'].iloc[row] = 0

		# 	print(row)

		# for index, row in self.df.iterrows():
		# 	print('Index: ', index, ' Row', row)
		# 	if index > 0:
		# 		a , b = self.df.iloc[row - 1,1], self.df.iloc[row - 1,2] # one point
		# 		c , d = self.df.iloc[row,1], self.df.iloc[row,2] # second point
		 
		# 		self.df['Distance'].loc[index] = self.haversine(a,b,c,d)
		# # self.df['distance'] = self.df.apply(lambda row: haversine(row.Latitude,row.Longitude,1,1))
	
	def test_base_map(self):
		gmap1 = gmplot.GoogleMapPlotter(30.3,78,10)

		# pass absolute path
		gmap1.draw('C:\\Users\\slin2\\Documents\\GitHub\\lehman-brothers\\map1.html')
		
	def map_points(self):
		
		# Center on 0, 0
		gmap2 = gmplot.GoogleMapPlotter(0,0,5)

		# Center on the first point
		#gmap2 = gmplot.GoogleMapPlotter(self.df.loc[1,'Latitude'],self.df.loc[1,'Longitude'],5)

		# lat list
		lat_list = self.df['Latitude']#.tolist()

		# long list
		long_list = self.df['Longitude']

		gmap2.scatter(lat_list, long_list, '# FF0000', size=40, marker=False)

		gmap2.plot(lat_list, long_list, 'cornflowerblue',edge_width=2.5)

		gmap2.draw(self.map_path)

	def execute_test_haversine(self):
		self.make_distance_column()
		print(self.df.head())
		l = self.df.iloc[-1]
		f = self.df.iloc[0]
		print('last entry ', l['Latitude'])
		a = self.df.iloc[1,1] # lat
		a , b = self.df.iloc[1,1] , self.df.iloc[1,2] # one point
		c , d = self.df.iloc[2,1], self.df.iloc[2,2] # second point
		print('The Haversine formula distance is: ', self.haversine(a,b,c,d))




if __name__ == '__main__':
	print('hello world')
	csv_file = 'ISS_Data.csv'
	map_path = 'C:\\Users\\slin2\\Documents\\GitHub\\lehman-brothers\\map3.html'
	my_mapper = Mapper(csv_file, map_path)
	print(my_mapper.df.head())
	my_mapper.map_points()