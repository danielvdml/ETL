
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json

fecha=time.strftime('%d-%b-%y')
data=open("Data/Smartphone_linio_pe_"+fecha+".csv","w")
data.write("id|origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen|preciOld\n")

exit=True
i=0
cont=0
condicion="nuevo"
moneda=""
monedaSimbolo=""
while exit:
	i=i+1
	html=urlopen("https://www.linio.com.pe/c/celulares-y-smartphones/smartphones?empty=true&lazy=true&page="+str(i))
	bsObj=BeautifulSoup(html,"html.parser")
	items=bsObj.findAll("div",{"class":"catalog-product-item"})
	if len(items)>0:
		for item in items:
			cont=cont+1
			try:
				link=item.find("a")["href"]
			except Exception as e:
				link=""
			try:							
				titulo=item.find("a")["title"]
			except Exception as e:
				titulo=""
			try:
				precioOld=item.find("span",{"class":"previous-price"}).text.replace("S/.","").replace(",","").strip()			
			except Exception as e:
				precioOld=""
			try:
				precioNew=item.find("span",{"class":"actual-price"}).text.replace("S/.","").replace(",","").strip()
			except Exception as e:
				precioNew=""
			try:			
				imagen=item.find("img",{"class":"responsive"})["data-echo"]
			except Exception as e:
				imagen=""
			try:
				if item.find("span",{"class":"actual-price"}).text.find("S/.")>0:
					moneda="Sol"
					monedaSimbolo="S/."
				if item.find("span",{"class":"actual-price"}).text.find("$")>0:	
					moneda="Dolar"
					monedaSimbolo="$"
			except Exception as e:
				moneda=""
				monedaSimbolo=""
			
			s=str(cont)+"|"+"li"+"|"+titulo+"|"+link+"|"+precioNew+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"|"+precioOld+"\n" 
			data.write(s)
			print(s)
	else:
		exit=False

data.close()
