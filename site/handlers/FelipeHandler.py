from datetime import date

import tornado.web
from tornado import template

from models.Person import Person


class FelipeHandler(tornado.web.RequestHandler):
    def get(self):
        person = Person("Fe", date(1989, 2, 21))

        loader = template.Loader("templates")
        t = loader.load("person.html")
        html = t.generate(name=person.name, days=person.days())
        self.write(html)
