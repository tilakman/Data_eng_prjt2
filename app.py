from flask import Flask, request, render_template
from src.recommendations import recommendations

app = Flask(__name__)

def tweets(sentence):
	tweets_block = ""
	if sentence:
		res= recommendations(sentence)
		print(res)
		for index, row in res.iterrows():
			tweets_block += "<tr><td>" + str(row['id']) + "</td><td>" + row['text'] + "</td></tr>"



	return render_template('index.html', tweets=tweets_block)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		output = request.form
		return tweets(output['sentence'])
	
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')