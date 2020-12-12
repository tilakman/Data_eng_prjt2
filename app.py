from flask import Flask, request, render_template
#from src.predict import prediction

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		output = request.form 
		return ('oui')

	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')