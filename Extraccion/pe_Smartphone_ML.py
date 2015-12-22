from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import threading


# Argentina  http://celulares.mercadolibre.com.ar
# Peru       http://celulares.mercadolibre.com.pe/_DisplayType_LF

def worker(inicial,final,urls,data,error,pais):
	for i in range(inicial,final):
		html=urlopen(urls[i])
		bsObj=BeautifulSoup(html,"html.parser")
		items=bsObj.findAll("li",{"class":"list-view-item"})
		for item in items:
				try:
					link=item.find("a",{"class":"item-link"})["href"]			
				except Exception as e:
					link=""
				try:
					htmlImage=urlopen(link)
					objImage=BeautifulSoup(htmlImage,"html.parser")
					itemImage=objImage.findAll("div",{"class":"first-image"})[0]			
					imagen=itemImage.find("img")["src"]
				except Exception as e:
					imagen=""
				try:
					titulo=item.find("a").text
				except Exception as e:
					titulo=""

				try:
					precio=float(item.find("strong",{"class":"ch-price"}).text.replace("S/.","").replace(".","").strip())/100.0
				except Exception as e:
					precio=0.0

				try:
					envio=item.find("span",{"class":"label"}).text
				except Exception as e:
					envio=""

				try:
					tipoVendedor=item.find("ul",{"class":"medal-list"}).find("li")["title"]
				except Exception as e:
					tipoVendedor=""

				try:
					condicion=item.find("li",{"class":"extra-info-condition"}).text
				except Exception as e:
					condicion=""

				try:
					cantidadVendida=item.find("li",{"class":"extra-info-sold"}).text.replace("vendidos","").strip()
				except Exception as e:
					cantidadVendida=""

				try:
					lugar=item.find("li",{"class":"extra-info-location"}).text
				except Exception as e:
					lugar=""

				try:
					if item.find("strong",{"class":"ch-price"}).text.find("S/.")>0:
						monedaSimbolo="S/."
						moneda="Sol"
					if item.find("strong",{"class":"ch-price"}).text.find("$")>0:
						monedaSimbolo="$"
						moneda="Dolar"
				except Exception as e:
					monedaSimbolo=""
					moneda=""
				try:
					s="ML"+"|"+titulo+"|"+link+"|"+str(precio)+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"|"+tipoVendedor+"|"+cantidadVendida+"|"+pais+"|"+lugar+"\n"
					data.write(s)
					print(s)
				except Exception as e:
					error.write(urls[i])
						

def main(nThreads,pais,dominio):
	fecha=time.strftime("%d-%b-%y")
	error=open("Data/Smartphone_ML_"+dominio+"_"+fecha+".error.csv","w")
	data=open("Data/Smartphone_ML_"+dominio+"_"+fecha+".csv","w")
	data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen|tipoVendedor|cantidadVendida|pais|lugar\n")
	threads=list()
	urls=list()
	for NPage in range(1,13961,50):
		urls.append("http://celulares.mercadolibre.com."+dominio+"/_Desde_"+str(NPage))
	N=len(urls)
	for i in range(nThreads):
		ini=int(N*(i-1)/nThreads)
		fin=int(N*(i)/nThreads)
		t=threading.Thread(target=worker,args=(ini,fin,urls,data,error,pais,))
		threads.append(t)
		t.start()
	

main(50,"Peru","pe")

