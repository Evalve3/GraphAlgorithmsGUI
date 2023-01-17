import tkinter as tk
import requests
from tkinter import simpledialog as sd, Tk, messagebox
from Windows import Window, MainWindow


class InputMatrixSizeWindow(Window):

    def update(self) -> None:
        pass

    def init_window(self) -> None:
        ans = sd.askinteger('Введите размер', 'Введите размер')
        self._window_subject.input_matrix_size = (ans, ans)


class InputMatrixWindow(Window):
    text_var: list

    def init_window(self) -> None:
        a = InputMatrixSizeWindow(self, self._window_subject)
        a.grab_set()
        self.title("Ввод матрицы")
        self.geometry("650x500+120+120")
        self.configure(bg='bisque2')
        self.resizable(False, False)
        self.init_input_label()
        self.init_save_button()

    def init_input_label(self) -> None:
        self.text_var = []
        entries = []

        tk.Label(self, text="Ввод матрицы :", font=('arial', 10, 'bold'),
                 bg="bisque2").place(x=20, y=20)

        x2 = 0
        y2 = 0
        rows, cols = self._window_subject.input_matrix_size
        for i in range(rows):
            self.text_var.append([])
            entries.append([])
            for j in range(cols):
                self.text_var[i].append(tk.StringVar())
                entries[i].append(tk.Entry(self, textvariable=self.text_var[i][j], width=3))
                entries[i][j].place(x=60 + x2, y=50 + y2)
                x2 += 30
            y2 += 30
            x2 = 0

    def init_save_button(self) -> None:
        button = tk.Button(self, text="Сохранить", bg='bisque3', width=15, command=self.update_matrix)
        button.pack(side='bottom')

    def update_matrix(self) -> None:
        matrix = []
        rows, cols = self._window_subject.input_matrix_size
        for row in range(rows):
            matrix.append([])
            for col in range(cols):
                matrix[row].append(self.text_var[row][col].get())
        matrix = [list(map(lambda x: int(x), row)) for row in matrix]
        self._window_subject.input_matrix = matrix
        self._window_subject.result_matrix = matrix

    def update(self) -> None:
        pass


class ResultMatrixWindow(Window):
    result_matrix: list

    def init_window(self) -> None:
        self.result_matrix = self._window_subject.result_matrix
        self.title("Релузьтат")
        self.geometry("650x500+120+120")
        self.configure(bg='bisque2')
        self.resizable(False, False)
        self.init_result_label()

    def init_result_label(self) -> None:
        for i in range(len(self.result_matrix)):
            for j in range(len(self.result_matrix[0])):
                self.e = tk.Entry(self, width=3)
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, self.result_matrix[i][j])

    def update(self) -> None:
        pass


class AlgorithmsWindow(Window):
    input_matrix: list

    def init_window(self) -> None:
        self.input_matrix = self._window_subject.input_matrix
        self.title("Выберите алгоритм к графу")
        self.geometry("650x500+120+120")
        self.configure(bg='bisque2')
        self.init_heights_button()

    def init_heights_button(self) -> None:
        def heights_click(event):
            api_res = requests.get("http://127.0.0.1:5000//algorithms/heights",
                                   json={"matrix": self.input_matrix}).json()
            if 'error' in api_res:
                messagebox.showerror("Ошибка", api_res['error'])
                return
            self._window_subject.result_matrix = api_res['matrix']

        btn = tk.Button(self,
                        text="Посчиать высоты",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", heights_click)
        btn.pack()

    def update(self) -> None:
        pass


class ChoiceWindow(MainWindow):
    @staticmethod
    def init_window(window_manager: Tk) -> None:
        ChoiceWindow.init_change_matrix_button()
        ChoiceWindow.init_show_result_button()
        ChoiceWindow.init_algorithm_button()

    @staticmethod
    def init_algorithm_button() -> None:
        def button_click(event):
            a = AlgorithmsWindow(ChoiceWindow.window_manager(), ChoiceWindow.window_manager().window_subject)
            a.grab_set()

        btn = tk.Button(ChoiceWindow.window_manager(),
                        text="Алгоритмы",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", button_click)
        btn.pack()

    @staticmethod
    def init_change_matrix_button() -> None:
        def change_matrix_click(event):
            a = InputMatrixWindow(ChoiceWindow.window_manager(), ChoiceWindow.window_manager().window_subject)
            a.grab_set()

        btn = tk.Button(ChoiceWindow.window_manager(),
                        text="Ввести матрицу",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", change_matrix_click)
        btn.pack()

    @staticmethod
    def init_show_result_button() -> None:
        def show_result_click(event):
            a = ResultMatrixWindow(ChoiceWindow.window_manager(), ChoiceWindow.window_manager().window_subject)
            a.grab_set()

        btn = tk.Button(ChoiceWindow.window_manager(),
                        text="Показать результат",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", show_result_click)
        btn.pack()
