#Scheda A
numeri=[3,7,2,9,4]

numeri[1]=10
numeri.append(15)

print(numeri[0])
print(numeri[3])
print(len(numeri))
print(numeri)

#Scheda B
colori=["rosso","blu","verde","giallo","viola","arancione"]

primi=colori[0:3]
ultimi=colori[3:]

print(primi)
print(ultimi)
print(colori[1:5:2])
print(colori[-1])
print(colori[2:5:2])

#Scheda C
for i in range(6):
    print(i)
    
for i in range(3,7):
    print(i)
    
for i in range(0,11,2):
    print(i)
    
#Scheda D
voti=[6,7,4,8,5]

for i in range(len(voti)):
    voti[i]=voti[i]+1
    
    print(voti)
    
for i in range(len(voti)):
    voti[i]=voti[i]-1
    
    print(voti)
    
#Scheda E
numeri=[12,5,8,19,3,14]
somma=0

for i in range(len(numeri)):
    somma=somma+numeri[i]

print("La somma è:", somma)

somma=0

for element in numeri:
    somma=somma+element

print("La somma è:", somma)

#Scheda F
for i in range(2,15,3):
    if i%2==0:
        print(i, "è pari")
    else:
        print(i, "è dispari")
        
for i in range(2,15,3):
    if i%2==1:
        print(i, "è dispari")
        
for i in range(1,11,3):
    if i%2==0:
        print(i, "è pari")
    else:
        print(i, "è dispari")