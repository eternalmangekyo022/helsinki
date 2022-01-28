




#1.feladat
class adatok:
    helyezes=0
    fo=0
    snev=''
    verseny=''
#2.feladat
lista=[]
f=open('helsinki.txt','r')
for i in f:
    a=adatok()
    sor=i.strip().split()
    a.helyezes=sor[0]
    a.fo=sor[1]
    a.snev=sor[2]
    a.verseny=sor[3]
    lista.append(a)
f.close()
#3.feladat
print('3.feladat:')
print('Pontszerző helyezések száma:',len(lista))
#4.feladat
print('4.feladat:')
a=0
e=0
b=0
for i in lista:
    if i.helyezes=='1':
        a=a+1
    elif i.helyezes=='2':
        e=e+1
    elif i.helyezes=='3':
        b=b+1
print('Arany:',a)
print('Ezüst:',e)
print('Bronz:',b)
print('Összesen:',a+e+b)
#5.feladat
print('5.feladat:')
ossz=0
for i in lista:
    if i.helyezes=='1':
        ossz=ossz+7
    elif i.helyezes=='2':
        ossz=ossz+5
    elif i.helyezes=='3':
        ossz=ossz+4
    elif i.helyezes=='4':
        ossz=ossz+3
    elif i.helyezes=='5':
        ossz=ossz+2
    elif i.helyezes=='6':
        ossz=ossz+1
print('Olimpiai pontok száma:',ossz)
#6.feladat
print('6.feladat:')
