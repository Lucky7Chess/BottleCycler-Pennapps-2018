from flask import Flask, render_template, request, Response, redirect
from subprocess import Popen, PIPE
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("image.html")

@app.route('/capture', methods = ["POST"])
def capture():
	if request.method == "POST":
		img = request.get_json(force = True)
		process = Popen(['python', 'classify_image.py'], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate() #get classifier results
		print(img)	
		return str(str(stderr).find('bottle'))

if __name__ == '__main__':
    app.run()
