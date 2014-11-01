'''
========

Aim of this file is to find wikipedia articles of the
keywords that it gets from wt_init_parse
It's main aim is not to get the content
but to see if the wiki page exists.

We may use wiki search, their api or create our
own detection methodology, this is up for discussion.

========

'''

import requests as req
import sys
from bs4 import BeautifulSoup

arguments = sys.argv
BASE_URL = "http://en.wikipedia.org/wiki/"
#read = BASE_URL+read.replace(' ', '_')
if(len(args) > 1):
	url = args[1]
	page = req.get(url);
	print(page.text.encode('utf-8'))