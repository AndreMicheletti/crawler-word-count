# crawler-word-count
Web Crawler API to count how many times a word appear in a given URL

## API

This API will take a url and a word and count in the requested URL's HTML the number of matches (case sensitive)

Example:
`http://127.0.0.1:5000/?url=google.com&word=google&ignorecase=true`

`?url=[url]` is the url to be requested

`&word=[word]` is the word to be searched and counted

`&ignorecase=true` pass this argument to match ignoring case

Return JSON:

```json
{
	"http://google.com" : {
		"google" : 83
	}
}
```

## Setup

To test this script, you'll need [Python 3.x](https://www.python.org/downloads/) installed and [pip](https://pip.pypa.io/en/stable/installing/) to get the packages

Then you must get the extensions [Flask-restful](http://flask-restful-cn.readthedocs.io/en/0.3.5/installation.html) and [requests](http://docs.python-requests.org/en/master/user/install/)

To get then you can simply open a terminal and type:
`pip install flask-restful` and then `pip install requests`

## Running

To run the program, `clone` the repository or download `crawler.py`

Open a terminal and go to the folder that contains `crawler.py` 

Type `python crawler.py` and it will run the service under http://127.0.0.1:5000/

Then all you need to do is request the service passing the arguments:

- via Browser : you can do it on your browser, just type this in the address box = `http://127.0.0.1:5000/?url=google.com&word=google`

- via cURL : open another terminal and type `curl http://127.0.0.1:5000/ -d "url=google.com" -d "word=google" -X GET` 
