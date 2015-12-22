from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests
def worker(url,data):
	# html=urlopen(url)
	html=requests.get(url)
	bsObj=BeautifulSoup(html.text,"html.parser")
	items=bsObj.findAll("li",{"class":"item"})
	condicion="nuevo"
	for item in items:

		try:
			titulo=item.find("h2",{"class":"product-name"}).find("a")["title"]
		except Exception as e:
			titulo=""
		try:
			link=item.find("h2",{"class":"product-name"}).find("a")["href"]
		except Exception as e:
			link=""

		try:
			if item.find("p",{"class":"special-price"}).find("span",{"class":"price"}).text.find("S/.")>=0:
				moneda="S/."
				monedaSimbolo="Sol"
				precio=item.find("p",{"class":"special-price"}).find("span",{"class":"price"}).text.replace("S/.","").replace(",",".").strip()		     
			else:
				moneda=""
				monedaSimbolo=""
				precio="0.0"
		except Exception as e:
			if item.find("span",{"class":"regular-price"}).find("span",{"class":"price"}).text.find("S/.")>=0:
				moneda="S/."
				monedaSimbolo="Sol"
				precio=item.find("span",{"class":"regular-price"}).find("span",{"class":"price"}).text.replace("S/.","").replace(",",".").strip()
			else:
				moneda=""
				monedaSimbolo=""
				precio=""

		try:
			imagen=item.find("a",{"class":"product-image"}).find("img")["src"]
		except Exception as e:
			imagen=""

		s="LoginStore"+"|"+titulo+"|"+link+"|"+precio+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"\n"
		data.write(s)
		print(s)

def main(dominio):
	fecha=time.strftime("%d-%b-%y")
	data=open("/home/ETL_v2/Extraccion/Data/Smartphone_LS_"+dominio+"_"+fecha+".csv","w")
	data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen\n")
	url="https://www.loginstore.com/celulares-telefonia/smartphones?limit=all"
	worker(url, data)
	data.close()
main("pe")
