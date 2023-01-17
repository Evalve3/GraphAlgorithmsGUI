from abc import abstractmethod


class Observer:
    @abstractmethod
    def update(self) -> None:
        pass


class Subject:
    @abstractmethod
    def register_observer(self, o: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, o: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WindowsSubject(Subject):
    __observers: list
    __input_matrix: list = []
    __result_matrix: list = []
    __input_matrix_size: tuple = [0, 0]

    @property
    def input_matrix_size(self) -> tuple:
        return self.__input_matrix_size

    @input_matrix_size.setter
    def input_matrix_size(self, new_size: tuple) -> None:
        self.__input_matrix_size = new_size
        self.notify_observers()

    @property
    def input_matrix(self) -> list:
        return self.__input_matrix

    @input_matrix.setter
    def input_matrix(self, new_matrix: list) -> None:
        self.__input_matrix = new_matrix
        self.notify_observers()

    @property
    def result_matrix(self) -> list:
        return self.__result_matrix

    @result_matrix.setter
    def result_matrix(self, new_matrix: list) -> None:
        self.__result_matrix = new_matrix
        self.notify_observers()

    def __init__(self):
        self.__observers = list()

    def register_observer(self, o: Observer) -> None:
        self.__observers.append(o)

    def remove_observer(self, o: Observer) -> None:
        self.__observers.remove(o)

    def notify_observers(self) -> None:
        for observer in self.__observers:
            observer.update()
