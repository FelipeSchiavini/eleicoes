import os
from typing import Dict

from modelos import get_csvs
from modelos.LeitorCsv import LeitorCsv
from modelos.SqlInserter import SqlInserter


class DespesaCandidato:
    def __init__(self, dados: Dict[str, str]):
        self.dados = dados

    def despesa_candidato(self):
        return {
            "cpf_candidato": int(self.dados['NR_CPF_CANDIDATO']),
            "cnae_fornecedor": self.dados['DS_CNAE_FORNECEDOR'],
            "cnpj_fornecedor": self.dados['NR_CPF_CNPJ_FORNECEDOR'],
            "nm_fornecedor": self.dados['NM_FORNECEDOR'],
            "cd_origem_despesa": self.dados['CD_ORIGEM_DESPESA'],
            "origem_despesa": self.dados['DS_ORIGEM_DESPESA'],
            "valor_contratado": float(self.dados['VR_DESPESA_CONTRATADA'].replace(',', '.')),
        }

    @classmethod
    def insert_csv(cls, pasta: str):
        sql = SqlInserter()
        for linha in get_csvs(pasta):
            item = DespesaCandidato(linha)
            sql.insert(tabela="despesa_candidato", linha=item.despesa_candidato())


DespesaCandidato.insert_csv(r'C:\Users\Felipe Schiavini\Desktop\Data Analitics\Digital House\Projeto Integrador\prestacao de contas\Base de dados - TSE - Prestação de Contas - Copia')
