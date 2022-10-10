from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def __init__(self) -> None:
        self._name = "Karthick Sabari"
        super(AbstractClass, self).__init__()

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_contact_center(self):
        pass


class ConcreteClass(AbstractClass):

    def get_contact_center(self):
        return self.name


if __name__ == '__main__':
    print(AbstractClass.__abstractmethods__)
    name = ConcreteClass().get_contact_center()
    print(name)
