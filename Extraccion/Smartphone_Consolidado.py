import time
import os.path

def checkArchivo(ruta):
    if os.path.exists(ruta):
        print("El Archivo Existe :"+ruta)
        return True
    else:
        print("El Archivo no Existe :"+ruta)
        return False

def consolidar(consolidado,ruta):
    if not checkArchivo(consolidado):
        con=open(consolidado,"w")
        print("Se ha creado el Archivo Consolidado")
    else:
        con=open(consolidado,"a")
    if checkArchivo(ruta):
        Data=open(ruta,"r")
        for row in Data:
            cols=row.split("|")
            s=""
            for  i in cols[:7]:
                s=s+i+"|"
            s=s+cols[7]
            con.write(s.replace("\n","").replace(","," ")+"\n")
        Data.close()
    else:
        print("No se ha encontrado el archivo de fuente de datos "+ruta)
    con.close()

def main():
	fecha=time.strftime("%d-%b-%y")
	consolidado="/home/ETL_v2/Extraccion/Data/Consolidado.csv"
	path="/home/ETL_v2/Extraccion/Data/"
	origen=["linio","LS","olx","Ri","wong","ML","RS","SF"]
	for o in origen:
		print(o)
		consolidar(consolidado,path+"Smartphone_"+o+"_pe_"+fecha+".csv")

main()





