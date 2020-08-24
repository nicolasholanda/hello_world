# -*- coding: utf-8 -*-

import getpass


def hello_world():
    """
        Método responsável por exibir 'Hello World' no console.
        E exibir um bom dia com o o nome do usuário.
    """
    print(f"Hello World! Good morning, {getpass.getuser()}.")


if __name__ == "__main__":
    hello_world()
