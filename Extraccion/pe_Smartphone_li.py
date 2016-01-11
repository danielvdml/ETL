from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json

fecha=time.strftime('%d-%b-%y')
data=open("/home/ETL_v2/Extraccion/Data/Smartphone_linio_pe_"+fecha+".csv","w")
data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen|preciOld\n")

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
                link=item.find("div",{"class":"catalog-product-title"}).find("a")["href"]
            except Exception as e:
                print("Error Link :"+e)
                link=""
            try:
                titulo=item.find("div",{"class":"catalog-product-title"}).find("a")["title"]
            except Exception as e:
                titulo="--"
            try:
                precioOld=item.find("span",{"class":"previous-price"}).text.replace("S/.","").replace(",","").strip()
            except Exception as e:
                precioOld="0.0"
            try:
                precioNew=item.find("span",{"class":"actual-price"}).text.replace("S/.","").replace(",","").strip()
            except Exception as e:
                print("error")
                precioNew="0.0"
            try:
                imagen=item.find("figure",{"class":"main-figure"}).find("img")["data-echo"]
            except Exception as e:
                print("error")
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
            s="li"+"|"+titulo+"|"+link+"|"+precioNew+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"|"+precioOld+"\n"
            data.write(s)
    else:
        exit=False

data.close()
