#importo le classi dei capi principali e dei componenti finitura
from Capi_principali import CapoPrincipale, Giacca, Pantalone, Gilet 
from Componenti_finitura import ComponenteFinitura, Cravatta, Papillon, Pochette 
import csv
import os

#Classe che fa da contenitore centrale del sistema. Gestisce capi e componenti con metodi polimorfici
class Sartoria:

    VENDITE_FILE = "vendite.csv"
    
    MAPPA_TIPI = {
        "giacca": Giacca, "pantalone": Pantalone, "gilet": Gilet,
        "cravatta": Cravatta, "papillon": Papillon, "pochette": Pochette
    }
    
    def __init__(self):
        self._capi = [] #lista che conterrà oggetti di tipo CapoPrincipale o sue sottoclassi
        self._componenti = [] #lista che conterrà oggetti di tipo componentefinitura o sue sottoclassi

    def aggiungi_capo(self, capo): #funzione che verifica se l'oggetto passato sia un'istanza di capoprincipale prima di aggiungerlo
        if isinstance(capo, CapoPrincipale): #con isinstance controllo se l'oggetto è un'istanza della classe o di una sua sottoclasse
            self._capi.append(capo)
        elif isinstance(capo, ComponenteFinitura):
            self._componenti.append(capo)

    def rimuovi_capo(self, capo, codice): #scorro la lista e rimuovo il capo con il codice corrispondente usando una list comprehension
        if isinstance(capo, CapoPrincipale):
            self._capi = [c for c in self._capi if c.codice != codice] #la list comprehension crea una nuova lista escludendo il capo con quel codice
            return True
        elif isinstance(capo, ComponenteFinitura):
            self._componenti = [c for c in self._componenti if c.codice != codice]
            return True
        return False
            
    def modifica_capo(self, codice, nuovo_prezzo=None): #funzione per modificare i capi in cui uso parametri opzionali con valore none per permettere alcune modifiche
        if self.cerca_capo(codice) is not None:
            capo = self.cerca_capo(codice)
            print(f"Vecchio prezzo del {self.capo.__class__.__name__} {self.codice}: €{capo.prezzo}")
            capo.prezzo = nuovo_prezzo
            print(f"Nuovo prezzo del {self.capo.__class__.__name__} {self.codice}: €{capo.prezzo}")
            return True
        return False #restituisco False se nessun capo con quel codice è stato trovato

    def cerca_capo(self, codice): #scorro la lista e restituisco il primo capo trovato con quel codice oppure diretttamente None
        prodotti = self._capi + self._componenti
        for capo in prodotti:
            if capo.codice == codice:
                return capo
        return None

    def analizza_tutti(self): #chiamo descrizione() in modo polimorfico cioè Python esegue la versione corretta in base al tipo reale dell'oggetto
        selezione = input("cosa vuoi analizzare:\n 1 per capi\n 2 per componenti: ")
        match selezione:
            case "1":   
                print("\n>>> ANALISI DI TUTTI I CAPI <<<")
                
                if not self._capi: #controllo se la lista è vuota prima di procedere
                    print("[X] Nessun capo presente")
                    return
                for capo in self._capi:
                    print(f"{capo.descrizione()} | Prezzo calcolato: €{capo.calcola_prezzo():.2f}") #il polimorfismo fa sì che descrizione() e calcola_prezzo() eseguano la versione della sottoclasse reale
                
            
            case "2":
                print("\n>>> ANALISI DI TUTTI I COMPONENTI <<<")
                if not self._componenti:
                    print("> Nessun componente presente")
                    return
                for comp in self._componenti:
                    print(f"{comp.descrizione()} | Prezzo calcolato: €{comp.calcola_prezzo():.2f}")
                

    def analizza_per_tipo(self, tipo): #uso isinstance per filtrare la lista in base al tipo di classse richiesto

        classe = self.MAPPA_TIPI.get(tipo.lower()) #get restituisce none solose la chiave non esiste
        if classe is None:
            print(f"[!] Tipo '{tipo}' non riconosciuto")
            return
        tutti = self._capi + self._componenti #unisco le due liste 
        trovati = [obj for obj in tutti if isinstance(obj, classe)] #filtro con isinstance per riconoscere anche le sottoclassi
        print(f"\n>>> Analisi per tipo: {tipo.upper()} <<<")
        if not trovati:
            print("[X] Nessun elemento trovato.")
            return
        for obj in trovati:
            print(f"{obj} | {obj.descrizione()}")

    def analizza_per_tipo_e_personalizzazione(self, tipo, valore): #combino il filtro per tipo con un confronto sul risultato di descrizione()

        classe = self.MAPPA_TIPI.get(tipo.lower())
        if classe is None:
            print(f"Tipo '{tipo}' non riconosciuto")
            return
        tutti = self._capi + self._componenti
        trovati = [obj for obj in tutti if isinstance(obj, classe) and valore.lower() in obj.descrizione().lower()] #cerco il valore nella descrizione polimorfica dell'oggetto
        print(f"\n>>> ANALISI PER TIPO '{tipo}' E PERSONALIZZAZIONE '{valore}' <<<")
        if not trovati:
            print("[X] Nessun elemento trovato")
            return
        for obj in trovati:
            print(f"{obj} | {obj.descrizione()}")

    def salva_vendita(self, capo):
        file_esiste = os.path.exists(self.VENDITE_FILE)

        with open(self.VENDITE_FILE, "a", newline="", encoding="utf-8") as f:
            fieldnames = ["codice", "tipo", "nome", "prezzo_finale"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            if not file_esiste:        # scrive l'intestazione solo al primo accesso
                writer.writeheader()

            writer.writerow({
                "codice":            capo.codice,
                "tipo":              type(capo).__name__,
                "nome":              capo.nome,
                "prezzo_finale":     f"{capo.calcola_prezzo():.2f}",
            })
       
    def vendi_capo(self, codice):
        capo = self.cerca_capo(codice)
        if capo is None:
            print(f"[X] Nessun capo trovato con codice '{codice}'")
            return False
        if capo.venduto:
            print(f"[!] Il capo '{capo.nome}' è già stato venduto")
            return False
        capo.venduto = True
        self.salva_vendita(capo)
        print(f"[✓] Vendita registrata: {capo.nome} — €{capo.calcola_prezzo():.2f}")
        return True
    
    def analizza_venduti(self):
        prodotti = self._capi + self._componenti
        tot = 0
        for p in prodotti:
            if p.venduto == True:
                print(p.descrizione())
                prezzo = p.calcola_prezzo()
                tot += prezzo
        print(f"Il ricavato dei capi venduti è €{tot}")

    def get_capi(self): #espongo la lista 
        return list(self._capi) #restituisco una copia della lista così l'originale non può essere modificata dall'esterno

    def get_componenti(self):
        return list(self._componenti)