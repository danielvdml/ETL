import json
data=open("../CatalogoTop.csv","r")
DataJson=open("Catalogo_1.json","w")
dic=dict()
for d in data:
	s=d.replace("\n","").split("|")
	dic[s[0]]=s[1]
Json=json.dumps(dic)
DataJson.write(Json)
DataJson.close()
data.close()


