from datetime import date

import tornado.web
from tornado import template

from models.Person import Person


class PersonHandler(tornado.web.RequestHandler):
    PEOPLE = {
        "projetos": Person("Matéria Prima", date(1989, 2, 21), "https://pypi.org/static/images/logo-large.72ad8bf1.svg"),
        "daniel": Person("Daniel", date(1986, 11, 12), "https://pypi.org/static/images/logo-large.72ad8bf1.svg"),
        "maya": Person("Maya", date(2017, 5, 26)),
        "mae": Person("Claudia", date(1962, 3, 29)),
    }

    def get(self, name: str):
        person = self.PEOPLE[name]
        loader = template.Loader("templates")
        t = loader.load("person.html")
        html = t.generate(name=person.name, days=person.days(), people=self.PEOPLE)
        self.write(html)
