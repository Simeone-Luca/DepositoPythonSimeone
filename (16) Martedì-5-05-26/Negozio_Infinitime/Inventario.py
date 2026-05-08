import os 

INVENTARIO_FILE = "inventario.txt" #costante condivisa del percorso file usata in tutto il modulo

def _carica_inventario() -> dict: #funzione privata che ricostruisce il dizionario inventario leggendo il file riga per riga
    if not os.path.exists(INVENTARIO_FILE): #verifico l'esistenza prima di aprire
        return {}
    inventario = {}
    with open(INVENTARIO_FILE, "r", encoding="utf-8") as f: #apro in sola lettura per non rischiare modifiche accidentali
        for riga in f: #itero il file riga per riga 
            riga = riga.strip()
            if not riga or riga.startswith("#"): #salto le righe vuote e quelle che iniziano con "#" usate come commenti nel file
                continue
            parti = riga.split("|") #uso il carattere "|" come separatore perchè è improbabile nei nomi degli articoli
            if len(parti) == 3: #verifico che la riga abbia esattamente 3 campi prima di estrarre i valori
                nome = parti[0].strip()
                inventario[nome] = {
                    "prezzo": float(parti[1].strip()), #converto in float perch+ il file contiene testo e il prezzo richiede decimali
                    "quantita": int(parti[2].strip()) #converto in int perchè la quantità è un numero intero
                }
    return inventario

def _salva_inventario(inventario: dict): #funzione privata che sovrascrive il file con lo stato corrente dell'inventario in memoria
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f: #modalità w tronca e riscrive tutto garantendo coerenza tra memoria e file
        f.write("> Inventario di Infinitime\n") #scrivo una riga di intestazione per rendere il file leggibile
        f.write("> formato: nome|prezzo|quantita\n\n") #documento il formato nel file stesso per chiarezza
        for nome, dati in inventario.items(): #itero su coppie chiave-valore del dizionario con items()
            f.write(f"{nome}|{dati['prezzo']:.2f}|{dati['quantita']}\n") #:.2f formatta il float con sempre 2 decimali

def inizializza_inventario(): #funzione pubblica che crea il file con dati di esempio se non esiste ancora
    if not os.path.exists(INVENTARIO_FILE):
        inventario_default = { #dizionario di articoli predefiniti usato per popolare il negozio al primo avvio
            "Creatina monoidrato Creapure": {"prezzo": 34.99, "quantita": 190},
            "Proteine isolate": {"prezzo": 40.99, "quantita": 180},
            "Vitamina D3+K2": {"prezzo": 18.29, "quantita": 130},
            "Magnesio Bisglicinato": {"prezzo": 0.99, "quantita": 120},
            "Pre workout Infinity": {"prezzo": 24.49, "quantita": 130},
            "Shaker": {"prezzo": 4.99, "quantita": 500},
        }
        _salva_inventario(inventario_default) #persisto l'inventario di default sul file

def get_inventario() -> dict: #funzione pubblica che espone il contenuto corrente dell'inventario agli altri moduli
    return _carica_inventario()

def aggiungi_articolo(nome: str, prezzo: float, quantita: int) -> bool: #restituisce bool per segnalare se l'aggiunta è riuscita o se il nome era duplicato e "->" lo utilizzo per aspettarmi un valore del tipo, come bool in questo caso
    inventario = _carica_inventario()
    if nome in inventario: #blocco l'aggiunta se il nome è già presente perchè il nome è la chiave del dizionario
        return False
    inventario[nome] = {"prezzo": prezzo, "quantita": quantita}
    _salva_inventario(inventario)
    return True

def rimuovi_articolo(nome: str) -> bool: #restituisce bool per comunicare se la rimozione ha trovato l'articolo
    inventario = _carica_inventario()
    if nome not in inventario: #verifico l'esistenza prima di tentare la rimozione per evitare keyerror
        return False
    del inventario[nome] #del rimuove la chiave e il suo valore associato dal dizionario
    _salva_inventario(inventario)
    return True

def aggiorna_articolo(nome: str, nuovo_prezzo: float | None, nuova_quantita: int | None) -> bool: #accetta none per i campi che non vanno modificati
    inventario = _carica_inventario()
    if nome not in inventario:
        return False
    if nuovo_prezzo is not None: #aggiorno il campo solo se è stato fornito un valore diverso da None
        inventario[nome]["prezzo"] = nuovo_prezzo
    if nuova_quantita is not None:
        inventario[nome]["quantita"] = nuova_quantita
    _salva_inventario(inventario)
    return True

def scala_quantita(nome: str, quantita: int) -> bool: #diminuisce la quantità disponibile dopo un acquisto restituisce False se non c'è abbastanza stock
    inventario = _carica_inventario()
    if nome not in inventario:
        return False
    if inventario[nome]["quantita"] < quantita: #verifico che lo stock sia sufficiente prima di sottrarre
        return False
    inventario[nome]["quantita"] -= quantita #sottrae direttamente dal valore esistente nel dizionario
    _salva_inventario(inventario)
    return True

def stampa_inventario(): #funzione di visualizzazione che legge dal file e stampa in formato tabellare
    inventario = _carica_inventario()
    if not inventario:
        print("\n  Inventario vuoto.")
        return
    print("\n" + "="*55)
    print(f"  {'ARTICOLO':<20} {'PREZZO':>10} {'DISPONIBILE':>12}")
    print("="*55)
    for nome, dati in inventario.items(): #:<20 allinea a sinistra con larghezza 20 :>10 allinea a destra con larghezza 10
        disponibile = dati['quantita']
        stato = f"{disponibile} pz" if disponibile > 0 else "ESAURITO" #operatore ternario per mostrare lo stato in modo leggibile
        print(f"  {nome:<20} {dati['prezzo']:>9.2f}€ {stato:>12}")
    print("="*55)
