#!/usr/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

s=requests.session()
url="https://www.collinsdictionary.com/dictionary/english-hindi/"
url2="https://dict.hinkhoj.com/hindi-dictionary.php?word="
if sys.argv[1] is not None:
	word=sys.argv[1]
try:
	se=sys.argv[2]
except Exception as e:
	se='h'

if(se=='c' or se=='a'):
	print("collinsdictionary: ")
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
	print('\n')

if(se=='h' or se=='a'):
	print("HindiKhoj: ")
	tmp=s.get(url2+word)
	cont=str(tmp.content.decode())
	soup =BeautifulSoup(cont, 'html.parser')
	mydivs = soup.findAll("a", {"class": "hin_dict_span"})
	for i in mydivs:
		print(i.find('span').contents[0])
