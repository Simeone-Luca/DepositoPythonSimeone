from Componenti_finitura import Cravatta, Papillon, Pochette
from Capi_principali import Giacca, Pantalone, Gilet
from Sartoria import *
import random


def crea_capo(sartoria):
    scelta = input("Che capo vuoi creare?\n 1 per Capo Principale\n 2 per Componente finitura: ")
    match scelta:
        case "1":
            selezione = input("Che capo vuoi creare?\n 1 per Giacca\n 2 per Pantalone\n 3 per Gilet: ")
            codice = input("Inserisci il codice: ")
            nome = input("Inserisci nome: ")
            tessuto = input("Inserisci il tessuto: ")
            colore = input("Inserisci il colore: ")
            taglia = input("Inserisci taglia: (S, M, L, XL)")
            prezzo = float(input("Inserisci il prezzo: "))
            match selezione:
                case "1":
                    numero_bottoni= int(input("Inserisci il numero di bottoni: "))
                    capo = Giacca(codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni)
                case "2":
                    tipo_taglio = input("Seleziona il tipo del taglio (slim, regular, wide): ")
                    capo = Pantalone(codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio)
                case "3":
                    rever_presente = bool(input("Il rever è presente ? (True / False): "))
                    capo = Gilet(codice, nome, tessuto, colore, taglia, prezzo, rever_presente)
                case _:
                    print("Scelta non valida")
            sartoria.aggiungi_capo(capo)
            print(f"Capo {capo.codice} aggiunto con successo")
        case "2":
            selezione = input("Che componente di finitura vuoi creare?\n 1 per Cravatta\n 2 per Papillon\n 3 per Pochette: ")
            codice = input("Inserisci il codice: ")
            nome = input("Inserisci nome: ")
            materiale = input("Inserisci il tessuto: ")
            colore = input("Inserisci il colore: ")
            prezzo = float(input("Inserisci il prezzo: "))
            match selezione:
                case "1":
                    larghezza = input("Seleziona la larghezza della cravatta: ")
                    componente = Cravatta(codice, nome, materiale, colore, prezzo, larghezza)
                case "2":
                    tipo_chiusura = input("Selezione il tipo di chiusura del papillon [elastico, regolabile, fissa]: ")
                    componente = Papillon(codice, nome, materiale, codice, prezzo, tipo_chiusura)
                case "3":
                    piega_decorativa = input("Seleziona la piega decorativa della pochette [piatta, a punta, a ventaglio]: ")
                    componente = Pochette(codice, nome, materiale, colore, prezzo, piega_decorativa)
                case _:
                    print("Scelta non valida")
            sartoria.aggiungi_capo(componente)
            print(f"Capo {capo.codice} aggiunto con successo")
        

def modifica_capo(sartoria, codice):
    capo = sartoria.cerca_capo(codice)
    if capo is None:
        print("Prodotto non trovato")
    nuovo_prezzo = float(input(f"Seleziona il nuovo prezzo per il capo: {capo.__class__.__name__} {capo.codice}: "))
    sartoria.modifica_capo(capo, nuovo_prezzo)
    print(f"Capo {codice} modificato con successo")
    
    
def elimina_capo(sartoria, codice):
    capo = sartoria.cerca_capo(codice)
    if capo is None:
        print("Capo non trovato")
    sartoria.rimuovi_capo(capo, codice)
    print(f"Capo {codice} eliminato con successo")
    
def vendi_capo(sartoria, codice):
    capo = sartoria.cerca_capo(codice)
    if capo is None:
        print("Capo non trovato")
    sartoria.vendi_capo(codice)
    
def analisi(sartoria):
    print("Seleziona il tipo di analisi:")
    selezione = input("1 per analisi tipo\n2 per analisi tipo e personalizzazione \n3 per analisi prodotti venduti: ")
    match selezione:
        case "1":
            tipo = input("Scegli il tipo per cui effettuqre l'analisi: ")
            sartoria.analizza_per_tipo(tipo)
        case "2":
            tipo = input("Scegli il tipo per cui effettuare l'analisi: ")
            valore = input("Scegli il valore su cui filtrare l'analisi: ")
            sartoria.analisi_per_tipo_e_personalizzazione(tipo, valore)
        case "3":
            sartoria.analizza_venduti()
        case _:
            print("Scelta non valida")

def genera_dati(sartoria): #genero dati casuali realistici per simulare un magazzino già popolato
    nome = ["Roma", "Napoli", "Milano", "Padova", "Bologna", "Treviso"]
    tessuti = ["lana", "cotone", "seta", "cashmere", "lino"] #liste di valori possibili da cui prendo a caso con random.choice
    colori = ["nero", "blu navy", "grigio antracite", "bordeaux", "beige"]
    tagli = ["classico", "slim", "sartoriale", "regular"]
    materiali = ["seta", "cotone", "microfibra", "poliestere"]
    pieghe = ["a punta", "piatta", "a ventaglio"]
    taglia = ["S", "M", "L", "XL"]
    tipo_chiusura = ["elastico", "regolabile", "fissa"]

    for i in range(1, 6): #genero 5 giacche con dati casuali
        sartoria.aggiungi_capo(Giacca(
            codice=f"G{i:03d}", #f-string con formato :03d che produce un numero con zeri iniziali per es G001(roba visiva)
            nome=f"Giacca modello {random.choice(nome)}",
            tessuto=random.choice(tessuti), #random.choice sceglie un elemento a caso dalla lista
            colore=random.choice(colori),
            taglia=random.choice(taglia),
            prezzo=round(random.uniform(150, 500), 2), #random.uniform genera un float casuale nell'intervallo dato
            numero_bottoni=random.randint(1, 3) #random.randint genera un intero casuale inclusi gli estremi
        ))

    for i in range(1, 6): #genero 5 pantaloni con dati casuali
        sartoria.aggiungi_capo(Pantalone(
            codice=f"P{i:03d}",
            nome=f"Pantalone modello {random.choice(nome)}",
            tessuto=random.choice(tessuti),
            colore=random.choice(colori),
            taglia=random.choice(taglia),
            prezzo=round(random.uniform(80, 300), 2),
            tipo_taglio=random.choice(tagli)
        ))

    for i in range(1, 4): #genero 3 gilet con dati casuali
        sartoria.aggiungi_capo(Gilet(
            codice=f"V{i:03d}",
            nome=f"Gilet modello {random.choice(nome)}",
            tessuto=random.choice(tessuti),
            colore=random.choice(colori),
            taglia=random.choice(taglia),
            prezzo=round(random.uniform(60, 200), 2),
            rever_presente=random.choice([True, False]) #random.choice funziona anche su liste di booleani
        ))

    for i in range(1, 4): #genero 3 cravatte con dati casuali
        sartoria.aggiungi_capo(Cravatta(
            codice=f"CR{i:03d}",
            nome=f"Cravatta modello {random.choice(nome)}",
            materiale=random.choice(materiali),
            colore=random.choice(colori),
            prezzo=round(random.uniform(20, 100), 2),
            larghezza=random.randint(6, 9)
        ))

    for i in range(1, 3): #genero 2 papillon con dati casuali
        sartoria.aggiungi_capo(Papillon(
            codice=f"PA{i:03d}",
            nome=f"Papillon modello {random.choice(nome)}",
            materiale=random.choice(materiali),
            colore=random.choice(colori),
            prezzo=round(random.uniform(15, 60), 2),
            tipo_chiusura=random.choice(tipo_chiusura)
        ))

    for i in range(1, 3): #genero 2 pochette con dati casuali
        sartoria.aggiungi_capo(Pochette(
            codice=f"PO{i:03d}",
            nome=f"Pochette modello {random.choice(nome)}",
            materiale=random.choice(materiali),
            colore=random.choice(colori),
            prezzo=round(random.uniform(10, 50), 2),
            piega_decorativa=random.choice(pieghe)
        ))

    print("Dati generati con successo!")
    
sartoria = Sartoria()  
genera_dati(sartoria)

def main():
    print("-"*40)
    print("BENVENUTO NEL GESTIONALE DELLA SARTORIA")
    print("-"*40)
    
    while True:
        azione = input("Seleziona l'azione da svolgere:\n 1 per creare un capo\n 2 per modificare il prezzo di un capo\n 3 per eliminare un capo \n 4 per vendere un capo\n 5 per analisi \n X per uscire: ")
        match azione:
            case "1":
                crea_capo(sartoria)
                
            case "2":
                codice = input("Seleziona il codice del capo da modificare: ")                
                modifica_capo(sartoria, codice)
                
            case "3":
                codice = input("Seleziona il codice del capo da eliminare: ")  
                elimina_capo(sartoria, codice)
                
            case "4":
                codice = input("Seleziona il codice del capo da vendere: ") 
                vendi_capo(sartoria, codice)
                
            case "5":
                analisi(sartoria)
                
            case "X":
                print("Chiusura gestionale")
                break
            
            case _:
                print("Scelta non valida")
                
            


if __name__ == "__main__":
    main()

            
            


                           
                                                   
