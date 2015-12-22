from bs4 import BeautifulSoup
import time
from urllib.request import urlopen


def worker(url,data):
	html=urlopen(url)	
	bsObj=BeautifulSoup(html,"html.parser")
	items=bsObj.findAll("div",{"class":"cajaLP4x"})
	condicion="nuevo"
	for item in items:
		try:
			link="http://www.falabella.com.pe"+item.find("div",{"class":"marca"}).find("a")["href"]
		except Exception as e:
			link=""

		try:
			imagen=item.find("img")["data-original"]
		except Exception as e:
			imagen=""
		
		try:
			titulo=item.find("img")["title"]
		except Exception as e:
			titulo=""

		try:
			precio=item.find("span",{"class":"unitPriceD"}).text.replace("S/.","").replace(",","").strip()
			if item.find("span",{"class":"unitPriceD"}).text.find("S/.")>=0:
				moneda="sol"
				monedaSimbolo="S/."				
			else:
				moneda=""
				monedaSimbolo=""
				precio="0.0"	
		except Exception as e:
			moneda=""
			monedaSimbolo=""
			precio=""
		s="Saga Fallabella"+"|"+titulo+"|"+link+"|"+precio+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"\n"
		data.write(s)
		print(s)


def main():
	s=time.strftime('%d-%b-%y')
	data=open('/home/ETL_v2/Extraccion/Data/Smartphone_SF_pe_'+s+'.csv','w')
	data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen\n")
	url="http://www.falabella.com.pe/falabella-pe/category/cat40591/Celulares?No=0&Nrpp=48"	
	worker(url,data)
	data.close()

main()
