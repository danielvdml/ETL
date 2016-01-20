import json
import re

def lcs(a, b):
    a=a.lower()
    b=b.lower()
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

consolidado=open("../../Data/Consolidado_1.csv","r",errors="ignore")
correccion=open("dicCorre.json","w",errors="ignore")
dic={}
for c in consolidado:
    tod=c.split(";")
    cad=re.sub('[!@#$.-]','',tod[2]).lower().split(" ")
    for pal in cad:
        try:
            dic[pal]=dic[pal]+1
        except Exception as e:
            dic[pal]=0

l=dic.items()
l.sort(lambda x,y:cmp(x[1], y[1]))
for i in l:
    try:
        print(i)
    except Exception as e:
        pass
    
corr={}
for i in list(dic):
    for j in list(dic):
        try:
            if 2*len(lcs(i, j))/(len(j)+len(i))>=0.85:
                print(corr)
                if dic[j]>dic[i]:
                    try:
                        if not i in corr[j]:
                            corr[j].append(i)
                            del dic[i]
                    except Exception as e:
                        corr[j]=[]
                        corr[j].append(i)
                        del dic[i]
                else :
                    try:
                        if not j in corr[i]:
                            corr[i].append(j)
                            del dic[j]
                    except Exception as e:
                        corr[i]=[]
                        corr[i].append(j)
                        del dic[j]
        except Exception as e:
            pass
corrJson=json.dumps(corr)
correccion.write(corrJson)
correccion.close()
consolidado.close()

