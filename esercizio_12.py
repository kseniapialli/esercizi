#si vuole creare un programma che leggendo da un file di testo contenente una serie di valori
#misurati di temperature, calcoli la media, la varianza e la mediana della distribuzione

#sottoproblemi
#1) leggere il file riga per riga e creare una lista
#2) calcolo della media della lista
#2) calcolo la varianza di una lista
#3) calcolo la mediana di una lista

def leggiFile(pathInpu): #gli passo il percorso come variabile
    temperature=[]
    with open(pathInput) as f:
        for line in f: #per tutte le righe che trovo all'interno del file
            temperature.append(int(line.strip())) #con int la converto ad intero e con strip tolgo l'andata a capo
    #elemento=int(line.strip())
    #temperature.append(elemento)
    return(temperature)

#media con l'uso del ciclo for
def media(lista):
    somma=0
    for i in range(0,len(lista)):
        somma=somma+lista[i]
    media_c=somma/len(lista)
    print(media_c)
    
#media con l'uso dell'interatore
def media_iterator(lista):
    somma=0
    for element in lista:
        somma=somma+element
    media_c=somma/len(lista)
    print(media_c)
    
def varianza(dati):
    n=len(dati)
    return(media)
scarti_quadrati=[(x-media)**2 for x in dati]
return sum(scarti_quadrati)/n
print(varianza)
#richiamo la funzione
lista=leggiFile("temperature.cvs")
#richiamo la procedura
media(lista)
media_iterator(lista)

    

            