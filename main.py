import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


@app.route('/')
def home():
	site = 'http://talkobamato.me/synthesize.py'
	text = {'input_text': get_fact()}

	r = requests.post(url=site,
						data = text,
						allow_redirects = False)

	h = r.headers['Location']

	return h


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug=True)

