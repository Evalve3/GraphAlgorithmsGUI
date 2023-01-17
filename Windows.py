from abc import abstractmethod
from exceptions import SingletonException
from observer import Observer, WindowsSubject
from tkinter import Toplevel, Tk, Wm


class Window(Observer, Toplevel):
    _window_subject: WindowsSubject

    def __init__(self, parent: Wm, window_subject: WindowsSubject) -> None:
        super().__init__(parent)
        self._window_subject = window_subject
        self._window_subject.register_observer(self)
        self.init_window()

    def destroy(self) -> None:
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
    def matrix(self) -> list:
        return self.__matrix

    @property
    def window_subject(self) -> WindowsSubject:
        return self._window_subject


class MainWindow:
    _window_manager: MainWindowTk = None

    @classmethod
    def create_window_manager(cls) -> TkObserver:
        if cls._window_manager is None:
            window_subject = WindowsSubject()
            cls._window_manager = MainWindowTk(window_subject)
            cls.init_window(cls._window_manager)
            return cls._window_manager
        raise SingletonException('Object already created')

    @classmethod
    def window_manager(cls) -> TkObserver:
        return cls._window_manager

    @staticmethod
    @abstractmethod
    def init_window(window_manager) -> None:
        pass

    def __init__(self) -> None:
        raise SingletonException('Only create_window_manager can create MainWindow objects')
