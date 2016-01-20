# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
url="http://es.gsmchoice.com/es/catalogo/"
Marcas=["Nokia","Motorola","Samsung","Sony","LG","HTC","Blackberry","Alcatel","Huawei","apple","Lenovo","Asus"]
data=open("CatalogoGSMchoice.json","w")
idcont=0
dic={}
for marca in Marcas:
	html = urlopen(url+marca)
	bsObj = BeautifulSoup(html,"html.parser")
	modelos=bsObj.find("select",{"id":"InfoLineModelSelector"})
	for modelo in modelos.findAll("option"):
		if modelo.text.find("selecciona un modelo")==-1:
			dic[idcont]=modelo.text
			idcont=idcont+1
			print(modelo.text)

d=json.dumps(dic)
data.write(d)
data.close()
