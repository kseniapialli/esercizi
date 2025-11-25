#Ho definito una funzione def che lavora sulla lista
def sommaLista(lista):
    somma=0
    for element in lista:
        somma=somma+element
    print(somma)
    
#Scrivere una funzione che data una lista stampi a video il numero degli elementi pari
def pariLista(lista):
    contatore=0
    for element in lista:
        if element%2==0:
            contatore=contatore+1
    print(contatore)
    
#Ho definito la funzione generica lista e ho richiamato il parametro di tipo lista
lista=[1,2,3,4]
sommaLista(lista)
pariLista(lista)

lista2=[2,3,4,5]
sommaLista(lista2)

