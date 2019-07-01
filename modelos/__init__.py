import os

from modelos.LeitorCsv import LeitorCsv


def get_csvs(pasta: str):
    arquivos = os.listdir(pasta)
    for arquivo in sorted(arquivos):
        print('******** Importando ', arquivo)
        if arquivo.endswith('.csv') and not arquivo.endswith("BRASIL.csv"):
            for linha in LeitorCsv(os.path.join(pasta, arquivo)).ler():
                yield linha
