import requests as req
import sys
from bs4 import BeautifulSoup

args = sys.argv
print(args)
if(len(args) == 2):
	url = args[1]
	page = req.get(url);
	print(page.text.encode('utf-8'))