#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

s=requests.session()
url="https://www.collinsdictionary.com/dictionary/english-hindi/"
if sys.argv[1] is not None:
	word=sys.argv[1]
tmp=s.get(url+word)
cont=str(tmp.content.decode())
soup =BeautifulSoup(cont, 'html.parser')
mydivs = soup.findAll("span", {"class": "cit type-translation"})
for i in mydivs:
	soup=BeautifulSoup(str(i), 'html.parser')
	soup=BeautifulSoup(str(soup.find("span").contents), 'html.parser')
	span=soup.find('span').contents
	for i in span:
		print(i, end="\t")
