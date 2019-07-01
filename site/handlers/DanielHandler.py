from datetime import date

import tornado.web
from tornado import template

from models.Person import Person


class DanielHandler(tornado.web.RequestHandler):
    def get(self):
        person = Person("Daniel", date(1986, 11, 12))

        loader = template.Loader("templates")
        t = loader.load("person.html")
        html = t.generate(name=person.name, days=person.days())
        self.write(html)
