import pprint as pp
from flask import Flask, request
app = Flask(__name__)

from flask import jsonify

@app.route('/plusminus3/<int:number>')
def addSubtractParam(number):
	number = int(number)
	return jsonify({'plus': number+3,'minus': number-3})

@app.route('/plusminus', methods = ['POST'])
def addSubtractJson():
	content = request.json
	pp.pprint(content)
	return jsonify({'plus': content["base"]+content["number"],'minus': content["base"]-content["number"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)