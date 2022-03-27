
"""
    Singleton- Uma vez insanciado a classe ela deve sempre retornar o mesmo conteudo.
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # problemas ocorem se tem init se nao tiver init nao ocorre
    def __init__(self) -> None:
        # este print vai ser executado toda vez que insanciar a classe.
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
