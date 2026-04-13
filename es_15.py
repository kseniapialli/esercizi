#Analisi delle temperature settimanali.
#Una stazione meteo ha registrato le temperature (°C) di ogni ora per 7 giorni.
#Devi calcolare statistiche giornaliere e trovare la giornata più calda e fredda
#della settimana. Struttura i dati: lista di liste (7 giorni per 24 ore).

import random

def riempi_temperature(lista):
    for i in range(0,24):
        element=random.randint(-3,25)
        lista.append(element)
        
def media_giornaliera(lista):
    somma=0
    for i in range(0,len(lista)):
        somma=somma+lista[i]
    media=somma/len(lista)
    return(media)

def varianza_giornaliera(lista,media):
    somma=0
    for i in range(0,len(lista)):
        differenza=(lista[i]-media)**2
        somma=somma+differenza
    varianza=somma/len(lista)
    return(varianza)

def deviazione_standard(varianza):
    deviazione=varianza**0.5
    return(deviazione)

def moda_giornaliera(lista):
    moda=0
    for i in range(0,len(lista)):
        contatore=0
        massimo=0
        for element in lista:
            if element==lista[i]:
                contatore=contatore+1
        if contatore>massimo:
            moda=lista[i]
    return(moda)

def errore_standard(lista,deviazione):
    errore=deviazione/len(lista)**0.5
    return(errore)

def giornata_calda():
    calda=media_lunedi
    giornata="lunedi"
    if media_martedi>calda:
        calda=media_martedi
        giornata="martedi"
    if media_mercoledi>calda:
        calda=media_mercoledi
        giornata="mercoledi"
    if media_giovedi>calda:
        calda=media_giovedi
        giornata="giovedi"
    if media_venerdi>calda:
        calda=media_venerdi
        giornata="venerdi"
    if media_sabato>calda:
        calda=media_sabato
        giornata="sabato"
    if media_domenica>calda:
        calda=media_domenica
        giornata="domenica"
    return(giornata)

def giornata_fredda():
    fredda=media_lunedi
    giornata="lunedi"
    if media_martedi<fredda:
        fredda=media_martedi
        giornata="martedi"
    if media_mercoledi<fredda:
        fredda=media_mercoledi
        giornata="mercoledi"
    if media_giovedi<fredda:
        fredda=media_giovedi
        giornata="giovedi"
    if media_venerdi<fredda:
        fredda=media_venerdi
        giornata="venerdi"
    if media_sabato<fredda:
        fredda=media_sabato
        giornata="sabato"
    if media_domenica<fredda:
        fredda=media_domenica
        giornata="domenica"
    return(giornata)
 
if __name__=="__main__":
    lunedi=[]
    riempi_temperature(lunedi)
    print("lunedi"+str(lunedi))
    media=media_giornaliera(lunedi)
    print(media)
    varianza=varianza_giornaliera(lunedi,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(lunedi)
    print(moda)
    errore=errore_standard(lunedi,deviazione)
    print(errore)
    martedi=[]
    riempi_temperature(martedi)
    print("martedi"+str(martedi))
    media=media_giornaliera(martedi)
    print(media)
    varianza=varianza_giornaliera(martedi,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(martedi)
    print(moda)
    errore=errore_standard(martedi,deviazione)
    print(errore)
    mercoledi=[]
    riempi_temperature(mercoledi)
    print("mercoledi"+str(mercoledi))
    media=media_giornaliera(mercoledi)
    print(media)
    varianza=varianza_giornaliera(mercoledi,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(mercoledi)
    print(moda)
    errore=errore_standard(mercoledi,deviazione)
    print(errore)
    giovedi=[]
    riempi_temperature(giovedi)
    print("giovedi"+str(giovedi))
    media=media_giornaliera(giovedi)
    print(media)
    varianza=varianza_giornaliera(giovedi,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(giovedi)
    print(moda)
    errore=errore_standard(giovedi,deviazione)
    print(errore)
    venerdi=[]
    riempi_temperature(venerdi)
    print("venerdi"+str(venerdi))
    media=media_giornaliera(venerdi)
    print(media)
    varianza=varianza_giornaliera(venerdi,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(venerdi)
    print(moda)
    errore=errore_standard(venerdi,deviazione)
    print(errore)
    sabato=[]
    riempi_temperature(sabato)
    print("sabato"+str(sabato))
    media=media_giornaliera(sabato)
    print(media)
    varianza=varianza_giornaliera(sabato,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(sabato)
    print(moda)
    errore=errore_standard(sabato,deviazione)
    print(errore)
    domenica=[]
    riempi_temperature(domenica)
    print("domenica"+str(domenica))
    media=media_giornaliera(domenica)
    print(media)
    varianza=varianza_giornaliera(domenica,media)
    print(varianza)
    deviazione=deviazione_standard(varianza)
    print(deviazione)
    moda=moda_giornaliera(domenica)
    print(moda)
    errore=errore_standard(domenica,deviazione)
    print(errore)
    media_lunedi=media_giornaliera(lunedi)
    media_martedi=media_giornaliera(martedi)
    media_mercoledi=media_giornaliera(mercoledi)
    media_giovedi=media_giornaliera(giovedi)
    media_venerdi=media_giornaliera(venerdi)
    media_sabato=media_giornaliera(sabato)
    media_domenica=media_giornaliera(domenica)
    calda=giornata_calda()
    print(calda)
    fredda=giornata_fredda()
    print(fredda)
