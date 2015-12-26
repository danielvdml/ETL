import  json

def max(D):
    max=0
    for d in D:
        if D[d]	>= max:
            max=D[d]
            cod=d
    return {"max":max,"cod":cod}


def main():
    consolidado=open("/home/ETL_v2/Extraccion/Data/Consolidado.csv","r")
    NewConsolidado=open("/home/ETL_v2/Transformacion/Data/Consolidado.csv","w")
    with open("/home/ETL_v2/Transformacion/Clasificacion/PalabrasIndexadas.json") as file:
        catalogo=json.load(file)
    with open("/home/ETL_v2/Transformacion/Clasificacion/Utilitarios/Catalogo_1.json") as file2:
        catalogo_1=json.load(file2)
    for con in consolidado:
        try:
            s=con.split("|")
            tit=s[1]
            cod=dict()
            for cat in catalogo:
                if (" "+tit+" ").lower().find(" "+cat.lower()+" ")>=0:
                    for c in catalogo[cat]:
                        try:
                            cod[c]=cod[c]+1
                        except Exception as e:
                            cod[c]=1
            maxcod=max(cod)
            modelo=catalogo_1[maxcod["cod"]]
            marca=modelo.split(" ")[0]
            if maxcod["max"]>=len(modelo.split(" ")):
                NewConsolidado.write(str(maxcod["cod"])+"|"+marca+"|"+modelo.replace(marca,"").strip()+"|"+con)
        except Exception as e:
            pass
    NewConsolidado.close()
    consolidado.close()
main()
