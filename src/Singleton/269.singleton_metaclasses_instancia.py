from typing import List, Dict, Any


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# a metaclass faz o memso trabalho do arquivo 268.singleton_resolver_init.py


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        # este print vai ser executado toda vez que insanciar a classe
        print('Inicializando AppSettings')
        self.tema = 'O tema escuro'
        self.font = 'Arial'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)
    # Mesmo endereço de memoria!
    print(as1 is as2)
    as3 = AppSettings()
    print(as3.tema)
    print(as1 is as3)
