#Ho definito una funzione def che lavora sulla lista
def sommaLista(lista):
#La variabile somma si dice scope ed esiste solo all'interno della funzione 
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
    
#Scrivere una procedura che data una lista e un numero chiamato alfa stampi a video il numero degli elementi della lista
#più grandi di alfa
def contaMaggioreAlfa(lista,alfa):
    contatore=0
    alfa=2
    for element in lista:
        if element>alfa:
            contatore=contatore+1
    print(contatore)
    
#Ho definito la funzione generica lista e ho richiamato il parametro di tipo lista
lista=[1,2,3,4]
sommaLista(lista)
pariLista(lista)
contaMaggioreAlfa(lista,2)

lista2=[2,3,4,5]
sommaLista(lista2)


    




