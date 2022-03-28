
from collections.abc import Iterator, Iterable
from typing import Any, List


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self.collection = collection
        self.index = 0

    def __next__(self):
        if self.index < len(self.collection):
            item = self.collection[self.index]
            self.index += 1
            return item
        raise StopIteration

    def __iter__(self):
        return self


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self.collection = collection
        self.index = len(self.collection) - 1

    def __next__(self):
        if self.index >= 0:
            item = self.collection[self.index]
            self.index -= 1
            return item
        raise StopIteration

    def __iter__(self):
        return self


class MyList(Iterable):
    def __init__(self):
        self._items: List[Any] = []
        self._my_iterator: Iterator = MyIterator(self._items)

    def add(self, item: Any) -> None:
        self._items.append(item)

    def __iter__(self) -> Iterator:
        print('Chamou o __iter__')
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        print('Chamou o reverse_iterator')
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == "__main__":
    mylist = MyList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    print('Roubei um valor da lista: ', next(mylist.__iter__()))
    for item in mylist:
        print(item)
    print(mylist)

    for item in mylist.reverse_iterator():
        print(item)
