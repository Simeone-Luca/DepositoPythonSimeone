import os

CLIENTI_FILE = "clienti.txt" #costante del percorso file che uso in tutto il modulo per coerenza

def _carica_clienti() -> dict: #funzione privata che legge il file riga per riga e ricostruisce il dizionario clienti in memoria
    if not os.path.exists(CLIENTI_FILE):
        return {}
    clienti = {}
    with open(CLIENTI_FILE, "r", encoding="utf-8") as f: #apro in sola lettura per non rischiare modifiche accidentali
        for riga in f:
            riga = riga.strip()
            if not riga or riga.startswith("#"): #salto righe vuote e commenti
                continue
            parti = riga.split("|") 
            if len(parti) < 4: #verifico che la riga abbia almeno 4 campi obbligatori: chiave nome cognome password
                continue
            chiave = parti[0]
            nome = parti[1]
            cognome = parti[2]
            password = parti[3]
            acquisti = []
            if len(parti) == 5 and parti[4]: #il quinto campo esiste solo se il cliente ha almeno un acquisto
                for blocco in parti[4].split(","): #split su , separa i singoli acquisti nella lista
                    campi = blocco.split(";") #split su ; separa i tre campi di ogni acquisto: articolo quantita totale
                    if len(campi) == 3:
                        acquisti.append({
                            "articolo": campi[0],
                            "quantita": int(campi[1]), #converto in int perchè la quantità è un numero intero
                            "totale": float(campi[2]) #converto in float per rappresentare correttamente il valore monetario
                        })
            clienti[chiave] = {
                "nome": nome,
                "cognome": cognome,
                "password": password,
                "acquisti": acquisti
            }
    return clienti

def _salva_clienti(clienti: dict): #funzione privata che riscrive l'intero file con lo stato aggiornato
    with open(CLIENTI_FILE, "w", encoding="utf-8") as f: #modalità 'w' tronca e riscrive tutto per mantenere coerenza tra memoria e file
        f.write("# formato: chiave|nome|cognome|password|articolo;qty;totale,articolo;qty;totale\n\n")
        for chiave, dati in clienti.items(): #itero sulle coppie chiave-valore del dizionario con items()
            acquisti_str = ",".join( #join concatena la lista di stringhe acquisto usando ',' come separatore
                f"{a['articolo']};{a['quantita']};{a['totale']:.2f}"
                for a in dati["acquisti"] #generatore che costruisce la stringa di ogni acquisto al volo senza lista intermedia
            )
            f.write(f"{chiave}|{dati['nome']}|{dati['cognome']}|{dati['password']}|{acquisti_str}\n")

def registra_cliente(nome: str, cognome: str, password: str) -> bool:
    clienti = _carica_clienti()
    chiave = nome.lower() + "_" + cognome.lower() #costruisco la chiave univoca combinando nomee e cognome in minuscolo
    if chiave in clienti:
        return False
    clienti[chiave] = {
        "nome": nome,
        "cognome": cognome,
        "password": password,
        "acquisti": [] #lista vuota che verrà popolata ad ogni acquisto
    }
    _salva_clienti(clienti)
    return True

def login_cliente(nome: str, cognome: str, password: str) -> dict | None:#funzione di controllo per verificare i criteri
    clienti = _carica_clienti()
    chiave = nome.lower() + "_" + cognome.lower()
    if chiave in clienti and clienti[chiave]["password"] == password:
        return clienti[chiave]
    return None

def registra_acquisto(nome: str, cognome: str, articolo: str, quantita: int, totale: float):#registro gli aquisti
    clienti = _carica_clienti()
    chiave = nome.lower() + "_" + cognome.lower()
    if chiave in clienti:
        clienti[chiave]["acquisti"].append({
            "articolo": articolo,
            "quantita": quantita,
            "totale": round(totale, 2) #round limita a 2 decimali per evitare imprecisioni dei float nella scrittura
        })
        _salva_clienti(clienti)