from csv import DictReader
from csv import excel
from typing import Iterable, Dict


class LeitorCsv:
    """
    Classe responsável por ler um aquivo em CSV e converter para um dicionário.
    """
    class DialetoCsv(excel):
        delimiter = ';'

    def __init__(self, arquivo):
        """
        :param arquivo: O nome do arquivo, incluindo pasta.
        """
        self.arquivo = arquivo

    def ler(self) -> Iterable[Dict[str, str]]:
        """
        Le o arquivo em CSV, retornando
        :return: Objetos do tipo self.classe.
        """
        with open(self.arquivo) as f:
            for linha in DictReader(f, dialect=self.DialetoCsv):
                yield linha
