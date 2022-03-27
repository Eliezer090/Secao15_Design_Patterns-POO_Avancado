"""
    Processador de pagamento de compra mas sem usar IF e de uma maneira mais legivel e facil manutanção.
    Order:
        Payment Pending:
            Inicia como pendente.
            Pode chamar Sucessful, Failed ou continuar pendente.
        Payment Successful:            
            Se for apovado chama ele mesmo.
            Se for pendente, chama o pending
            Se rejeitou chama o reject        
        Payment Failed:
            Failed só pode chamar ele mesmo
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """Context"""

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)
        print("\n")

    def pending(self) -> None:
        print("Tentando executar pending()")
        self.state.pending()
        print("Estado atual:", self.state)
        print("\n")

    def approve(self) -> None:
        print("Tentando executar approve()")
        self.state.aprove()
        print("Estado atual:", self.state)
        print("\n")

    def reject(self) -> None:
        print("Tentando executar reject()")
        self.state.reject()
        print("Estado atual:", self.state)
        print("\n")


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def aprove(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):

    def pending(self) -> None:
        print("Pagamento já pendente nao posso fazer nada")

    def aprove(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("Pagamento aprovado")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")


class PaymentApproved(OrderState):

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("Pagamento pendente")

    def aprove(self) -> None:
        print("Pagamento já aprovado, não posso fazer nada")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")


class PaymentRejected(OrderState):

    def pending(self) -> None:
        print("Pagamento já recusado, não vou mover para pendente")

    def aprove(self) -> None:
        print("Pagamento já recusado, não vou recusar novamente.")

    def reject(self) -> None:
        print("Pagamento já recusado, não vou recusar novamente.")


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
    order.pending()
