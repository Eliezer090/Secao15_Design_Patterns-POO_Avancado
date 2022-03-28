"""
    Adaptador para permitir que duas classes que seriam incompativeis se comunicam e trabalham junto.
    Por exemplo, já temos uma classe que move o personagem, mas por complexidades a empresa designou
        este trabalho para outra empresa que tem essas classes melhores implementadas com isso precisamos
        adaptar as classes da nova empresa para a classe que move o personagem.
"""

from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass

    @abstractmethod
    def down(self) -> None:
        pass

    @abstractmethod
    def left(self) -> None:
        pass


class Control(IControl):
    def top(self) -> None:
        print('Movendo para cima')

    def right(self) -> None:
        print('Movendo para direita')

    def down(self) -> None:
        print('Movendo para baixo')

    def left(self) -> None:
        print('Movendo para esquerda')


class NewControl:
    # Controles da nova empresa
    def move_top(self) -> None:
        print('Movendo para cima_NovaEmpresa')

    def move_right(self) -> None:
        print('Movendo para direita_NovaEmpresa')

    def move_down(self) -> None:
        print('Movendo para baixo_NovaEmpresa')

    def move_left(self) -> None:
        print('Movendo para esquerda_NovaEmpresa')


class ControlAdapter:
    """Adapter object - COMPOSIÇÃO(É melhor)"""

    def __init__(self, control: NewControl) -> None:
        self.control: NewControl = control

    def top(self) -> None:
        self.control.move_top()

    def right(self) -> None:
        self.control.move_right()

    def down(self) -> None:
        self.control.move_down()

    def left(self) -> None:
        self.control.move_left()


class ControlAdapter2(Control, NewControl):
    """Adapter class - HERANÇA"""

    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == "__main__":
    # Este seria o que a minha empresa criou
    #control = Control()
    new_control = NewControl()
    control_object = ControlAdapter(new_control)
    control_object.top()
    control_object.right()
    control_object.down()
    control_object.left()
    print('\n')
    control_class = ControlAdapter2()
    control_class.top()
    control_class.right()
    control_class.down()
    control_class.left()
