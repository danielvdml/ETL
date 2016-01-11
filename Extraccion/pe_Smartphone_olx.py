
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests
import random

fecha=time.strftime("%d-%b-%y")
data=open("/home/ETL_v2/Extraccion/Data/Smartphone_olx_pe_"+fecha+".csv","w")
i=0
exit=True
cont=0
data.write("origen|titulo|link|precio|moneda|monedaSimbolo|condicion|imagen|lugar\n")
while exit:
    i=i+1
    if i%20==0:
        time.sleep(60)
    url="http://www.olx.com.pe/telefonos-celulares-cat-831-p-"+str(i)
    html=requests.get(url)
    bsObj=BeautifulSoup(html.text,"html.parser")
    items=bsObj.findAll("li",{"class":"item"})
    if len(items)>0:
        for item in items:
            cont=cont+1
            try:
                link=item.find("a")["href"]
            except Exception as e:
                link=""
            try:
                imagen=item.find("img")["src"]
            except Exception as e:
                imagen=""
            try:
                titulo=item.find("h3").text.strip()
                if titulo.lower().find("nuevo"):
                    condicion="nuevo"
                if titulo.lower().find("usado"):
                    condicion="usado"
            except Exception as e:
                titulo=""
            try:
                precio=item.find("p",{"class","items-price"}).text.replace("S/.","").replace(".","").replace("Negociable","").strip()
            except Exception as e:
                precio="0.0"
            try:
                lugar=item.find("span").text
            except Exception as e:
                lugar=""
            try:
                if item.find("p",{"class":"items-price"}).text.find("S/.")>0:
                    moneda="Sol"
                    monedaSimbolo="S/."
                if item.find("p",{"class":"items-price"}).text.find("$")>0:
                    moneda="dolar"
                    monedaSimbolo="$"
            except Exception as e:
                moneda=""
                monedaSimbolo=""
            s="olx"+"|"+titulo+"|"+link+"|"+precio+"|"+moneda+"|"+monedaSimbolo+"|"+condicion+"|"+imagen+"|"+lugar+"\n"
            data.write(s)
    else:
        exit=False

data.close()
print("Fin")
