import pprint as pp
from flask import Flask, request
app = Flask(__name__)

from flask import jsonify

@app.route('/plusminus', methods = ['GET'])
def addSubtractParam():
	try:
		origin = int(request.args.get('origin', None))
		modifier = int(request.args.get('modifier', None))
		return jsonify({'plus': origin+modifier,'minus': origin-modifier})
	except TypeError:
		return ('An error has occurred.  Please check your query parameters.  Example:  http://localhost:1234/plusminus?origin=56&modifier=9')

@app.route('/plusminus', methods = ['POST'])
def addSubtractJson():
	content = request.json
	return jsonify({'plus': content["origin"]+content["modifier"],'minus': content["origin"]-content["modifier"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)