from interfaces import Window
import tkinter as tk
import requests
from tkinter import simpledialog as sd


class InputMatrixSeizeWindow(Window):

    def update(self) -> None:
        pass

    def init_window(self) -> None:
        ans = sd.askinteger('Введите размер', 'Введите размер')
        self._window_subject.input_matrix_size = (ans, ans)


class InputMatrixWindow(Window):

    def init_window(self):
        # Что-то взятое с интеренто, но работающее. Мб поменяю потом
        c = InputMatrixSeizeWindow(self, self._window_subject)
        c.grab_set()
        self.title("Ввод матрицы")
        self.geometry("650x500+120+120")
        self.configure(bg='bisque2')
        self.resizable(False, False)

        text_var = []
        entries = []

        # callback function to get your StringVars
        def get_mat():
            matrix = []
            for row in range(rows):
                matrix.append([])
                for col in range(cols):
                    matrix[row].append(text_var[row][col].get())
            matrix = [list(map(lambda x: int(x), row)) for row in matrix]
            self._window_subject.input_matrix = matrix
            self._window_subject.result_matrix = matrix

        tk.Label(self, text="Ввод матрицы :", font=('arial', 10, 'bold'),
                 bg="bisque2").place(x=20, y=20)

        x2 = 0
        y2 = 0
        rows, cols = self._window_subject.input_matrix_size
        for i in range(rows):
            # append an empty list to your two arrays
            # so you can append to those later
            text_var.append([])
            entries.append([])
            for j in range(cols):
                # append your StringVar and Entry
                text_var[i].append(tk.StringVar())
                entries[i].append(tk.Entry(self, textvariable=text_var[i][j], width=3))
                entries[i][j].place(x=60 + x2, y=50 + y2)
                x2 += 30

            y2 += 30
            x2 = 0
        button = tk.Button(self, text="Сохранить", bg='bisque3', width=15, command=get_mat)
        button.pack(side='bottom')

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

    def init_heights_button(self):
        def heights_click(event):
            api_res = requests.get("http://127.0.0.1:5000//algorithms/heights",
                                   json={"matrix": self.input_matrix}).json()
            if 'error' in api_res:
                print(api_res)
                return
            self._window_subject.result_matrix = api_res['matrix']

        btn = tk.Button(self,
                        text="Ввести матрицу",
                        width=15, height=5,
                        bg="white", fg="black")
        btn.bind("<Button-1>", heights_click)
        btn.pack()

    def update(self) -> None:
        pass
