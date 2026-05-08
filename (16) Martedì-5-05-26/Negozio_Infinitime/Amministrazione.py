#volevo importare json per leggere i dati strutturati del file clienti nel report vendite ma mi ero perso
import os #importo os per verificare l'esistenza dei file prima della lettura

ADMIN_FILE = "amministrazione.txt" #costante del file dove registro le transazioni per il report
CLIENTI_FILE = "clienti.txt" #importo il percorso del file clienti per generare il report vendite da esso

ADMIN_CREDENZIALI = { #dizionario con le credenziali degli amminnistratori preinserite nel sistema
    "luca.simeone": {"nome": "Luca", "cognome": "Simeone", "password": "maledettoaudio123"},
    "mirko.campari": {"nome": "Mirko", "cognome": "Campari", "password": "commentatutto999"},
}

def login_admin(username: str, password: str) -> dict | None: #confronto con le credenziali senza toccare alcun file
    if username in ADMIN_CREDENZIALI and ADMIN_CREDENZIALI[username]["password"] == password:
        return ADMIN_CREDENZIALI[username]
    return None

def registra_transazione(cliente_nome: str, cliente_cognome: str, articolo: str, quantita: int, totale: float): #scrive ogni vendita come riga di testo nel file amministrazione
    with open(ADMIN_FILE, "a", encoding="utf-8") as f: #la modalità 'a' aggiunge in fondo senza cancellare le righe precedenti
        f.write(f"{cliente_nome}|{cliente_cognome}|{articolo}|{quantita}|{totale:.2f}\n") #formato pipe separato facile facile da rileggere con split

def mostra_report_vendite(): #legge il file amministrazione riga per riga e genera il report delle vendite
    print("\n" + "="*60)
    print("[!] Rreport delle VENDITE - da: amministrazione.txt")
    print("="*60)
    if not os.path.exists(ADMIN_FILE):
        print("[X] Nessuna vendita registrata.")
        print("="*60)
        return
    totale_negozio = 0.0 #accumula il guadagno totale incrementato ad ogni riga letta
    trovato = False #flag di debug per sapere se esiste almeno una riga valida nel file
    with open(ADMIN_FILE, "r", encoding="utf-8") as f: #apro in sola lettura per non modificare il file sorgente
        for riga in f: #itero riga per riga sfruttando il fatto che i file sono iterabili in severus python 
            riga = riga.strip()
            if not riga: #salto le righe vuote che potrebbero esistere nel file
                continue
            parti = riga.split("|") #split divide la stringa usando | come separatore e restituisce una lista di stringhe
            if len(parti) != 5: #debug in cui verifico che la riga abbia esattamente 5 campi prima di estrarre i valori
                continue
            nome, cognome, articolo, quantita, totale_str = parti #unpacking assegna ciascun elemento della lista a una variabile separata
            totale_riga = float(totale_str) #converto la stringa del totale in float per la somma e la formattazione
            print(f"  {nome} {cognome:<15} | {articolo:<15} x{quantita:<4} | {totale_riga:.2f}€")
            totale_negozio += totale_riga
            trovato = True
    if not trovato:
        print("[!] Nessuna vendita registrata al momento")
    print("-"*60)
    print(f"[*] Guadagno totale di Infinitime: {totale_negozio:.2f}€")
    print("="*60)

def mostra_guadagno_totale(): #calcola il guadagno sommando solo la colonna totale del file senza costruire strutture dati complesse
    if not os.path.exists(ADMIN_FILE):
        print("\n  Guadagno totale: 0.00€ (nessun dato)")
        return
    totale = 0.0
    with open(ADMIN_FILE, "r", encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            parti = riga.split("|")
            if len(parti) == 5: #leggo solo le righe ben formate per evitare errori di conversione
                totale += float(parti[4]) #parti[4] è sempre il totale perchè il formato è fisso e posizionale
    print(f"\n[*] Guadagno totale di Infinitime: {totale:.2f}€")

def mostra_stato_inventario_da_file(): #delega la stampa al modulo inventario che è l'unico responsabile del suo file
    from Inventario import stampa_inventario #importo localmente per evitare dipendenza circolare a livello di modulo
    stampa_inventario()