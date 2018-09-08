from flask import Flask, render_template, request, Response, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("image.html")

@app.route('/capture', methods = ["POST"])
def capture():
	if request.method == "POST":
		img = request.get_json(force = True)

		print(img)
		return "jvhcxkvj"

if __name__ == '__main__':
    app.run()
