#scrivere un programma che dati due punti in un piano cartesiano
#scriva l'equazione della retta associata e mandi in output
#il messaggio con la positività o negatività del coefficiente angolare.

#sottoproblemi
#1)m=y2-y1/x2-x1 (funzione) [parametri: 4 (xUno,xDue,yUno,yDue)]
#2)y-y0=m(x-x0) (procedura) [parametri: 3 (m,xDue,yDue)]

import random

def calcolo_m(xUno,xDue,yUno,yDue): #funzione perchè rilascia un valore all'esterno, quando finisce la funzione i valori sono 0
    m=(yDue-yUno)/(xDue-xUno)
    return(m)

def equazione(m,x,y):
    eq="y-"+str(y)+"="+str(m)+"(x-"+str(x)+")" #concatenazione di stringhe, variazione tra stringhe fisse e variabili, uso la variabile stringa per la parte variabile
    print(eq)

def controllo_m(m):
    if m>0:
        print("m ha segno positivo")
    elif m==0: #= è assegnazione e == è un ugualianza
        print("m è nullo")
    else:
        print("m ha segno negativo")

#incremento, l'unico parametro che cambia è la lista, i valori che passo dal main non cambiano 
def incremento_uno(a):
    a=a+1
    print(a)
    
def incremento_uno_stable(a): #se sovrascrivo il valore nel main cambia
    a=a+1
    return(a)

if __name__=="__main__": #le variabili del main sono xUno,xDue,yUno,yDue,m
    xUno=random.randint(-20,20)
    xDue=random.randint(-20,20)
    yUno=random.randint(-20,20)
    yDue=random.randint(-20,20)
    
    coefficente_angolare=calcolo_m(xUno,xDue,yUno,yDue) #variabile a sinitra perchè è una funzione
    print(coefficente_angolare)
    equazione(coefficente_angolare,xDue,yDue) #sono definiti all'interno del main
    controllo_m(coefficente_angolare)
    
    incremento_uno(xUno) #i numeri non cambiano perchè passano come valore
    xUno=incremento_uno_stable(xUno) #sovrascrivo il valore cioè lo riassegno un'altra volta