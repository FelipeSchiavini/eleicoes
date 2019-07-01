from typing import List


class Animal:
    def __init__(self, nome: str):
        self.nome = nome
        self.posicao = 0

    def andar(self):
        self.posicao += 1
        print(self.nome, 'esta na posicao', self.posicao)


class Felino(Animal):
    def __init__(self, nome, bigodes: int):
        super().__init__(nome)
        self.roronadas = False
        self.bigodes = bigodes

    def ronronar(self):
        print('rrrrr')
        self.bigodes += 1
        self.roronadas = True


class Leao(Felino):
    def rugir(self):
        print('raaauw')
        self.ronronar()

class Cachorro(Animal):
    def latir(self):
        print(self.nome, 'au au')


class Pessoa:
    def __init__(self, animais: List[Animal]):
        self.animais = animais

    def carinho(self):
        for animal in self.animais:
            animal.andar()
            if isinstance(animal, Cachorro):
                animal.latir()


apolo = Cachorro('Apolo')
apolo.latir()
apolo.andar()
print(apolo.posicao)

felipe = Pessoa([apolo])
felipe.carinho()

daniel = Pessoa([Leao('Tablu', 3), Felino('Kuba', 4)])
daniel.carinho()
