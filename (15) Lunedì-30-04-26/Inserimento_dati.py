#modulo di acquisizione e validazione dell'input dell'utente
def acquisisci_vendite(): #definisco una funzione che incapsula il ciclo di input e lo rende riutilizzabile dal main
    while True: #fin quando è True:
        input_utente = input("\n- Inserisci gli importi di vendita separati da spazi: ")
        try: #intercetto eventuali problemi per non far crashaare il programma
            vendite = [int(x) for x in input_utente.split()] #uso una lista comprehension che divide la stringa con split() e converte ogni elemento in int
            return vendite #restituisco la lista al chiamante solo se la conversione è riuscita
        except ValueError: #eccezione che quando riceve una stringa non numerica:
            print("[X] Errore: hai inserito un valore non valido. Devi usare solo numeri interi separati da spazi!\n")
