import networkx as nx
from database.dao import DAO
from model.Connessione import Connessione


class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self.G = nx.Graph()
        self.nodes = None
        self.edges = None

    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        self.G.clear()

        rifugi = DAO.readRifugio()
        connessioni = DAO.readConnessione(year)

        self.id_map = {}
        for r in rifugi:
            self.id_map[r.id] = r

        for c in connessioni:
            if c.id_rifugio1 in self.id_map and c.id_rifugio2 in self.id_map:
                n1 = self.id_map[c.id_rifugio1]
                n2 = self.id_map[c.id_rifugio2]
                self.G.add_edge(n1, n2, weight = Connessione.peso)


    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        all_weights = list(nx.get_edge_attributes(self.G, 'weight').values())

        return min(all_weights), max(all_weights)



    def count_edges_by_threshold(self, soglia):
        """
        Conta il numero di archi con peso < soglia e > soglia
        :param soglia: soglia da considerare nel conteggio degli archi
        :return minori: archi con peso < soglia
        :return maggiori: archi con peso > soglia
        """
        self.massimi = 0
        self.minimi = 0

        for g in self.G.edges():
            if soglia < self.G.nodes[g]['weight']:
                self.massimi += 1
            if soglia > self.G.nodes[g]['weight']:
                self.minimi += 1
        return self.massimi, self.minimi

    """Implementare la parte di ricerca del cammino minimo"""
    # TODO
