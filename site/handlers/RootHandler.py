import tornado.web


class RootHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")
