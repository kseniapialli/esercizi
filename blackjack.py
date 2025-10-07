"""
1)Estrarre 3 carte da un mazzo (lista)
mazzo=[1,2,3,4,5,6,7,8,9,10,J,Q,K]
2)Calcolare punteggio usando dizionario
Associa carta il suo valore
"""

import random

mazzo=["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
dizionario={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

punteggio=0

carte=random.sample(mazzo,3)

for i in range(1,3):
    punteggio=punteggio+dizionario[carte[i]]
   
    
#indice=random.randint(1,13)
#carta=mazzo[indice]

#for i in range(0,3):
#    indice=random.randint(1,13)
#    carta=mazzo[indice]
#    valore=dizionario[carta]
#    punteggio=punteggio+valore
