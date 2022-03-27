
from abc import ABC, abstractmethod


class StringReprMixing:
    def __str__(self):
        parms = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])

        return f'{self.__class__.__name__}({parms})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixing):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def set_firstname(self, firstname):
        pass

    @abstractmethod
    def set_lastname(self, lastname):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def add_phone_number(self, phone_number):
        pass

    @abstractmethod
    def add_address(self, address):
        pass

    @abstractmethod
    def build(self):
        pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def set_firstname(self, firstname):
        self._result.firstname = firstname

    def set_lastname(self, lastname):
        self._result.lastname = lastname

    def set_age(self, age):
        self._result.age = age

    def add_phone_number(self, phone_number):
        self._result.phone_numbers.append(phone_number)

    def add_address(self, address):
        self._result.addresses.append(address)

    def build(self):
        return self._result


class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.set_firstname(firstname)
        self._builder.set_lastname(lastname)
        self._builder.set_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address):
        self._builder.set_firstname(firstname)
        self._builder.set_lastname(lastname)
        self._builder.add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user = user_director.with_age('John', 'Doe', 30)
    user2 = user_director.with_address('Maria', 'miranda', 'Rua 1, 1')
    print(user)
    print(user2)