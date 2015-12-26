import json

Catalogo=open("/home/ETL_v2/Transformacion/Clasificacion/CatalogoTop.csv","r")
CatalogoIndex=open("/home/ETL_v2/Transformacion/Clasificacion/PalabrasIndexadas.json","w")
dic=dict()

for cat in Catalogo:
	s=cat.replace("-"," ").replace(" GB","GB").replace("GB"," GB").replace("\n","").lower().split("|")
	cad=s[1].split(" ")
	for i in cad:
		try:
			dic[i].append(s[0])
		except Exception as e:
			dic[i]=[]
			dic[i].append(s[0])
json1=json.dumps(dic,ensure_ascii=False)
CatalogoIndex.write(json1)
CatalogoIndex.close()
Catalogo.close()
