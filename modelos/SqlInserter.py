from typing import Dict
from mysql.connector import connect, MySQLConnection, IntegrityError
from mysql.connector.cursor import MySQLCursorPrepared


class SqlInserter:
    """
    Classe responsável por inserir dicionários no MySQL.
    """
    def __init__(self):
        self.db: MySQLConnection = connect(
            host="localhost",
            user="root",
            passwd="",
            database="projeto_integrador",
        )
        self.db.autocommit = True

        # variáveis que guardam quantas linhas foram adicionadas por tabela e quantas foram ignoradas
        self.counts: Dict[str, int] = {}
        self.ignoradas: Dict[str, int] = {}

    def insert(self, tabela: str, linha: Dict[str, any]) -> None:
        """
        Adiciona um dicionário no MySQL.
        :param tabela: O nome da tabela.
        :param linha: A linha que será adicionada.
        """
        colunas = list(linha)
        interrogacoes = ', '.join(['%s'] * len(colunas))
        query = "Insert Into {} ({}) " \
                "Values ({})".format(tabela, ', '.join(colunas), interrogacoes)
        parametros = [linha[coluna] for coluna in colunas]
        try:
            cursor: MySQLCursorPrepared = self.db.cursor(prepared=True)
            cursor.execute(query, parametros)
            cursor.close()
            mensagem = 'Adicionado'
            count = self.counts.get(tabela, 0) + 1
            self.counts[tabela] = count
        except IntegrityError as err:
            mensagem = str(err)
            count = self.ignoradas.get(tabela, 0) + 1
            self.ignoradas[tabela] = count

        if not count % 1000:
            print(mensagem, tabela, self.counts[tabela])
