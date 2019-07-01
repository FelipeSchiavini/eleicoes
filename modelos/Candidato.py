from typing import Dict

from modelos import get_csvs
from modelos.SqlInserter import SqlInserter


class Candidato:
    def __init__(self, dados: Dict[str, str]):
        self.dados = dados

    def candidato(self):
        return {
            "cpf_candidato": int(self.dados['NR_CPF_CANDIDATO']),
            "nm_candidato": self.dados['NM_CANDIDATO'],
            "idade_posse": int(self.dados['NR_IDADE_DATA_POSSE']),
            "sit_tot_turno": self.dados['DS_SIT_TOT_TURNO'],
            "st_reeleicao": self.dados['ST_REELEICAO'],
            "declarar_bens": self.dados['ST_DECLARAR_BENS'],
            "id_genero": int(self.dados['CD_GENERO']),
            "id_escolaridade": int(self.dados['CD_GRAU_INSTRUCAO']),
            "id_estado_civil": int(self.dados['CD_ESTADO_CIVIL']),
            "id_cor_raca": int(self.dados['CD_COR_RACA']),
            "id_uf": self.dados['SG_UF'],
            "id_uf_nascimento": self.dados['SG_UF_NASCIMENTO'],
            "id_cargo": int(self.dados['CD_CARGO']),
            "id_partido": int(self.dados['NR_PARTIDO']),
            "id_ocupacao": int(self.dados['CD_OCUPACAO']),
        }

    def cargo(self):
        return {
            "id_cargo": self.dados["CD_CARGO"],
            "cargo": self.dados["DS_CARGO"],
        }

    @classmethod
    def insert_csv(cls, pasta: str):
        sql = SqlInserter()
        for dados in get_csvs(pasta):
            candidato = Candidato(dados)
            sql.insert("candidato", candidato.candidato())
            sql.insert("cargo", candidato.cargo())


Candidato.insert_csv(r'C:\Users\Felipe Schiavini\Desktop\Data Analitics\Digital House\Projeto Integrador\consulta_cand_2018')
