import requests
import json

response = requests.post('http://localhost:1234/plusminus', json = {"base":10, "number":4})
if response.ok:
	responseJson = json.loads(response.text)
	print (responseJson)