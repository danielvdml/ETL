from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests

def worker(url,data):
	# html=urlopen(url)
	html=requests.get(url)
	bsObj=BeautifulSoup(html.text,"html.parser")
	items=bsObj.findAll("a",{"class":"item-t1"})
	condicion="nuevo"
	
	for item in items:

		try:
			titulo=item.find("div",{"class":"text"}).text.strip()
		except Exception as e:
			titulo=""
		try:
			link="http://www.radioshackperu.com.pe"+item["href"]
		except Exception as e:
			link=""

		try:
			
			if item.find("div",{"class":"w-precio"}).text.find("S/.")>=0:
				moneda="S/."
				monedaSimbolo="Sol"
				precio=item.find("div",{"class":"w-precio"}).text.replace("S/.","").replace(" ","").strip()
			else:
				moneda=""
				monedaSimbolo=""
				precio="0.0"
		except Exception as e:
			moneda=""
			monedaSimbolo=""
			precio="0.0"

		try:
			imagen="http://www.radioshackperu.com.pe"+item.find("img")["src"]
		except Exception as e:
			imagen=""

		s="RadioShack"+"|"+titulo+"|"+link+"|"+precio+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"\n"
		data.write(s)
		print(s)

def main(dominio):
	fecha=time.strftime("%d-%b-%y")
	data=open("Data/Smartphone_RS_"+dominio+"_"+fecha+".csv","w")
	data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen\n")
	url="http://www.radioshackperu.com.pe/catalogo/telefonia/celulares-desbloqueados?page="
	for i in range(1,4):
		print(i)
		worker(url+str(i), data)
	data.close()
main("pe")