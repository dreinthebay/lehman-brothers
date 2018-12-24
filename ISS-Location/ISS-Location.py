import urllib3 as urllib
import json
import csv

http =urllib.PoolManager()
req = http.request('GET',"http://api.open-notify.org/iss-now.json")

obj = json.loads(req.data.decode('utf-8'))


print (obj['timestamp'])
print (obj['iss_position']['latitude'])
print (obj['iss_position']['longitude'])


newRow = [obj['timestamp'],obj['iss_position']['latitude'],obj['iss_position']['longitude']]
print (newRow)

with open('location-logger.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(newRow)

