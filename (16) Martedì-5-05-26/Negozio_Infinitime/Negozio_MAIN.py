#Importo le funzioni specifiche
from Clienti import registra_cliente, login_cliente, registra_acquisto 
from Inventario import inizializza_inventario, get_inventario, aggiungi_articolo, rimuovi_articolo, aggiorna_articolo, scala_quantita, stampa_inventario
from Amministrazione import login_admin, registra_transazione, mostra_report_vendite, mostra_guadagno_totale, mostra_stato_inventario_da_file



#MENU' DISPONIBILITA' ARTICOLI
def menu_acquisto(cliente: dict): #funzione che gestisce il flusso di acquisto interattivo per il cliente loggato
    inventario = get_inventario() #carico l'inventario fresco fresco dal file ad ogni avvio del menù per avere dati aggiornati
    articoli = list(inventario.keys()) #converto le chiavi in lista per poterle indicizzare con i numeri del menù
    if not articoli:
        print("\n[X] Nessun articolo disponibile.")
        return
    print("\n∞∞∞∞∞ ARTICOLI DISPONIBILI ∞∞∞∞∞")
    for i, nome in enumerate(articoli, 1): #enumerate con start=1 genera coppie "indice, valore" partendo da 1
        dati = inventario[nome]
        if dati["quantita"] > 0:
            print(f"[>]  {i}. {nome:<20} {dati['prezzo']:.2f}€  (disp: {dati['quantita']})")
        else:
            print(f"[X]  {i}. {nome:<20} ESAURITO! ")

    try:
        scelta = int(input("\nNumero articolo (0 per annullare): ").strip()) 
    except ValueError:
        print("[X] Input non valido")
        return
    
    if scelta == 0:
        return
    if scelta < 1 or scelta > len(articoli): #verifico che l'indice sia dentro i limiti della lista
        print("[X] Scelta fuori lista")
        return

    nome_articolo = articoli[scelta - 1] #sottraggo 1 perchè il menu parte da 1
    dati_art = inventario[nome_articolo]
    if dati_art["quantita"] == 0:
        print("[X] Articolo esaurito!")
        return

    try:
        quantita = int(input(f"[Z] Quantità di '{nome_articolo}' (max {dati_art['quantita']}): ").strip())
    except ValueError:
        print("[X] Quantità non valida")
        return
    if quantita <= 0 or quantita > dati_art["quantita"]: #valido il range in un'unica condizione
        print("[X] Quantità non disponibile")
        return

    totale = round(dati_art["prezzo"] * quantita, 2) #round per evitare imprecisioni dei floating point nella moltiplicazione
    print(f"\n  Riepilogo: {nome_articolo} x{quantita} = {totale:.2f}€")
    conferma = input("Confermi l'acquisto? (s/n): ").strip().lower() #lower() normalizza l'input per accettare sia s che S

    if conferma == "s":
        if scala_quantita(nome_articolo, quantita): #scala_quantita aggiorna il file inventario e restituisce True se riuscito
            registra_acquisto(cliente["nome"], cliente["cognome"], nome_articolo, quantita, totale) #aggiorno il file clienti con l'acquisto
            registra_transazione(cliente["nome"], cliente["cognome"], nome_articolo, quantita, totale) #loggo la transazione nel file admin
            print(f"[>] Acquisto completato! Totale: {totale:.2f}€")
        else:
            print("[X] Errore: stock non sufficiente")
    else:
        print("[!] Acquisto annullato")



#MENU' CLIENTE
def menu_cliente(cliente: dict): #menù principale della sesssione cliente
    nome_display = f"{cliente['nome']} {cliente['cognome']}"
    print(f"\n  Benvenuto/a {nome_display}!")
    while True:
        print(f"\n∞∞∞∞∞ MENU CLIENTE [{nome_display}] ∞∞∞∞∞")
        print("1. Visualizza inventario")
        print("2. Acquista un articolo")
        print("0. Logout")
        scelta = input("\nScelta: ").strip()
        match scelta:
            case "1":
                stampa_inventario()
            case "2":
                menu_acquisto(cliente)
            case "0":
                print(f"\n[>] Arrivederci {nome_display}!")
                break
            case _:
                print("[X] Opzione non valida.")



#MENU' INVENTARIO
def menu_gestione_inventario(): #sottomenu dedicato alle operazioni sull'inventario accessibile solo agli admin
    while True:
        print("\n∞∞∞∞∞ GESTIONE INVENTARIO ∞∞∞∞∞")
        print("1. Aggiungi articolo")
        print("2. Rimuovi articolo")
        print("3. Aggiorna prezzo")
        print("4. Aggiorna quantita'")
        print("5. Visualizza inventario")
        print("0. Torna indietro")
        scelta = input("\nScelta: ").strip()
        match scelta:
            case "1":
                nome = input("Nome articolo: ").strip()
                try:
                    prezzo = float(input("Prezzo: ").strip().replace(",", ".")) #replace permette di inserire la virgola decimale all'italiana
                    quantita = int(input("Quantità: ").strip())
                except ValueError:
                    print("[X] Valore non valido")
                    continue #continue salta il resto del ciclo e torna all'inizo del while senza eseguire altro codice
                if aggiungi_articolo(nome, prezzo, quantita):
                    print(f"[+] Articolo '{nome}' aggiunto")
                else:
                    print(f"[!] Articolo '{nome}' già esistente")
            case "2":
                nome = input("[>] Nome articolo da rimuovere: ").strip()
                if rimuovi_articolo(nome):
                    print(f"[>] Articolo '{nome}' rimosso")
                else:
                    print(f"[!] Articolo '{nome}' non trovato")
            case "3":
                nome = input("Nome articolo: ").strip()
                try:
                    nuovo_prezzo = float(input("Nuovo prezzo: ").strip().replace(",", "."))
                except ValueError:
                    print("[!] Valore non valido")
                    continue
                if aggiorna_articolo(nome, nuovo_prezzo, None): #passo None per la quantità perchè voglio modificare solo il prezzo
                    print("[!] Prezzo aggiornato")
                else:
                    print(f"[!] Articolo '{nome}' non trovato")
            case "4":
                nome = input("Nome articolo: ").strip()
                try:
                    nuova_qty = int(input("Nuova quantità: ").strip())
                except ValueError:
                    print("[!] Valore non valido")
                    continue
                if aggiorna_articolo(nome, None, nuova_qty): #passo None per il prezzzo perchè voglio modificare solo la quantità
                    print("[!] Quantità aggiornata")
                else:
                    print(f"[!] Articolo '{nome}' non trovato")
            case "5":
                stampa_inventario()
            case "0":
                break
            case _:
                print("[X] Opzione non valida")
                
                
                
#MENU' ADMIN
def menu_admin(admin: dict): 
    nome_display = f"{admin['nome']} {admin['cognome']}"
    print(f"\n[!] Benvenuto admin {nome_display}!")
    while True:
        print(f"\n∞∞∞∞∞ MENU ADMIN [{nome_display}] ∞∞∞∞∞")
        print("1. Visualizza inventario corrente")
        print("2. Gestisci inventario")
        print("3. Report vendite")
        print("4. Guadagno totale")
        print("0. Logout")
        scelta = input("\nScelta: ").strip()
        match scelta:
            case "1":
                mostra_stato_inventario_da_file()
            case "2":
                menu_gestione_inventario()
            case "3":
                mostra_report_vendite()
            case "4":
                mostra_guadagno_totale()
            case "0":
                print(f"\n  Logout admin {nome_display}.")
                break
            case _:
                print("  Opzione non valida.")



#MENU' AREA E LOGIN CLIENTI
def menu_accesso_cliente(): #funzione che gestisce il sottomenù di registrazione e login per i clienti
    while True:
        print("\n∞∞∞∞ AREA CLIENTI ∞∞∞∞∞")
        print("1. Registrati")
        print("2. Login")
        print("0. Torna al menu principale")
        scelta = input("\nScelta: ").strip()
        match scelta:
            case "1":
                print("\n∞∞∞∞∞ REGISTRAZIONE ∞∞∞∞∞")
                nome = input("Nome: ").strip()
                cognome = input("Cognome: ").strip()
                password = input("Password: ").strip()
                if not nome or not cognome or not password: #valido che tutti i campi siano stati compilati
                    print("[!] Tutti i campi sono obbligatori.")
                    continue
                if registra_cliente(nome, cognome, password):
                    print(f"[!] Cliente '{nome} {cognome}' registrato. Ora puoi fare il login.")
                else:
                    print("[!] Cliente già registrato con questo nome e cognome.")
            case "2":
                print("\n∞∞∞∞∞ LOGIN CLIENTE ∞∞∞∞∞")
                nome = input("Nome: ").strip()
                cognome = input("Cognome: ").strip()
                password = input("Password: ").strip()
                cliente = login_cliente(nome, cognome, password) #login_cliente restituisce il dizionario cliente o None
                if cliente:
                    menu_cliente(cliente) #avvio la sessione passando il dizionario dell'utente autenticato
                else:
                    print("[X] Credenziali errate.")
            case "0":
                break
            case _:
                print("[X] Opzione non valida.")



#MENU' LOGIN ADMIN
def menu_accesso_admin(): #funzione separata per il login admin più semplice perchè non ha registrazione
    print("\n∞∞∞∞∞ LOGIN AMMINISTRATORE ∞∞∞∞∞")
    print("[!] (L'username deve avere il seguente formato: nome.cognome)")
    print("[>] Admin disponibili: luca.simeone | mirko.campari")
    username = input("Username: ").strip().lower() #lower() normalizza l'username perchè le chiavi del dizionario sono in minuscolo
    password = input("Password: ").strip()
    admin = login_admin(username, password) #login_admin confroonta con le credenziali nel modulo amministrazione
    if admin:
        menu_admin(admin)
    else:
        print("[X] Credenziali admin errate.")



#MAINagioia
def main(): #funzione principale che avvia il sistema e gestisce il loop del menu iniziale
    inizializza_inventario() #garantisco che il file inventario esiista con dati di default al primo avvio
    print("\n" + "╔" + "∞"*40 + "╗")
    print("║  BENVENUTO NEL NEGOZIO DI INFINITIME   ║")
    print("╚" + "∞"*40 + "╝")

    while True:
        print("\n∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞")
        print("║     MENU PRINCIPALE    ║")
        print("∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞\n")
        print("1. Area clienti (login/registrazione)")
        print("2. Area amministrazione")
        print("0. Esci")
        scelta = input("\n> Scelta: ").strip()
        match scelta:
            case "1":
                menu_accesso_cliente()
            case "2":
                menu_accesso_admin()
            case "0":
                print("\nA presto!")
                break
            case _:
                print("[X] Opzione non valida.")

if __name__ == "__main__":
    main()
