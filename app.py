from flask import Flask, request, render_template
from src.recommendations import recommendations
from prometheus_client import start_http_server
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client import Summary


import time

REQUESTS = Counter('twitter_calls_total', 'How many times the app was called')
EXCEPTIONS = Counter('twitter_exceptions_total', 'How many exceptions the app trigger')
INPROGRESS = Gauge('twitter_inprogress','number of requests in progress')
LAST = Gauge('twitter_last_time_seconds','the last time our app was called')
LATENCY = Summary('twitter_latency_seconds','time needed for a request')

app = Flask(__name__)

def tweets(sentence):
	tweets_block = ""
	if sentence:
		REQUESTS.inc()
		INPROGRESS.inc()
		start=time.time()
		time.sleep(5)
		res= recommendations(sentence)
		for index, row in res.iterrows():
			tweets_block += "<tr><td>" + str(row['id']) + "</td><td>" + row['text'] + "</td></tr>"
	else:
		with EXCEPTIONS.count_exceptions():
			raise Exception

	LATENCY.observe(time.time() - start)
	INPROGRESS.dec()
	return render_template('index.html', tweets=tweets_block)

@app.route('/', methods=['GET','POST'])
def index():
	LAST.set(time.time())
	if request.method == 'POST':
		output = request.form
		return tweets(output['sentence'])
	REQUESTS.inc()
	return render_template('index.html')

if __name__ == '__main__':
	start_http_server(8010)
	app.run(host='0.0.0.0')