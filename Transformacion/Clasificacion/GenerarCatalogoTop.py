import json

data=open("/home/ETL_v2/Transformacion/Data/Consolidado.csv","r")
csv=open("/home/ETL_v2/Transformacion/Clasificacion/CatalogoTop.csv","w")
dic=dict()
for d in data:
	s=d.split("|")[0]+"|"+d.split("|")[1]+" "+d.split("|")[2]
	try:
		dic[s]=dic[s]+1
	except Exception as e:
		dic[s]=1
for d in dic:
    if dic[d]>=20:
        csv.write(d+"\n")
data.close()
csv.close()

