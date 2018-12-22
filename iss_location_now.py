import urllib3
import json

req = urllib3.Request("http://api.open-notify.org/iss-now.json")
response = urllib3.urlopen(req)

obj = json.loads(response.read())

print(obj['timestamp'])
print(obj['iss_position']['latitude'], obj['data']['iss_position']['latitude'])

# Example prints:
#   1364795862
#   -47.36999493 151.738540034