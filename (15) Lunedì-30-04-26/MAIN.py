#p
from datetime import datetime #importo datetime per gestire timestamp di avvio e fine elaborazione

#m
from Inserimento_dati import acquisisci_vendite #importo la funzione di input dal suo modulo 
from Calcoli_vendite import calcola_totale, calcola_media, giorni_sopra_media #importo le funzioni di calcolo
from Report_vendite import stampa_intestazione, stampa_totale_media, stampa_giorni_sopra, stampa_durata #importo le funzioni di stampa
from Salvataggio_vendite import salva_risultati #importo la funzione di salvataggio

def main():
    risultati = [] #uso una lista per raccogliere tutte le righe da passare al modulo di salvataggio

    ora_avvio = datetime.now() #catturo il momento esatto di avvio prima di qualsiasi operazione
    risultati.append(stampa_intestazione(ora_avvio))

    vendite = acquisisci_vendite() #delego interamente l'input e la validazione al modulo dedicato

    if not vendite: #valuto la lista come booleano perchè una lista vuota è falsa in Python
        messaggio = "Nessun dato di vendita inserito"
        print(messaggio)
        risultati.append(messaggio)
    else:
        totale = calcola_totale(vendite)
        media = calcola_media(vendite)
        risultati.extend(stampa_totale_media(totale, media)) #extend() aggiunge alla lista tutti gli elmenti restituiti dalla funzione

        giorni = giorni_sopra_media(vendite, media)
        risultati.extend(stampa_giorni_sopra(giorni))

    ora_fine = datetime.now() #calcolo la durata nel modulo report
    risultati.append(stampa_durata(ora_avvio, ora_fine))

    salva_risultati(risultati, ora_avvio) #passo le righe raccolte e l'ora d'avvio al modulo di salvataggio

if __name__ == "__main__": 
    main()
