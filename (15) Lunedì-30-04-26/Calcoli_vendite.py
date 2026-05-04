#modulo dela logica di calcolo sui dati di vendita
def calcola_totale(vendite): #ricevo la lista e delego a sum() l'iterazione e la somma degli elementi
    return sum(vendite)

def calcola_media(vendite): #divido il totale per il numero di elementi ottenuto con len()
    return calcola_totale(vendite) / len(vendite)

def giorni_sopra_media(vendite, media): #enumerate() mi fornisce indice e valore insieme e filtro solo i valori superiori alla media
    return [(i + 1, v) for i, v in enumerate(vendite) if v > media] #aggiungo 1 all indice perché i giorni partono da 1 non da 0
