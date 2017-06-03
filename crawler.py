from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import requests

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('url')
parser.add_argument('word')
parser.add_argument('ignorecase')

# Função para abortar a Request feita
def abort_if_invalid(url):
	abort(404)
	
# Função que faz um GET para a URL e retorna quantas vezes a palavra word aparece no conteudo
def count_words_in(url, word, ignore_case):
	try:
		r = requests.get(url)
		data = str(r.text)
		if (str(ignore_case).lower() == 'true'):
			return data.lower().count(word.lower())
		else:
			return data.count(word)
	except Exception:
		abort_if_invalid(url)
		
# Função que inclui 'http://' na url e retorna a URL valida
def validate_url(url):
	if not(url.startswith('http')):
		url = 'http://' + url
	return url
	

class UrlCrawlerAPI(Resource):
	def get(self):
		args = parser.parse_args()
		if (args['url'] == ''):
			abort(404, message="Please provide 'url' argument")
		valid_url = validate_url(args['url'])
		return { valid_url : { args['word'] : count_words_in(valid_url, args['word'], args['ignorecase']) }}

		
api.add_resource(UrlCrawlerAPI, "/")

if __name__ == '__main__':
	app.run(debug=True)