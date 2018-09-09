from flask import Flask, render_template, request, Response, redirect
from subprocess import Popen, PIPE
import base64
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")
@app.route('/login')
def login():
    return render_template("image.html")

@app.route('/capture', methods = ["POST"])
def capture():
	if request.method == "POST":
		img = request.get_json(force = True)["strings"] #get the img
		print(img)
		img = img[22:]
		casted = b'{img}'
		#img += '=' * (-len(img) % 4)
		#encoded = base64.b64encode(str(img))

		with open("bottle.png", "wb") as fh:
			print(base64.b64decode(base64.b64decode(base64.b64encode(img.encode()))))
			fh.write(base64.b64decode(base64.b64decode(base64.b64encode(img.encode()))))
		process = Popen(['python', 'classify_image.py'], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate() #get classifier results
		return str(str(stderr).find('bottle'))

if __name__ == '__main__':
    app.run()
