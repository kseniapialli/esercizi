#problema: data una serie di 10 misurazioni randomiche intere, comprese tra 2 intervalli forni da tastiera
#produrre in output un file di testo che abbia i valori, la media dei valori, il numero di valori sopra
#una certa soglia fissata a massimo delle misurazioni -10

#sotoproblemi:
#1)creare una lista di 10 misurazioni random (procedura perche le liste sono passate per riferimento)
#2)media dei valori di una lista (funzione)
#3)calcolare la soglia [massimo lista -10] (funzione)
#4)contare il numero di valori sopra la soglia (procedura)

import random

def creaLista(lista):
    n1=input("Inserire il primo estremo ") #con input tiriamo su una stringa
    n1=int(n1)
    n2=input("Inserire il secondo estremo ")
    n2=int(n2)
    
    for i in range(0,10):
        if n1<n2:
            valori=random.randint(n1,n2)
        else:
            valori=random.randint(n1,n2)
        lista.append(valori)
        
def calcoloMedia(lista):
    somma=0
    for i in range(0,len(lista)): 
        somma=somma+lista[i]
        
    media=somma/len(lista)
    return(media)
        
if __name__=="__main__":
    listaM=[]
    creaLista(listaM) #inserisco tra parentesi il parametro reale
    mediaValori=calcolo_media(listaM)