#funzione che prende 3 parametri, il 3 è un parametro opzionale, ha una valore fisso
def somma(numero1,numero2,numero3=4):
    somma_r=numero1+numero2+numero3
    return somma_r

a=1
b=3
somma_2=somma(a,b)
print(somma_2)
#qui il parametro non è piu opzionale ma ha valore 10
somma_3=somma(a,b,10)
print(somma_3)