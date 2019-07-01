import tornado.web

from handlers.DanielHandler import DanielHandler
from handlers.FelipeHandler import FelipeHandler
from handlers.PersonHandler import PersonHandler
from handlers.RootHandler import RootHandler


class SiteApp(tornado.web.Application):
    def __init__(self):
        super().__init__(self._routes())

    def _routes(self):
        return [
            (r"/", RootHandler),
            (r"/daniel", DanielHandler),
            (r"/felipe", FelipeHandler),
            (r"/person/(.*)", PersonHandler),
        ]
