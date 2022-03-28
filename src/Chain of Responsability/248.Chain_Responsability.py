"""
    Delegação de responsabilidades, um exemplo seria de atendimento ao cliente:
    Cliente:
        Cliente chama o suporte, pedindo para fazer X ação:
        Suporte:
            Posso fazer:
                Atende o problema do cliente e pede se precisa de algo mais:
                    Precisa?
                        Sim:
                            Caso for algo que o suporte pode fazer faz, senao delega para outra area que volta para o ponto da linha 6
                        Nao:
                            Finaliza e retorna para o cliente.
            Nao posso fazer:
                Nao pode fazer mas sabe quem pode, delega para outra area, volta para o ponto da linha 6

Resumindo o exemplo acima, é posso fazer? Sim - atende, Não - Delega para quem pode ou sabe.

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from ast import Str
from cgitb import handler


def HandlerABC(letter: str) -> str:
    letters = ["A", "B", "C"]
    if letter in letters:
        return 'HandlerABC consegiu tratar o valor: ' + letter
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ["D", "E", "F"]
    if letter in letters:
        return 'handler_DEF consegiu tratar o valor: ' + letter
    return handler_unolved(letter)


def handler_unolved(letter: str) -> str:
    return 'handler_unolved não sei tratar o valor: ' + letter


if __name__ == "__main__":
    print(HandlerABC("A"))
    print(HandlerABC("B"))
    print(HandlerABC("C"))
    print(HandlerABC("D"))
    print(HandlerABC("J"))
