from abc import ABC, abstractmethod

class ComponenteFinitura(ABC):
    
    def __init__(self, codice, nome, materiale, colore, prezzo):
        self._codice = codice
        self._nome = nome
        self._materiale = materiale
        self._colore = colore
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
            print(f"{self.__class__.__name} {self.codice} è già stato venduto")
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
    def materiale(self):
        return self._materiale
    
    @materiale.setter
    def materiale(self, nuovo_materiale):
        self._materiale = nuovo_materiale
    
    @property
    def colore(self):
        return self._colore
    
    @colore.setter
    def colore(self, nuovo_colore):
        self._colore = nuovo_colore        
    
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
    def venduto(self, valore):
        if isinstance(valore, bool):
            self._venduto = valore
    
    def __str__(self):
        return f"{self.codice}, {self.nome}, {self.materiale}, {self.colore}, {self.prezzo}€"
    
class Cravatta(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, larghezza):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.__larghezza = larghezza

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.calcola_prezzo()}, larghezza: {self.larghezza}"
    
    def calcola_prezzo(self):
        return self.prezzo + (2 * self.larghezza)
    
    @property
    def larghezza(self):
        return self.__larghezza
    
    @larghezza.setter
    def larghezza(self, nuova_larghezza):
        if nuova_larghezza > 0:
            self.__larghezza = nuova_larghezza
    
class Papillon(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, tipo_chiusura):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.__tipo_chiusura = tipo_chiusura

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.calcola_prezzo()}, tipo chiusura: {self.tipo_chiusura}"
    
    def calcola_prezzo(self):
        if self.tipo_chiusura == "elastico":
            return self.prezzo * 1.1
        elif self.tipo_chiusura == "regolabile":
            return self._prezzo + 1.3
        elif self.tipo_chiusura == "fissa":
            return self._prezzo * 1.4
        else:
            return self.prezzo
    
    @property
    def tipo_chiusura(self):
        return self.__tipo_chiusura
    
    @tipo_chiusura.setter
    def tipo_chiusura(self, nuovo_tipo_chiusura: str):
        self.__tipo_chiusura = nuovo_tipo_chiusura
        
    
class Pochette(ComponenteFinitura):

    def __init__(self, codice, nome, materiale, colore, prezzo, piega_decorativa):
        super().__init__(codice, nome, materiale, colore, prezzo)
        self.__piega_decorativa = piega_decorativa

    def descrizione(self):
        return f"{self.__class__.__name__}, codice:{self.codice}, nome: {self.nome}, materiale: {self.materiale}, colore: {self.colore}, prezzo: {self.calcola_prezzo()}, piega decorativa: {self.piega_decorativa}"
    
    def calcola_prezzo(self):
        if self.peiga_decorativa  == "piatta":
            return self.prezzo * 1.1
        elif self.peiga_decorativa  == "a punta":
            return self._prezzo + 1.3
        elif self.peiga_decorativa  == "a ventaglio":
            return self._prezzo * 1.4
        else:
            return self.prezzo
        
    @property
    def piega_decorativa(self):
        return self.__piega_decorativa
    
    @piega_decorativa.setter
    def piega_decorativa(self, nuova_piega_decorativa: str):
        self.__piega_decorativa = nuova_piega_decorativa    