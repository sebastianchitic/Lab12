from dataclasses import dataclass

@dataclass
class Connessione:
    id : int
    id_rifugio1 : int
    id_rifugio2 : int
    distanza : int
    difficolta : str
    durata : int
    anno : int

    def __init__(self, id, distanza, difficolta, anno, id_rifugio1, id_rifugio2, durata):
        self.id = id
        self.distanza = distanza
        self.difficolta = difficolta
        self.anno = anno
        self.id_rifugio1 = id_rifugio1
        self.id_rifugio2 = id_rifugio2
        self.durata = durata


    @property
    def fattore_difficolta(self):
        mappa = {
            'Bassa': 1.0,
            'Media': 1.5,
            'Alta': 2.5
        }
        return mappa.get(self.difficolta, 1)

    @property
    def peso(self):
        return self.distanza * self.fattore_difficolta

    def __str__(self):
        return f"{self.id} {self.id_rifugio1} {self.id_rifugio2}"

    def __hash__(self):
        return hash(self.id)
