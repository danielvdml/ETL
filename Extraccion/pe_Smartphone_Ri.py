from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests

def worker(url,data):
	# html=urlopen(url)
	html=requests.get(url)
	bsObj=BeautifulSoup(html.text,"html.parser")
	items=bsObj.findAll("div",{"class":"product"})
	condicion="nuevo"
	
	for item in items:

		try:
			titulo=item.find("div",{"class":"product_name"}).find("a").text.strip()
		except Exception as e:
			titulo=""
		try:
			link=item.find("div",{"class":"product_name"}).find("a")["href"]
		except Exception as e:
			link=""

		try:
			if item.find("div",{"class":"product_price"}).find("div",{"class":"price"}).text.find("S/.")>=0:
				moneda="S/."
				monedaSimbolo="Sol"
				precio=item.find("div",{"class":"product_price"}).find("div",{"class":"price"}).text.replace("S/.","").strip()
			else:
				moneda=""
				monedaSimbolo=""
				precio="0.0"
		except Exception as e:
			moneda=""
			monedaSimbolo=""
			precio="0.0"

		try:
			imagen="http://www.ripley.com.pe"+item.find("img")["data-original"]
		except Exception as e:
			imagen=""
		if titulo!="":
			s="Ripley"+"|"+titulo+"|"+link+"|"+precio+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"\n"
			data.write(s)
			print(s)

def main(dominio):
	fecha=time.strftime("%d-%b-%y")
	data=open("Data/Smartphone_Ri_"+dominio+"_"+fecha+".csv","w")
	data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen\n")
	url="http://www.ripley.com.pe/ripley-peru/SearchDisplay?urlRequestType=Base&storeId=10751&catalogId=10101&langId=-24&categoryId=266188&urlLangId=-24&beginIndex=0&pageSize=133"
	worker(url, data)
	data.close()
main("pe")