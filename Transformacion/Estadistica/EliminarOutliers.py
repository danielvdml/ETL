import json
import math
import os.path

def getTC(moneda):
	if moneda=="$":
		return 3.42
	else:
		return 1.0

def getQuartil(array):
	array.sort()
	l=len(array)
	quartiles={"Q1":array[int(l/4)],"Q2":array[int(l/2)],"Q3":array[int((3*l)/4)],"RI":abs(array[int(l/4)]-array[int((3*l)/4)])}
	return quartiles
def getmedia(array):
	x=0
	for a in array:
		x=x+a
	return x/len(array)

def getDS(array):
	x=getmedia(array)
	var=0
	for a in array:
		var=var+(a-x)**2
	ds=math.sqrt(float(var/len(array)))
	return ds

def getInfEst(array):
	return {"media":getmedia(array),"DS":getDS(array)}

# def cleanOurliers(Li,Ls,lista):
# 	for i in lista:


def getEstadistica(dic):
	for d in dic:
		N=len(dic[d])
		if N>0:
			Q=getQuartil(dic[d])
			Li=Q["Q1"]-Q["RI"]*1.5
			Ls=Q["Q3"]+Q["RI"]*1.5
			l=[i for i in dic[d] if (i>=Li and i<=Ls)]			
			IE=getInfEst(l)
			if N>=4:
				Li=IE["media"]-1.96*IE["DS"]
				Ls=IE["media"]+1.96*IE["DS"]
			# elif N>=6:
			# 	Li=Q["Q1"]-Q["RI"]*1.5
			# 	Ls=Q["Q3"]+Q["RI"]*1.5
			else:
				Li=min(dic[d])
				Ls=max(dic[d])
			dic[d]={"item":d,"media":IE["media"],"DS":IE["DS"],"Li":Li,"Ls":Ls,"N":N,"precios":dic[d]}
	return dic

def toJson(dic):
	Est=open("Estadistica.json","w",errors="ignore")
	JS=json.dumps(dic)
	Est=Est.write(JS)
	return "Listo"

def main():
	consolidado=open("../Data/Consolidado.csv","r",errors="ignore")
	dic={}
	for c in consolidado:
		cad=c.split(",")
		try:
			dic[cad[1]+"|"+cad[2]+"|"+cad[9]].append(float(cad[6])*getTC(cad[8]))
		except Exception as e:
			dic[cad[1]+"|"+cad[2]+"|"+cad[9]]=[]
	toJson(getEstadistica(dic))
	
main()


	