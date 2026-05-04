#modulo per la formattazione e la stampa dei risultati
def stampa_intestazione(ora_avvio): #ricevo l'oggetto datetime e lo formato con strftime() che converte la data secondo la maschera specificata
    riga = f"\n|||||||||| Programma di report delle vendite di Infinitime - {ora_avvio.strftime('%d/%m/%Y %H:%M:%S')} ||||||||||"
    print(riga)
    return riga

def stampa_totale_media(totale, media): #restituisco una lista di righe così il chiamante può raccoglierle senza logica di stampa duplicata
    r1 = f"- Totale vendite: {totale}"
    r2 = f"- Media vendite: {media:.2f}" #uso :.2f nel formato f-string per arrotondare la media a 2 cifre decimali
    print(r1)
    print(r2)
    return [r1, r2]

def stampa_giorni_sopra(giorni_sopra): #ricevo la lista di tuple (giorno, valore) già filtrata dal modulo calcoli
    righe = []
    if giorni_sopra: #valuto la lista come booleano: una lista vuota è falsa in Python
        header = "\n[+] Giorni con vendite sopra la media:"
        print(header)
        righe.append(header)
        for giorno, valore in giorni_sopra: #decompongo ogni tupla direttamente nel ciclo for senza accesso per indice
            riga = f"  - Giorno {giorno}: {valore}"
            print(riga)
            righe.append(riga)
    else:
        riga = "- Nessun giorno ha vendite sopra la media"
        print(riga)
        righe.append(riga)
    return righe

def stampa_durata(ora_avvio, ora_fine): #sottraggo due oggetti datetime ottenendo un timedelta e chiamo total_seconds() per avere i secondi come float
    durata = (ora_fine - ora_avvio).total_seconds()
    riga = f"\n[!] Elaborazione completata in {durata:.3f} secondi"
    print(riga)
    return riga
