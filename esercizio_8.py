#dati quattro numeri generati random creare una tupla che contengta il maggiore dei primi due e il minore dei secondi due

#sottoproblemi:
#trovare il maggiore di due numeri
#trovare il minore di due numeri

def maggiore(numero1,numero2):
    if numero1>numero2:
        print(numero1)
    else:
        print(numero2)
        
def minore(numero3,numero4):
    if numero3<numero4:
        print(numero3)
    else:
        print(numero4)
        
uno=input("inserire il primo numero")
uno=int(uno)
due=input("inserire il secondo numero")
due=int(due)
tre=input("inserire il terzo numero")
tre=int(tre)
quattro=input("inserire il terzo numero")
quattro=int(quattro)

risultato=maggiore(uno,due)
risultato2=minore(tre,quattro)
        
    