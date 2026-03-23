#Scheda 1
#1. Definisci una funzione quadrato che prende un numero e restituisce il suo quadrato. Chiamala con 4 e stampa il risultato.
#2. Crea una funzione stampa_nome che prende un nome e stampa "Benvenuto, [nome]!". Chiamala con il tuo nome.
#3. Modifica somma per sommare tre numeri. Chiamala con 1, 2, 3.
#4. Scrivi una funzione massimo che prende due numeri e restituisce il maggiore (usa if).
#5. Create una funzione che calcola l'area di un rettangolo (lunghezza * larghezza). Testatela con valori diversi.

#1
def quadrato(numero):
    risultato=numero*numero
    print(risultato) 
#2
def stampa_nome(nome):
    print("Benvenuto "+nome+" !")      
#3
def somma(a,b,c):
    return(a+b+c)
#4
def massimo(uno,due):
    if uno>due:
        massimo=uno
    else:
        massimo=due
    return(massimo)
#5
def area(lunghezza,larghezza):
    area=lunghezza*larghezza
    print(area)
    
#Scheda 2
#1. Definisci una funzione potenza che prende base e esponente (default=2). Restituisce base^esponente. Chiamala con 3 (output:9) e con 3,3 (output:27).
#2. Crea benvenuto con parametri nome (obbligatorio) e eta (default=18). Stampa "Benvenuto [nome], hai [eta] anni.". Chiamala in entrambi i modi.
#3. Modifica calcola per avere a default=1. Chiamala senza argomenti.
#4. Scrivi una funzione media per due numeri, con secondo opzionale=0. Calcola (a + b)/2.
#5. Simulate un "calcolatore IVA": funzione con prezzo e iva (default=22%). Restituisce prezzo + IVA. Discutete casi d'uso.
    
#1
def potenza(base,esponente=2):
    return(base**esponente)
#2
def benvenuto(nome,eta=18):
    print(f"Benvenuto {nome}, hai {eta} anni.")
#3
def calcola(a=1,b=2,c=3):
    return(a+b+c)
#4
def media(a,b=0):
    return((a+b)/2)
#5
def calcolatore_iva(prezzo,iva=22):
    return(prezzo+((prezzo*iva)/100))

#Scheda 3
#1. Scrivi una procedura stampa_pari che prende un numero n e stampa i numeri pari da 0 a n.
#2. Trasforma stampa_pari in funzione che restituisce una lista di pari invece di stamparli.
#3. Crea una procedura disegna_rettangolo che stampa un rettangolo di asterischi (altezza, larghezza come parametri).
#4. Scrivi una funzione fattoriale che calcola e restituisce il fattoriale di n (usa ciclo).
#5. Create una procedura per stampare un menu (es. opzioni di un gioco) e una funzione per calcolare un punteggio. Integratele.

#1
def stampa_pari(n):
    for i in range(0,n+1):
        if i%2==0:
            print(i)
#2
def lista_pari(n):
    pari=[]
    for i in range(0,n+1):
        if i%2==0:
            pari.append(i)
    return(pari)
    
if __name__=="__main__":
    num=4
    quadrato(num)
    
    nome="Ksenia"
    stampa_nome(nome)
    
    risultato=somma(1,2,3)
    print(risultato)
    
    numUno=5
    numDue=7
    risultato=massimo(numUno,numDue)
    print(risultato)
    
    lung=9
    larg=3
    area(lung,larg)
    lung=6
    larg=2
    area(lung,larg)
    
    print(potenza(3))
    print(potenza(3,3))
    
    benvenuto("Ksenia")
    
    print(calcola())
    
    print(media(4))
    
    print(calcolatore_iva(100))
    
    stampa_pari(10)
    
    lista=lista_pari(10)
    print(lista)
    
    