#Scheda 1
#1. Crea una lista chiamata numeri con i numeri da 1 a 5. Stampa il terzo elemento (indice 2).
#2. Modifica il secondo elemento di numeri in 10. Stampa la lista aggiornata.
#3. Aggiungi il numero 6 alla fine della lista usando append. Stampa la lunghezza della lista.
#4. Crea una lista mista con 3 stringhe e 2 numeri. Stampa l'ultimo elemento (usa len per calcolarlo).

#1
numeri=[1,2,3,4,5]
print(numeri[2])
#2
numeri[1]=10
print(numeri)
#3
numeri.append(6)
print(numeri)
print(len(numeri))
#4
mista=["uno","due","tre",1,2]
print(mista[len(mista)-1])

#Scheda 2
#1. Data la lista colori = ["rosso", "blu", "verde", "giallo", "nero"], estrai i primi due colori con slicing.
#2. Estrai gli ultimi tre colori.
#3. Inserisci "bianco" all'indice 1. Stampa la lista.
#4. Rimuovi "verde" e stampa la lunghezza della lista aggiornata.

#1
colori=["rosso","blu","verde","giallo","nero"]
print(colori[0:2])
#2
print(colori[2:])
#3
colori.insert(1,"bianco")
print(colori)
#4
colori.remove("verde")
print(len(colori))

#Scheda 3
#1. Usa range(10) in un ciclo for per stampare i numeri da 0 a 9.
#2. Stampa i numeri da 5 a 15 (inclusi 5, escluso 16).
#3. Stampa i multipli di 3 da 0 a 30 usando step=3.
#4. Crea un ciclo che stampi "Ciao" 7 volte usando range.

#1
for i in range(10):
    print(i)
#2   
for i in range(5,16):
    print(i)
#3    
for i in range(0,31,3):
    print(i)
#4    
for i in range(7):
    print("Ciao")
    
#Scheda 4
#1. Data città = ["Roma", "Milano", "Napoli", "Torino"], usa un ciclo con range(len(città)) per stampare ogni città con il suo indice.
#2. Crea una lista di 5 numeri. Usa un ciclo per raddoppiare ciascun numero e stampa la lista modificata.
#3. In una lista di stringhe, usa un ciclo per aggiungere "!" alla fine di ciascuna (es. "ciao" -> "ciao!").
#4. Crea una lista vuota, poi usa un ciclo con range(5) per aggiungere numeri da 1 a 5 con append.

#1
città=["Roma","Milano","Napoli","Torino"]
for i in range(len(città)):
    print(f"Città all'indice{i}:{città[i]}")
#2   
lista=[1,2,3,4,5]
for i in range(len(lista)):
    lista[i]=lista[i]*2
print(lista)
#3
stringhe=["uno","due","tre"]
for i in range(len(stringhe)):
    stringhe[i]=stringhe[i]+"!"
print(stringhe)
#4
lista=[]
for i in range(5):
    lista.append(i+1)
print(lista)
    
#Scheda 5
#1. Crea una lista di 10 numeri casuali (usa range per generarli). Calcola la somma con un ciclo.
#2. Filtra una lista: data [10, 15, 20, 25, 30], crea una nuova lista solo con numeri > 20 usando un ciclo e if.
#3. Genera una lista di quadrati da 1 a 10 (es. [1, 4, 9, ...]) con range e append.
#4. In una lista di nomi, usa un ciclo per stampare solo quelli che iniziano con "A" (usa if e slicing).

#1
import random
lista=[]
for i in range(10):
    numeri=random.randint(0,10)
    lista.append(numeri)
print(lista)       
somma=0
for i in range(len(lista)):
    somma=somma+lista[i]
print(somma)
#2
lista=[10,15,20,25,30]
listaFiltrata=[]
for i in range(len(lista)):
    if lista[i]>20:
        listaFiltrata.append(lista[i])
print(listaFiltrata)
#3
quadrati=[]
for i in range(1,11):
    quadrati.append(i*i)
print(quadrati)
#4
nomi=["Anna","Chiara","Sofia","Sara","Alessia"]
for i in range(len(nomi)):
    if nomi[i][0:1]=="A":
        print(nomi[i])

#· Livello base: Scrivi un programma che genera una lista di multipli di un numero dato (es. multipli di 5 fino a 50).
#· Livello avanzato: Simula un registro di classe: lista di nomi studenti, usa ciclo per assegnare voti casuali (con range) e calcola la media classe.

#Livello base
numero=5
multipli=[]
for i in range(5,50,5):
    multipli.append(i)
print(multipli)
#Livello avanzato
import random
studenti=["Chiara","Sofia","Sara","Luca","Marco"]
voti=[]
for i in range(len(studenti)):
    voti.append(random.randint(0,10))
print(voti)

somma=0
for i in range(len(voti)):
    somma=somma+voti[i]
    media=somma/len(voti)
print(media)








