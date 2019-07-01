from tornado.ioloop import IOLoop

from SiteApp import SiteApp

if __name__ == "__main__":
    app = SiteApp()
    app.listen(8888)
    IOLoop.current().start()
