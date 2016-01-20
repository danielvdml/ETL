import json

IndexItemJson=open("IndexItem.json","w")
with open("CatalogoGSMchoice.json","r",errors="ignore") as fileJson:
	dicCatalogoGSM=json.load(fileJson)

IndexItems={}
for item in dicCatalogoGSM:
	cad=dicCatalogoGSM[item].split(" ")
	for c in cad:
		c=" "+c+" "
		try:
			IndexItems[c].append(item)
		except Exception as e:
			IndexItems[c]=[]
			IndexItems[c].append(item)

CatalogoJSon=json.dumps(IndexItems)
IndexItemJson.write(CatalogoJSon)
IndexItemJson.close()
