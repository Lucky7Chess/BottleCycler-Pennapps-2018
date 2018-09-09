from flask import Flask, render_template, request, Response, redirect
from subprocess import Popen, PIPE
import base64
import serial
import os
app = Flask(__name__)

@app.route('/')
def index():
	# tmpl = env.get_template('index.html')
    # sidebar = env.get_template('sidebar.html')
    # js_url = url_for('static', filename='image.js')
    # return tmpl.render(root_url="",sidebar=sidebar.render(), jsurl=js_url)
    return render_template("home.html")

@app.route('/pic')
def pic():
    return render_template("image.html")

# @app.context_processor
# def override_url_for():
#     return dict(url_for=dated_url_for)
#
# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                      endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)

@app.route('/capture', methods = ["POST"])
def capture():
	if request.method == "POST":
		img = request.get_json(force = True)["strings"] #get the img
		print(img)
		img = img[22:]
		casted = b'{img}'
		with open("bottle.png", "wb") as fh:
			print(base64.b64decode(base64.b64decode(base64.b64encode(img.encode()))))
			fh.write(base64.b64decode(base64.b64decode(base64.b64encode(img.encode()))))
		process = Popen(['python', 'classify_image.py'], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate() #get classifier results
		bottle = str(str(stderr).find('bottle'))
		can = str(str(stderr).find('can'))
		if bottle == "-1" and can == "-1" :
			return -1
		else:
			a.write(b'1')
			return 1

if __name__ == '__main__':
    a =serial.Serial("/dev/tty.usbmodem1411")
    app.run()
