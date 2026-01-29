#il sottoproblema del calcolo dell'area del rettangolo è costituito da
#due input(base e altezza) e un solo output (area)

import random

def proceduraCalcoloAreaRettangolo(base, altezza):
    area=base*altezza
    print(area)

def funzioneCalcoloAreaRettangolobase(base,altezza):
    area=base*altezza
    return(area)

if __name__ == '__main__':
     a=random.randint(1,20) #a e b vengono presi come valori
     b=random.randint(1,20)
     proceduraCalcoloAreaRettangolo(a,b) #sostituisce a e b con base e altezza
     
     area=funzioneCalcoloAreaRettangolobase(a,b) #prende il valore che rilascia e lo inserisce all'interno dell'area
     print(area) #l'area vine restituita