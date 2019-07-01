from tornado.web import RequestHandler


class ProjetoHandler(RequestHandler):
    def get(self, projeto_id: str):


