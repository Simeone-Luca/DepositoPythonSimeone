from abc import ABC, abstractmethod

class CapoPrincipale(ABC):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo):
        self._codice = codice
        self._nome = nome
        self._tessuto = tessuto
        self._colore = colore
        self._taglia = taglia
        self._prezzo = prezzo
        self._venduto = False

    @abstractmethod
    def descrizione(self):
        pass


    @abstractmethod
    def calcola_prezzo(self):
        pass
    
    def vendi(self):

        if not self.venduto:
            self.venduto = True
            print(f"{self.__class__.__name} {self.codice} venduto con successo")
            return True

        else:
            print(f"{self.nome} è già stato venduto") 
            return False
        
    @property
    def codice(self):
        return self._codice

    @codice.setter
    def codice(self, nuovo_codice):
        self._codice = nuovo_codice

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    @property
    def tessuto(self):
        return self._tessuto

    @tessuto.setter
    def tessuto(self, nuovo_tessuto):
        self._tessuto = nuovo_tessuto

    @property
    def colore(self):
        return self._colore

    @colore.setter
    def colore(self, nuovo_colore):
        self._colore = nuovo_colore

    @property
    def taglia(self):
        return self._taglia

    @taglia.setter
    def taglia(self, nuova_taglia):
        if nuova_taglia in ["S", "M", "L", "XL"]:
            self._taglia = nuova_taglia
            
    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, nuovo_prezzo):

        if nuovo_prezzo > 0:
            self._prezzo = nuovo_prezzo

    @property
    def venduto(self):
        return self._venduto

    @venduto.setter
    def venduto(self, nuovo_valore):
        if isinstance(nuovo_valore, bool):
            self._venduto = nuovo_valore

    def __str__(self):
        return f"{self.codice}, {self.nome}, {self.tessuto}, {self.taglia}, {self.colore}, {self.prezzo}€ "


class Giacca(CapoPrincipale):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, numero_bottoni):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.__numero_bottoni = numero_bottoni

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, tessuto: {self.tessuto}, colore: {self.colore}, prezzo: {self.calcola_prezzo()}, numero bottoni: {self.numero_bottoni}"
    
    def calcola_prezzo(self):
        return self.prezzo + (self.numero_bottoni * 10)
    
    @property
    def numero_bottoni(self):
        return self.__numero_bottoni

    @numero_bottoni.setter
    def numero_bottoni(self, nuovo_numero_bottoni):
        if nuovo_numero_bottoni >= 0:
            self.__numero_bottoni = nuovo_numero_bottoni
        else:
            print("Il numero di bottoni deve essere maggiore o uguale a 0")


class Pantalone(CapoPrincipale):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, tipo_taglio):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.__tipo_taglio = tipo_taglio

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, tessuto: {self.tessuto}, colore: {self.colore}, prezzo: {self.calcola_prezzo()}, tipo taglio: {self.tipo_taglio}"

    def calcola_prezzo(self):
        if self.tipo_taglio.lower() == "slim":
            return self.prezzo * 1.1
        elif self.tipo_taglia.lower() == "regular":
            return self.prezzo * 1.2
        elif self.tipo_taglio.lower() == "wide":
            return self.prezzo * 1.4
        return self.prezzo
    
    @property
    def tipo_taglio(self):
        return self.__tipo_taglio

    @tipo_taglio.setter
    def tipo_taglio(self, nuovo_tipo_taglio):
        self.__tipo_taglio = nuovo_tipo_taglio


class Gilet(CapoPrincipale):

    def __init__(self, codice, nome, tessuto, colore, taglia, prezzo, rever_presente: bool):
        super().__init__(codice, nome, tessuto, colore, taglia, prezzo)
        self.rever_presente = rever_presente

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, tessuto: {self.tessuto}, colore: {self.colore}, prezzo: {self.calcola_prezzo()}, rever presente: {self.rever_presente}"

    def calcola_prezzo(self):
        if self.rever_presente:
            return self.prezzo + 25
        return self.prezzo

    @property
    def rever_presente(self):
        return self.__rever_presente

    @rever_presente.setter
    def rever_presente(self, nuovo_rever_presente):

        if isinstance(nuovo_rever_presente, bool):
            self.__rever_presente = nuovo_rever_presente

        else:
            print("Il valore deve essere True o False")

