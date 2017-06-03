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

To run this script, you'll need [Python 3.x](https://www.python.org/downloads/) installed and [pip](https://pip.pypa.io/en/stable/installing/) to get the packages

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

## Testing

The file `crawler_test.py` is a *test suit* that was created to be used with the library [pytest](https://docs.pytest.org/en/latest/getting-started.html) 

Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) by running in your terminal `pip install pytest`

Then, on the root folder of this project, run the terminal command `pytest`. It will automatically look for and run tests files (that follow a naming convention)
