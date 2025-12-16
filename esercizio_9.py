#scrivere un programma che calcoli il minimo e il massimo di una lista lunghezza n
#di interi e random compresi nell'intervallo 0,100.

#sottoproblemi:
#1)calcolare il minimo di una lista
#2)calcolare il massimo di una lista
#3)generare una lista di n numeri random nell'intervallo 0,100

import random

def generaLista(n):
    myList=[]
    for i in range (0,n):
        elemento=random.randint(0,100)
        myList.append(elemento)
    return(mylist)

def minimoLista(lista,n):
    minimo=lista[0]
    for i in range (1,n):
        if lista[i]<minimo:
            minimo=lista[i]
    print(minimo)

def massimoLista(lista,n):
    massimo=lista[0]
    for i in range (1,n):
        if lista[i]>massimo:
            massimo=lista[i]
    print(massimo)

#decoratore che serve per esplicitare qualcosa che tiene nascosto. il programma inizia sempre invocando main
if__name__=="__main__":
    dimensione=10
    listaBella=generaLista(dimensione)
    minimoLista(listaBella,dimensione)
    massimoLista(listaBella,dimensione)
