#!-*-coding:utf-8-*-
import requests
import os
import hashlib
import argparse
from readability import Document
#url = "https://www.quantamagazine.org/new-bird-species-arises-from-hybrids-as-scientists-watch-20171213/"
#response = requests.get(url)
SAVE_DIR = os.path.join(os.path.dirname(__name__), "html", "result")

def parse_summary(filename=None,url=None):
	if filename:
		with open(filename,"r") as f:
			html = f.read()
		n = "content_%s"%os.path.basename(filename)
	if url:
		html = request.get(url)
		n = "url_content_%s_.html"%hashlib.md5(url.encode("utf-8")).hexdigest()[0:6]
	doc = Document(html)
	summary = doc.summary()
	fn = os.path.join(SAVE_DIR, n)
	with open(fn, 'w') as f:
	    f.write(summary)


if __name__ == "__main__":
	parse = argparse.ArgumentParser()
	parse.add_argument('-f',"--file",help="set file to parse")
	parse.add_argument("-l", "--url", help="set url link to parse")
	args = parse.parse_args()
	if args.file:
		filename = args.file
		parse_summary(filename=filename)
		print("parse success")
	else :
		if args.url:
			url = args.url
			parse_summary(url=url)
			print("parse success")