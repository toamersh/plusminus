import requests
import json
import sys

def main(argv):
	response = requests.post('http://localhost:1234/plusminus', json = {"origin":int(argv[1]), "modifier":int(argv[2])})
	if response.ok:
		responseJson = json.loads(response.text)
		print (responseJson)

if __name__ == "__main__":
   main(sys.argv)