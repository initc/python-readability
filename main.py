#!-*-coding:utf-8-*-
import requests
import os
from readability import Document
#url = "https://www.quantamagazine.org/new-bird-species-arises-from-hybrids-as-scientists-watch-20171213/"
#response = requests.get(url)
with open("origin.html","r") as f:
    text = f.read()
doc = Document(text)
summary = doc.summary()
content = doc.content()
title = doc.title()
short_title = doc.short_title()
dir_name = os.path.join(os.path.dirname(__name__),'html')
fp = os.path.join(dir_name,"summary_new-bird-species-20171213.html")
with open(fp,'w') as f:
    f.write(summary)
fp = os.path.join(dir_name,"content_new-bird-species-20171213.html")
with open(fp,'w') as f:
    f.write(content)
fp = os.path.join(dir_name,"short_title__new-bird-species-20171213.html")
with open(fp,'w') as f:
    f.write(short_title)
fp = os.path.join(dir_name,"title__new-bird-species-20171213.html")
with open(fp,'w') as f:
    f.write(title)
fp = os.path.join(dir_name,"origin__new-bird-species-20171213.html")
with open(fp,'w') as f:
    f.write(text)
