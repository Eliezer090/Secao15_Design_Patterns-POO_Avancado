"""
    Resolvendo o problema do Singleton com decorator.
"""


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class AppSettings:
    def __init__(self) -> None:
        # este print vai ser executado somente 1 vez.
        print('Inicializando AppSettings')
        self.tema = 'O tema escuro'
        self.font = 'Arial'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    # Mesmo endereço de memoria!
    print(as1 is as2)
