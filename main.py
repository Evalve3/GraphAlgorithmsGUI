from interfaces import MainWindow, WindowsSubject
import tkinter as tk
from CustomWindows import ChangeWindow, ShowMatrixWindow


class ChoiceWindow(MainWindow):
    @staticmethod
    def init_window(window_manager):
        ChoiceWindow.init_change_matrix_button()
        ChoiceWindow.init_show_result_button()

    @staticmethod
    def init_change_matrix_button():
        def change_matrix_click(event):
            a = ChangeWindow(ChoiceWindow.window_manager(), ChoiceWindow.window_manager().window_subject)
            a.grab_set()

        btn = tk.Button(ChoiceWindow.window_manager(),
                        text="Ввести матрицу",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", change_matrix_click)
        btn.pack()

    @staticmethod
    def init_show_result_button():
        def show_result_click(event):
            a = ShowMatrixWindow(ChoiceWindow.window_manager(), ChoiceWindow.window_manager().window_subject)
            a.grab_set()

        btn = tk.Button(ChoiceWindow.window_manager(),
                        text="Показать результат",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", show_result_click)
        btn.pack()


subject = WindowsSubject()
main_window = ChoiceWindow.create_window_manager(subject)
main_window.mainloop()
