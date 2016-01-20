import json

consolidado=open("../../Data/Consolidado_1.csv","r",errors="ignore")
with open("IndexItem") as fileIndex:
	IndexItemDic=json.load(fileIndex)

for reg in consolidado:
	for indexItem in IndexItemDic:


