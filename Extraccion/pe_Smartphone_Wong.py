from bs4 import BeautifulSoup
import time
from urllib.request import urlopen


def worker(url,data):
	html=urlopen(url)	
	bsObj=BeautifulSoup(html,"html.parser")
	items=bsObj.findAll("li",{"class":"tecnologia"})
	condicion="nuevo"
	for item in items:
		try:
			link=item.find("h3").find("a")["href"]
		except Exception as e:
			link=""

		try:
			imagen=item.find("div",{"class":"photo"}).find("img")["src"]
		except Exception as e:
			imagen=""
		
		try:
			titulo=item.find("h3").find("a")["title"]
		except Exception as e:
			titulo=""

		try:
			
			if item.find("em",{"class":"valor-por"}).text.find("S/.")>=0:
				moneda="sol"
				monedaSimbolo="S/."				
				precio=item.find("em",{"class":"valor-por"}).text.replace("S/.","").replace("Online:","").replace(",","").strip()
			else:
				moneda=""
				monedaSimbolo=""
				precio="0.0"	
		except Exception as e:
			moneda=""
			monedaSimbolo=""
			precio=""
		s="Wong"+"|"+titulo+"|"+link+"|"+precio+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"\n"
		data.write(s)
		print(s)


def main():
	s=time.strftime('%d-%b-%y')
	data=open('Data/Smartphone_wong_pe_'+s+'.csv','w')
	data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen\n")
	url="http://tienda.wong.com.pe/buscapagina?fq=C%3a%2f1000144%2f1000230%2f1000231%2f&PS=12&sl=ef3fcb99-de72-4251-aa57-71fe5b6e149f&cc=3&sm=0&PageNumber=1"	
	worker(url,data)
	data.close()

main()