from flask import Flask, render_template, request, Response, redirect
from subprocess import Popen, PIPE
import base64
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/capture', methods = ["POST"])
def capture():
	if request.method == "POST":
		img = request.get_json(force = True) #get the img
		#img = img[23:]
		casted = b'{img}'
		#encoded = base64.b64encode(str(img))
		with open("bottle.png", "wb") as fh:
			fh.write(casted)
		process = Popen(['python', 'classify_image.py'], stdout=PIPE, stderr=PIPE) #classify the image
		stdout, stderr = process.communicate() #get classifier results
		return str(str(stderr).find('bottle'))

if __name__ == '__main__':
    app.run()
