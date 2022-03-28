
"""
    Proxy tem varias funções virtual, proteção, inteligente e sao aplicadas em diversos contextos.
    O exemplo abaixo implementa um proxy virtual e inteligente, onde o objeto real é criado apenas quando necessário
        e quando atender os requisitos que o virtual estabeleceu, então toda a regra de negócio inicial
        pode estar no virtual, e uma vez chamado ele fica em cache as informações nao sendo necessário
        chamar cada vez.
"""

from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    """Subject Interface"""
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        pass


class RealUser():
    """Real Subject"""

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # Simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # Simulando requisição
        return [{'street': 'Rua 1', 'number': '1'}, {'street': 'Rua 2', 'number': '2'}]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # Simulando requisição
        return {'cpf': '111.111.111-11', 'rg': '555555555555', 'firstname': self.firstname, 'lastname': self.lastname}


class UserProxy(IUser):
    """Proxy Subject"""

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname
        # Esses objtos nao existem ainda neste ponto do código
        self._real_user: RealUser
        self._cache_addresses: List[Dict]
        self._cache_all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cache_addresses'):
            self._cache_addresses = self._real_user.get_addresses()
        return self._cache_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        if not hasattr(self, '_cache_all_user_data'):
            self._cache_all_user_data = self._real_user.get_all_user_data()
        return self._cache_all_user_data


if __name__ == "__main__":
    user = UserProxy('Eliezer', 'Santos')
    print(user.firstname)
    print(user.lastname)
    # Vai demorar 6 segundos para carregar os dados do usuario pela primeira vez
    print(user.get_all_user_data())
    print(user.get_addresses())

    print('Cached Data:')
    # Agora vai estar em cache e vai ser insta
    for i in range(3):
        print(user.get_all_user_data())
        print(user.get_addresses())
