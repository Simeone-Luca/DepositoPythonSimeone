import csv #fornisce reader e writer ottimizzati per il formato CSV
import os

class GestoreFile: #cclasse che raggruppa tutte le operazioni di I/O sui file 
    def __init__(self):
        self.percorso_file = None #memorizzo il percorso del file corrente come attributo di istanza per riutilizzarlo in scrittura
        self.tipo_file = None #memorizzo il tipo (txt o csv) per sapere quale logica di scrittura applicare

    def imposta_file(self, nome, tipo): #metodo chiamato quando si crea un file nuovo senza ancora leggerlo
        self.percorso_file = f"{nome}.{tipo}" #costruisco il percorso unendo  nome ed estensione
        self.tipo_file = tipo

    def leggi_file(self, percorso): #metodo pubblico che smista la lettura al metodo corretto in base all'estensione
        self.percorso_file = percorso
        estensione = os.path.splitext(percorso)[1].lower() #os.path.splitext() separa il nome del file dall'estensione restituendo una tupla e prendo il secondo elemento
        self.tipo_file = estensione.lstrip(".") #lstrip() rimuove il punto iniziale dall'estensione per ottenere txt o csv

        if estensione == ".txt":
            return self._leggi_txt(percorso)
        elif estensione == ".csv":
            return self._leggi_csv(percorso)
        else:
            print("[!] Formato file non supportato. Usa TXT o CSV.")
            return None

    def _leggi_txt(self, percorso): #metodo privato per leggere file TXT con struttura: nome|categoria|prezzo|quantità
        prodotti = []
        try:
            with open(percorso, "r", encoding="utf-8") as f: #with open() apre il file e lo chiude automaticamente al termine del blocco anche in caso di eccezione
                for riga in f: #itero sulle righe del file oggetto che è un iterabile per default
                    riga = riga.strip()
                    if not riga or riga.startswith("#"): #salto righe vuote e commenti per rendere il file più leggibile
                        continue
                    parti = riga.split("|") #restituisce una lista di sottostringhe
                    if len(parti) != 4: #controllo che ogni riga abbia esattamente i quattro campi attesi
                        print(f"[!] Riga ignorata (formato errato): {riga}")
                        continue
                    try:
                        prodotti.append({ #costruisco il dizionario del prodotto convertendo i tipi necessari
                            "nome": parti[0].strip(),
                            "categoria": parti[1].strip(),
                            "prezzo": float(parti[2].strip()),
                            "quantita": int(parti[3].strip())
                        })
                    except ValueError:
                        print(f"[!] Riga ignorata (valori non numerici): {riga}")
        except FileNotFoundError: #FileNotFoundError viene sollevato da open() quando il file non esiste nel percorso indicato
            print("[!] File TXT non trovato.")
            return None
        except Exception as e: #catcho eccezioni generiche per evitare crash inattesi mostrando il messaggio originale
            print(f"[X] Errore durante la lettura del file TXT: {e}")
            return None
        return prodotti

    def _leggi_csv(self, percorso): #metodo privato per leggere file CSV usando DictReader che mappa automaticamente le colonne ai nomi dell'intestazione
        prodotti = []
        try:
            with open(percorso, "r", encoding="utf-8", newline="") as f: #newline="" è necessario con il modulo csv per gestire correttamente i ritorni a capo su tutti i sistemi operativi
                reader = csv.DictReader(f) #DictReader legge ogni riga come un dizionario usando la prima riga come chiavi
                for riga in reader:
                    try:
                        prodotti.append({
                            "nome": riga["nome"].strip(),
                            "categoria": riga["categoria"].strip(),
                            "prezzo": float(riga["prezzo"].strip()),
                            "quantita": int(riga["quantita"].strip())
                        })
                    except (KeyError, ValueError) as e: #keterror si verifica se manca una colonna attesa nel CSV mentre valueerror se il valore non è convertibile
                        print(f"[!] Riga CSV ignorata: {e}")
        except FileNotFoundError:
            print("[!] File CSV non trovato.")
            return None
        except Exception as e:
            print(f"[X] Errore durante la lettura del file CSV: {e}")
            return None
        return prodotti

    def scrivi_file(self, prodotti): #metodo pubblico che sceglie il formato di scrittura in base al tipo impostato
        if self.percorso_file is None or self.tipo_file is None: #se non è stato impostato nessun file non posso procedere
            percorso = input("[!] Nessun file impostato. Inserisci percorso con estensione: ").strip()
            if not percorso:
                print("[X] Percorso non valido.")
                return
            self.percorso_file = percorso
            self.tipo_file = os.path.splitext(percorso)[1].lstrip(".")

        if self.tipo_file == "txt":
            self._scrivi_txt(prodotti)
        elif self.tipo_file == "csv":
            self._scrivi_csv(prodotti)
        else:
            print("[!] Tipo file non riconosciuto per la scrittura.")

    def _scrivi_txt(self, prodotti): #metodo privato che serializza la lista di dizionaric con formato su txt
        try:
            with open(self.percorso_file, "w", encoding="utf-8") as f: #con w sovrascrive il file se esiste già o ne crea uno nuovo
                f.write("#nome|categoria|prezzo|quantita\n") #scrivo una riga di intestazione come commento per documentare il formato
                for p in prodotti:
                    riga = f"{p['nome']}|{p['categoria']}|{p['prezzo']}|{p['quantita']}\n"
                    f.write(riga)
            print(f"[+] File salvato: {self.percorso_file}")
        except Exception as e:
            print(f"[X] Errore durante la scrittura del file TXT: {e}")

    def _scrivi_csv(self, prodotti): #metodo privato per scrivere la lista di dizionari rispettando il formato CSV standard con dw
        try:
            with open(self.percorso_file, "w", encoding="utf-8", newline="") as f:
                campi = ["nome", "categoria", "prezzo", "quantita"] #definisco l'ordine delle colonne che sarà usato sia per l'intestazione sia per le righe
                writer = csv.DictWriter(f, fieldnames=campi) #dictwriter associa ogni chiave del dizionario alla colonna corrispondente
                writer.writeheader() #writeheader() scrive la riga di intestazione usando i fieldnames definiti
                writer.writerows(prodotti) #writerows() scrive tutte le righe della lista in un unico passaggio
            print(f"[+] File salvato: {self.percorso_file}")
        except Exception as e:
            print(f"[x] Errore durante la scrittura del file CSV: {e}")
