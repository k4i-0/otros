#Diccionario con rut chileno sin digito verificador
from io import open
import os
import math

def verificacionrut (lista):
    #invierte lista
    l = list(reversed(lista))
    # crea lista con numeros de 2 a 7
    l2 = [2,3,4,5,6,7,2]
    #crea lista vacia
    l3 = []
    #multiplica cada elemento de la lista por cada elemento de la lista l2
    for i in range(len(lista)):
        l3.append(int(l[i])*int(l2[i]))
    #suma los elementos de la lista l3
    suma = sum(l3)
    #divide la suma por 11
    div = suma/11
    #redondea el resultado hacia arriba
    div = math.trunc(div)
    #multiplica el resultado de la division por 11
    div = div*11
    #resta el resultado de la suma por el resultado de la multiplicacion
    resta = suma-div
    #resta el resultado de la resta por 11
    resta = 11-resta
    #si el resultado de la resta es 10, el digito verificador es K
    #si el resultado de la resta es 11, el digito verificador es 0
    if resta == 10:
        return "K"
    if resta == 11:
        return 0
    return resta

def listInt(lista):
    #transforma lista en int
    aux = None
    for i in lista:
        if (aux == None):
            aux = str(i)
        else:
            aux = aux + str(i)

    aux = int(aux)
    return aux


#progrma pincipal
#dicionario
dic = ""

#define lista rut inicial
lista = [3,0,0,0,0,0,0]
#define rut de termino
rutTermino = 27000000
#variable de control
control = 0

#mientas la condicion no se cumple, se ejecuta el codigo
while(control != 1):
    #transforma lista en int
    temp = listInt(lista)
    #condicion de termino
    if( temp == rutTermino):
        control = 1
    #suma 1
    temp = temp + 1
    #transforma int a string
    temp = str(temp)
    #transforma string a lista
    lista = list(temp)
    #llama a la funcion verificacionrut
    digito = verificacionrut(lista)
    if (digito == "K"):
        i = listInt(lista)
        dic = dic + str(i) + "K" + "\n"
        print(dic)
    else:
        #agrega el digito verificador a la lista
        lista.append(digito)
        #transforma lista en int
        ingresar = listInt(lista)
        #agrega el rut y el digito verificador al diccionario
        dic = dic + str(ingresar) + "\n"
        #imprime el diccionario
        print(dic)
        lista.pop()

#crea archivo
archivo = open("dic_rut.txt","w")
#escribe en el archivo
archivo.write(dic)
#cierra el archivo
archivo.close()
