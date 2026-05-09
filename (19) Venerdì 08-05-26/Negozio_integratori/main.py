import os
from gestore_file import GestoreFile
from analisi import analizza_prodotti


#SCELTE DEL MENU'
def mostra_menu():
    print("\n" + "╔" + "∞"*40 + "╗")
    print("║  BENVENUTO NEL MAGAZZINO DI INFINITIME ║")
    print("╚" + "∞"*40 + "╝")
    print("\n∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞ MENU' ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞")
    print("1. Carica file esistente (TXT o CSV)")
    print("2. Crea nuovo file")
    print("3. Visualizza prodotti caricati")
    print("4. Aggiungi prodotto")
    print("5. Modifica prodotto")
    print("6. Elimina prodotto")
    print("7. Analizza dati")
    print("8. Salva file")
    print("0. Esci")
    print("∞"*40)



#MAINagioia
def main():
    gestore = GestoreFile() #istanzio la classe che gestisce la lettura e scrittura dei file
    prodotti = [] #inizializzo la lista che conterrà i dizionari dei prodotti caricati o creati
    
    #MENU'
    while True:
        mostra_menu()
        scelta = input("> Scegli un'opzione: ").strip() #strip() rimuove spazi e newline ai bordi della stringa

        match scelta: #Carica file esistente di tipo txt o csv
            
            case "1":
                percorso = input("> Inserisci il percorso del file (TXT o CSV): ").strip()
                if not os.path.exists(percorso): #os.path.exists() controlla se il percorso punta a un file o cartella reale nel filesystem
                    print("[X] File non trovato.")
                else:
                    prodotti = gestore.leggi_file(percorso) #carico i prodotti leggendo il file tramite il metodo gestore
                    if prodotti is not None:
                        print(f"[+] Caricati {len(prodotti)} prodotti.")

            case "2": #Crea un nuovo file
                nome = input("> Nome del nuovo file (senza estensione): ").strip()
                tipo = input("> Tipo di file (txt/csv): ").strip().lower()
                if tipo not in ("txt", "csv"): #verifico che il tipo scelto sia tra quelli supportati
                    print("[X] Tipo non supportato. Usa 'txt' o 'csv'.")
                else:
                    prodotti = [] #il nuovo file parte con lista vuota modificabile
                    gestore.imposta_file(nome, tipo)
                    print(f"> Il nuovo file '{nome}.{tipo}' pronto. Puoi aggiungere prodotti.")

            case "3": #Visualizza prodotti caricati
                if not prodotti: #controllo se la lista è vuota prima di tentare di stamparla
                    print("[X] Nessun prodotto caricato!")
                else:
                    print("\n>>>>>>>> PRODOTTI <<<<<<<<")
                    for i, p in enumerate(prodotti): #enumerate() restituisce coppie (indice, elemento) utili per mostrare la posizione
                        print(f"[{i}] Nome: {p['nome']} | Categoria: {p['categoria']} | Prezzo: {p['prezzo']}€ | Quantità: {p['quantita']}")

            case "4": #Aggiungi prodotto
                nome = input("> Nome prodotto: ").strip()
                categoria = input("> Categoria: ").strip()
                try:
                    prezzo = float(input("> Prezzo: ").strip()) 
                    quantita = int(input("> Quantità: ").strip()) 
                except ValueError: #quando è numerico:
                    print("[X] Prezzo o quantità non validi!")
                    continue
                prodotti.append({"nome": nome, "categoria": categoria, "prezzo": prezzo, "quantita": quantita}) #aggiunge il dizionario del nuovo prodotto in fondo alla lista
                print("[+] Prodotto aggiunto correttamente")

            case "5": #Modifica prodotto
                if not prodotti:
                    print("[X] Nessun prodotto da modificare")
                else:
                    try:
                        indice = int(input("> Indice del prodotto da modificare: "))
                        if indice < 0 or indice >= len(prodotti): #verifico che l'indice sia dentro i limiti della lista
                            print("[X] Indice non valido!")
                            continue
                        p = prodotti[indice] #accedo al dizionario del prodotto tramite indice per modificarlo direttamente
                        print(f"> Modifica prodotto: {p}")
                        nuovo_nome = input(f"[+] Nuovo nome [{p['nome']}]: ").strip()
                        nuova_cat = input(f"[+] Nuova categoria [{p['categoria']}]: ").strip()
                        nuovo_prezzo = input(f"[+] Nuovo prezzo [{p['prezzo']}]: ").strip()
                        nuova_qty = input(f"[+] Nuova quantità [{p['quantita']}]: ").strip()
                        if nuovo_nome: #se l'utente ha inserito un valore aggiorno il campo altrimenti lo lascio invariato
                            p['nome'] = nuovo_nome
                        if nuova_cat:
                            p['categoria'] = nuova_cat
                        if nuovo_prezzo:
                            p['prezzo'] = float(nuovo_prezzo)
                        if nuova_qty:
                            p['quantita'] = int(nuova_qty)
                        print("Prodotto modificato.")
                    except ValueError:
                        print("Valore non valido.")

            case "6": #Elimina prodotto
                if not prodotti:
                    print("[X] Nessun prodotto da eliminare!")
                else:
                    try:
                        indice = int(input("> Indice del prodotto da eliminare: "))
                        if indice < 0 or indice >= len(prodotti):
                            print("[X] Indice non valido!")
                            continue
                        rimosso = prodotti.pop(indice) #rimuove e restituisce l'elemento alla posizione specificata modificando la lista originale
                        print(f"[!] Prodotto '{rimosso['nome']}' eliminato correttamente")
                    except ValueError:
                        print("[X] Indice non valido!")

            case "7": #Analizza dati
                if not prodotti:
                    print("[X] Nessun dato da analizzare!")
                else:
                    analizza_prodotti(prodotti) #delego l'analisi al modulo passando la lista dei prodotti

            case "8": #salva i file
                if not prodotti:
                    print("Nessun prodotto da salvare.")
                else:
                    gestore.scrivi_file(prodotti)

            case "0":#via di fuga
                print("Addios!")
                break #uscita
            
            case _:
                print("[X] Opzione non valida!")

if __name__ == "__main__": 
    main()
