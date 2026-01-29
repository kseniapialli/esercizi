#scrivere un programma che dati due numeri interi random in un intervallo 0,100
#ne calcoli la somma, la differenza e controlli se la differenza è minore di
#una certa soglia fissata a priori nel main

#sottoproblemi:
#1)somma di due numeri (procedura)
#2)differenza tra due numeri (funzione)
#3)verificare un numero è minore di una soglia (procedura)

import random

def somma(numeroUno,numeroDue):
    somma=numeroUno+numeroDue
    print(somma)
    
def differenza(numeroUno,numeroDue):
    differenza=numeroUno-numeroDue
    return(differenza)

def verifica(numeroUno,numeroDue):
    if numeroUno<soglia:
        

if __name__ == '__main__':
    uno=random.randint(0,100)
    due=random.randint(0,100)
    somma(uno,due)
    
    dif=differenza(uno,due)
    print(dif)