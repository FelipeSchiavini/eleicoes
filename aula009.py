from random import choice
from aula008b import names


def choose_name(name1: str, name2: str) -> str:
    Chooses a random name from the ones given.
    :param name1: The first name.
    :param name2: The second name.
    :return: One of the given names.    """

    """
    return choice([name1, name2])


def request_name(name_index: int) -> str:
    """
    Asks the user to type a string with the given title.
    :param name_index: The title of the string.
    :return: The string given by the user.
    """
    message = 'Digite o nome {}: '.format(name_index)
    return input(message)


def main() -> None:
    name1 = request_name(1)
    name2 = request_name(2)
    chosen_name = choose_name(name1, name2)
    print("The chosen name is", chosen_name)

    names()


print(__name__)
if __name__ == '__main__':
    main()
