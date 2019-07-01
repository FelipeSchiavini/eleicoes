import os
from typing import Dict

from modelos import get_csvs
from modelos.LeitorCsv import LeitorCsv
from modelos.SqlInserter import SqlInserter


class Votacao:
    def __init__(self, dados: Dict[str, str]):
        self.dados = dados

    def votacao(self):
        return {
            "NR_CANDIDATO": int(self.dados['NR_CANDIDATO']),
            "TP_ABRANGENCIA": self.dados['TP_ABRANGENCIA'],
            "NM_CANDIDATO": self.dados['NM_CANDIDATO'],
            "DS_SIT_TOT_TURNO": self.dados['DS_SIT_TOT_TURNO'],
            "QT_VOTOS": self.dados['QT_VOTOS_NOMINAIS'],
        }

    @classmethod
    def insert_csv(cls, pasta: str):
        sql = SqlInserter()
        for linha in get_csvs(pasta):
            item = Votacao(linha)
            sql.insert(tabela="votacao", linha=item.votacao())


Votacao.insert_csv(r'C:\Users\Felipe Schiavini\Desktop\votosp\Nova pasta')
