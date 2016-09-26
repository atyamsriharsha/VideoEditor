import os
import sys
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)


@app.route('/server1',methods=['GET','POST'])
def adding():
	name = request.form
	output = name.getlist('output')
	rows = int(name['Rows'])
	cols = int(name['Cols'])
	Flag = int(name['Flag'])
	print rows,cols
	list1 = str(output[0])
	list1 = list1[1:-1]
	ans = ""
	for x in xrange(len(list1)):
		if list1[x]!='"':
			ans = ans + str(list1[x])
	finalvalues = []
	temp = ""
	for x in xrange(len(ans)):
		if ans[x]!=",":
			temp = temp+ans[x]
		else:
			finalvalues.append(temp)
			temp = ""
	finalvalues[0] = (finalvalues)[0][1:]
	Names = ""
	for x in xrange(len(finalvalues)):
		Names = Names + ',' + str(finalvalues[x])
	Names = Names[1:]
	os.system('python concatenation.py ' + Names + ' ' + str(rows) + ' ' + str(cols)+ ' '+str(Flag))
	#print Names
	#print finalvalues,rows,cols
	return "hello"


@app.route('/record',methods=['GET','POST'])
def Record():
	os.system('python record.py')


@app.route('/reverse',methods=['GET','POST'])
def Reverse():
	name = request.form
	filename = name['output']
	os.system('python reverse.py ' + str(filename))


if __name__ == '__main__':
	app.run(debug=True)
