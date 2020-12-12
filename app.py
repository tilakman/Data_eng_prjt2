from flask import Flask, request, render_template
from src.recommendations import recommendations

app = Flask(__name__)

def tweets(sentence):
	tweets_block = ""
	if sentence:
		res= recommendations(sentence)
		for index in res:
			#tweets_block += "<tr id=" + str(index) + " > <td>" + str(index) + "</td> <td>" + res[index] + "</td> </tr>"
			print(index)


	print(tweets_block)	
	return render_template('index.html', tweets=tweets_block)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		output = request.form 
		return tweets(output['sentence'])

	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')