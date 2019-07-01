from datetime import date


class Person:
    def __init__(self, name: str, birthday: date, image: str = None):
        self.name = name
        self.birthday = birthday
        self.image = image

    def greeting(self) -> str:
        return "Olá {} ({} dias de vida)".format(self.name, self.days())

    def days(self) -> int:
        age = date.today() - self.birthday
        return age.days
