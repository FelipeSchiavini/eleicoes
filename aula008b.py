from random import choice, shuffle

def names ():
    a1 = input(' nome do aluno 1:')
    a2 = input(' nome do aluno 2:')
    a3 = input(' nome do aluno 3:')
    a4 = input(' nome do aluno 4:')
    lista = [a1, a2, a3, a4]
    print(' o Aluno predileto é',choice(lista))
    shuffle(lista)
    print (' vai se fuder ', lista)

print(__name__)

if __name__ == '__main__':
    names()
