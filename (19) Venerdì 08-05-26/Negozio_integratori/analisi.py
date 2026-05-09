def analizza_prodotti(prodotti): #ricevo la lista di dizionari dei prodotti e produco statistiche aggregate senza modificarla
    print("\n∞∞∞∞∞∞∞∞ Gestione del magazzino ∞∞∞∞∞∞∞∞")
 
    prezzi = [p["prezzo"] for p in prodotti] #estrae solo i prezzi dalla lista di dizionari in modo conciso
    quantita = [p["quantita"] for p in prodotti]
 
    print(f"> Totale prodotti: {len(prodotti)}")
    print(f"> Prezzo medio: {sum(prezzi) / len(prezzi):.2f}€")
    print(f"> Prezzo minimo: {min(prezzi):.2f}€") #min() e max() iterano sulla lista per trovare il valore massimo e minimo
    print(f"> Prezzo massimo: {max(prezzi):.2f}€")
    print(f"> Quantità totale in magazzino: {sum(quantita)}")
 
    valore_totale = 0 #accumulo il valore totale sommando manualmente ogni prodotto senza usare generator expression
    for p in prodotti:
        valore_totale += p["prezzo"] * p["quantita"]
    print(f"> Valore totale del magazzino: {valore_totale:.2f}€")
 
    categorie = {} #dizionario per contare quanti prodotti appartengono a ciascuna categoria
    for p in prodotti:
        cat = p["categoria"]
        if cat not in categorie: #se la categoria non è ancora nel dizionario la inizializzo a zero
            categorie[cat] = 0
        categorie[cat] += 1
 
    print("\n> Prodotti per categoria:")
    for cat in categorie: #itero direttamente sulle chiavi del dizionario senza usare .items()
        print(f"  {cat}: {categorie[cat]} prodotto/i") #accedo al valore tramite chiave come in un dizionario normale
 
    sotto_soglia = [p for p in prodotti if p["quantita"] < 5] #filtro con list comprehension i prodotti con scorte basse
    if sotto_soglia:
        print("\n> Prodotti con scorte basse (quantità < 5):")
        for p in sotto_soglia:
            print(f"  - {p['nome']} (quantità: {p['quantita']})")
    else:
        print("\n[X] Nessun prodotto con scorte basse!")
 
    print("∞" * 40)
