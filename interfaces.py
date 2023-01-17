from abc import abstractmethod
from exceptions import SingletonException
from tkinter import *


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
    def input_matrix_size(self):
        return self.__input_matrix_size

    @input_matrix_size.setter
    def input_matrix_size(self, new_size: tuple):
        self.__input_matrix_size = new_size
        self.notify_observers()

    @property
    def input_matrix(self):
        return self.__input_matrix

    @input_matrix.setter
    def input_matrix(self, new_matrix: list):
        self.__input_matrix = new_matrix
        self.notify_observers()

    @property
    def result_matrix(self):
        return self.__result_matrix

    @result_matrix.setter
    def result_matrix(self, new_matrix: list):
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


class Window(Observer, Toplevel):
    _window_subject: WindowsSubject

    def __init__(self, parent, window_subject: WindowsSubject):
        super().__init__(parent)
        self._window_subject = window_subject
        self._window_subject.register_observer(self)
        self.init_window()

    def destroy(self):
        self._window_subject.remove_observer(self)
        super().destroy()
        del self

    @abstractmethod
    def init_window(self) -> None:
        pass


class TkObserver(Tk, Observer):
    _window_subject: WindowsSubject

    def __init__(self, window_subject: WindowsSubject):
        super().__init__()
        self._window_subject = window_subject
        self._window_subject.register_observer(self)

    @abstractmethod
    def update(self) -> None:
        pass


class MainWindowTk(TkObserver):
    __input_matrix: list

    def update(self) -> None:
        self.__input_matrix = self._window_subject.input_matrix

    @property
    def matrix(self):
        return self.__matrix

    @property
    def window_subject(self):
        return self._window_subject


class MainWindow:
    _window_manager: MainWindowTk = None

    @classmethod
    def create_window_manager(cls, window_subject):
        if cls._window_manager is None:
            cls._window_manager = MainWindowTk(window_subject)
            cls.init_window(cls._window_manager)
            return cls._window_manager
        raise SingletonException('Object already created')

    @classmethod
    def window_manager(cls):
        return cls._window_manager

    @staticmethod
    @abstractmethod
    def init_window(window_manager):
        pass

    def __init__(self):
        raise SingletonException('Only window manager can create MainWindow objects')
