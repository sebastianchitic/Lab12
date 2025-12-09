from dataclasses import dataclass

from database.DB_connect import DBConnect

from model.Rifugio import Rifugio
from model.Connessione import Connessione


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    @staticmethod
    def readRifugio():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM rifugio"
        cursor.execute(query)
        for row in cursor:
            rifugio = Rifugio(
                id = row["id"],
                nome = row["nome"],
                localita = row["localita"],
                altitudine = row["altitudine"],
                capienza = row["capienza"],
                aperto = row["aperto"]
            )
            result.append(rifugio)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def readConnessione(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM connessione WHERE ANNO <= %s"
        cursor.execute(query, (year,))
        for row in cursor:
            connessioni = Connessione(
                id = row["id"],
                id_rifugio1 = row["id_rifugio1"],
                id_rifugio2 = row["id_rifugio2"],
                distanza = row["distanza"],
                difficolta = row["difficolta"],
                durata = row["durata"],
                anno = row["anno"]
            )
            result.append(connessioni)

        cursor.close()
        conn.close()
        return result


